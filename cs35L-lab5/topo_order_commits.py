#!/usr/bin/env python3

# Recommended libraries. Not all of them may be needed.
import copy, os, sys, re, zlib
from collections import deque

# Note: This is the class for a doubly linked list. Some implementations of
# this assignment only require the `self.parents` field. Delete the
# `self.children` field if you don't think its necessary.
class CommitNode:
    def __init__(self, commit_hash):
        """
        :type commit_hash: str
        """
        self.commit_hash = commit_hash
        self.parents = set()
        self.children = set()


# ============================================================================
# ======================== Auxiliary Functions ===============================
# ============================================================================

def in_git_directory() -> bool:
    """
    :rtype: bool

    Checks if `topo_order_commits.py` is inside a Git repository.
    """
    
    pass


def get_branch_hash(branch_name : str) -> str:
    """
    :type branch_name: str
    :rtype: str

    Returns the commit hash of the head of a branch.
    """
    pass


def decompress_git_object(commit_hash : str, path : str) -> list[str]:
    """
    :type commit_hash: str
    :rtype: list

    Decompresses the contents of a git object and returns a
    list of the decompressed contents.
    """
    # The first 2 characters form the directory, the remaining 38 form the filename
    obj_dir = commit_hash[:2]
    obj_file = commit_hash[2:]
    
    # Construct the path to the git object
    git_object_path = os.path.join(path, ".git", "objects", obj_dir, obj_file)
    
    # Read the compressed data
    with open(git_object_path, "rb") as f:
        compressed_data = f.read()
    
    # Decompress using zlib
    decompressed_data = zlib.decompress(compressed_data)
    
    # Git objects start with a header like "commit <size>\0", "tree <size>\0", etc.
    # We split on the first null byte to separate the header from the actual content.
    content = decompressed_data.split(b'\x00', 1)
    
    # Decode the actual content from bytes to string
    decoded_content = content[1].decode('utf-8', errors='replace')

    parent_hashes = []
    for line in decoded_content.splitlines():
        if line.startswith("parent"):
            parent_hash = line.split()[1]
            parent_hashes.append(parent_hash)

    return parent_hashes
    pass


# ============================================================================
# =================== Part 1: Discover the .git directory ====================
# ============================================================================

def get_git_directory() -> str:
    """
    :rtype: str
    Returns absolute path of `.git` directory.
    """
    directory = os.path.abspath(os.getcwd())  # Use the current working directory

    while True:
        git_path = os.path.join(directory, ".git")
        if os.path.isdir(git_path):
            return directory  # .git found, return the directory
        
        parent_directory = os.path.dirname(directory)  # Move up one level
        if parent_directory == directory:  # If the root is reached
            print("Not inside a Git repository", file=sys.stderr)
            sys.exit(1)
        
        directory = parent_directory

    pass


# ============================================================================ 
# =================== Part 2: Get the list of local branch names =============
# ============================================================================

def get_branches(path : str) -> list[tuple[str, str]]:
    """
    :type path: str
    :rtype: list[(str, str)]

    Returns a list of tupes of branch names and the commit hash
    of the head of the branch.
    """
    #.git/refs/heads
    branches_directory = os.path.join(path, ".git/refs/heads")
    if not os.path.isdir(branches_directory):
        print("No local branches found.")
        return []  # Return empty list because no branchs exist

    branches = []

    def traverse_branches(current_path, branch_prefix=""):
        for entry in os.listdir(current_path):
            entry_path = os.path.join(current_path, entry)

            if os.path.isdir(entry_path):  
                #recursiion
                traverse_branches(entry_path, branch_prefix + entry + "/")
            else:
                with open(entry_path, "r") as file:
                    commit_hash = file.read().strip()
                    branch_name = branch_prefix + entry  # Build full branch name
                    branches.append((branch_name, commit_hash))

    # Start traversal from the top-level branches directory
    traverse_branches(branches_directory)
    return branches
    pass


# ============================================================================
# =================== Part 3: Build the commit graph =========================
# ============================================================================

def build_commit_graph(branches_list: list[(str, str)], path: str) -> dict[str, CommitNode]:
    """
    :type branches_list: list[(str, str)]
    :rtype: dict[str, CommitNode]

    Iteratively builds the commit graph from the list of branches and
    returns a dictionary mapping commit hashes to CommitNode objects.
    """
    commit_graph = {}
    frontier = {commit_hash for _, commit_hash in branches_list}

    while frontier:
        new_frontier = set()
        for commit_hash in frontier:
            if commit_hash not in commit_graph:
                parents = decompress_git_object(commit_hash, path)

                # Create a CommitNode for this commit
                commit_node = CommitNode(commit_hash)
                commit_node.parents = set(parents)

                # Add the commit to the graph
                commit_graph[commit_hash] = commit_node

                # Add parents to the new frontier if they haven't been processed
                for parent in parents:
                    if parent not in commit_graph:
                        new_frontier.add(parent)

        # Update the frontier for the next iteration
        frontier = new_frontier

        # Print the current frontier for debugging

    # Update children references
    for commit_hash, commit_node in commit_graph.items():
        for parent_hash in commit_node.parents:
            if parent_hash in commit_graph:
                commit_graph[parent_hash].children.add(commit_hash)
    return commit_graph




# ============================================================================
# ========= Part 4: Generate a topological ordering of the commits ===========
# ============================================================================


def topo_sort(root_commits: list[CommitNode], commit_graph: dict[str, CommitNode]) -> list[str]:
    """
    :type root_commits: list[CommitNode]
    :type commit_graph: dict[str, CommitNode]
    :rtype: list[str]

    Generates a topological ordering of the commits in the commit graph
    using Kahn's Algorithm. The ordering ensures that all descendants
    come after their ancestors in the final list.
    """

    # L will store the resulting topological order (list of commit hashes).
    L = []

    # Compute in-degree (number of parents) for each commit.
    # in_degree[commit_hash] = number of parents that commit still has.
    in_degree = {}
    for commit_hash, node in commit_graph.items():
        in_degree[commit_hash] = len(node.parents)

    # Initialize a queue (or set) with all root commits (those having 0 parents).
    S = deque()
    for root in root_commits:
        S.append(root.commit_hash)

    # While there are nodes with no incoming edges:
    while S:
        # Remove one such node n from S.
        n = S.popleft()

        # Add n to the end of the topological order list.
        L.append(n)

        # For each node m that n points to (n's children):
        for child_hash in commit_graph[n].children:
            # "Remove" the edge n→m by decrementing m's in_degree.
            in_degree[child_hash] -= 1

            # If m now has no incoming edges, add it to S.
            if in_degree[child_hash] == 0:
                S.append(child_hash)

    # If we didn't include all nodes, there's a cycle in the graph.
    if len(L) < len(commit_graph):
        # For real-world usage, you might want to raise an error or print a warning.
        print("Warning: the commit graph has at least one cycle.", file=sys.stderr)

    return L[::-1]



# ============================================================================
# ===================== Part 5: Print the commit hashes ======================
# ============================================================================

def ordered_print(
    commit_nodes : dict[str, CommitNode],
    topo_ordered_commit : list[str],
    head_to_branches : dict[str, list[str]]
):
    """
    :type commit_nodes: dict[str, CommitNode]
    :type topo_ordered_commits: list[str]
    :type head_to_branches: dict[str, list[str]]

    Prints the commit hashes in the the topological order from the last
    step. Also, handles sticky ends and printing the corresponding branch
    names with each commit.
    """
    if not topo_ordered_commit:
        return

    # Print the first commit line.
    first_commit = topo_ordered_commit[0]
    if first_commit in head_to_branches:
        branches = sorted(head_to_branches[first_commit])
        print(f"{first_commit} {' '.join(branches)}")
    else:
        print(first_commit)

    # Process the rest of the commits.
    for i in range(len(topo_ordered_commit) - 1):
        current = topo_ordered_commit[i]
        next_commit = topo_ordered_commit[i + 1]

        # Check if the next commit is a direct parent of the current commit.
        if next_commit not in commit_nodes[current].parents:
            # Build and print sticky end for current commit.
            parents = list(commit_nodes[current].parents)
            if not parents:
                sticky_end_line = "="
            else:
                # Append '=' to the last parent in the list.
                sticky_end_line = " ".join(parents[:-1] + [parents[-1] + "="])
            print(sticky_end_line)
            print()  # Print an empty line.

            # Build and print sticky start for the next commit.
            children = list(commit_nodes[next_commit].children)
            if not children:
                sticky_start_line = "="
            else:
                # The '=' is immediately followed by the first child hash.
                sticky_start_line = "=" + " ".join(children)
            print(sticky_start_line)

        # Print the next commit line with branch names if applicable.
        if next_commit in head_to_branches:
            branches = sorted(head_to_branches[next_commit])
            print(f"{next_commit} {' '.join(branches)}")
        else:
            print(next_commit)



# ============================================================================
# ==================== Topologically Order Commits ===========================
# ============================================================================

def topo_order_commits():
    """
    Combines everything together.
    """


    # Check if you are inside a Git repository.
    # Part 1: Discover the .git directory.
    directory_path = get_git_directory()
    # Part 2: Get the list of local branch names.
    branches = get_branches(directory_path)
    # Part 3: Build the commit graph
    commit_graph = build_commit_graph(branches, directory_path)
    # Part 4: Generate a topological ordering of the commits in the graph.
    # root_commits = [commit_graph[commit_hash] for commit_hash in commit_graph if not commit_graph[commit_hash].parents]
    root_commits = []
    for commit_hash in commit_graph:
        commit = commit_graph[commit_hash]
        if not commit.parents: #getting the roots
            root_commits.append(commit)

    topo_ordered_commit = topo_sort(root_commits, commit_graph)
    # Generate the head_to_branches dictionary showing which
    # branches correspond to each head commit
    # # Part 5: Print the commit hashes in the topological order.
    head_to_branches = {}
    for branch_name, commit_hash in branches:
        head_to_branches.setdefault(commit_hash, []).append(branch_name)

    # Call the ordered_print function to print the commits.
    ordered_print(commit_graph, topo_ordered_commit, head_to_branches)



# ============================================================================

if __name__ == '__main__':
    topo_order_commits()

 