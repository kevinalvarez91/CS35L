import { useState } from 'react';

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}
//if squares[i] != null, and user clicks on it, 
//allow user to click on empty squares and replace
//value of clicked square. The empty square must be adjecent to the clicked square
//

function Board({ xIsNext, squares, onPlay }) {
  const [userSquare, setuserSquare] = useState(null);

  function handleClick(i) {
    if (calculateWinner(squares)) {
      return;
    }

    const Xcount = squares.filter((square) => square === 'X').length;
    const Ocount = squares.filter((square) => square === 'O').length;
    const currentPlayer = xIsNext ? 'X' : 'O';
    const nextSquares = squares.slice();

    function isWinningMove(from, to) {
      const tempSquares = squares.slice();
      tempSquares[to] = tempSquares[from]; // Simulate move
      tempSquares[from] = null;
      return calculateWinner(tempSquares) === currentPlayer;
    }

    // Only apply the "must move center" logic once both players have placed all 3 pieces.
    if (Xcount === 3 && Ocount === 3) {
      // If the current player has the center piece, enforce movement rules.
      if (squares[4] === currentPlayer) {
        // Check if any move (from any piece, not just center) results in a win
        let canWin = false;
        for (let j = 0; j < 9; j++) {
          if (squares[j] === currentPlayer) {
            const adj = adjacentSquares(j);
            for (let k of adj) {
              if (squares[k] === null && isWinningMove(j, k)) {
                canWin = true;
                break;
              }
            }
          }
          if (canWin) break;
        }

        // If no winning move exists, restrict the player to moving the center piece
        if (!canWin) {
          // If no piece is selected yet, enforce selecting the center only
          if (userSquare === null) {
            if (i !== 4) {
              console.log(`Player ${currentPlayer} must move the center piece.`);
              return;
            }
            setuserSquare(i);
            return;
          } else {
            // Player is trying to move the selected piece
            const adjacent = adjacentSquares(userSquare);
            if (squares[i] === null && adjacent.includes(i)) {
              nextSquares[i] = squares[userSquare]; // Move the piece
              nextSquares[userSquare] = null;       // Clear old position
              setuserSquare(null);                  // Reset selection
              onPlay(nextSquares);
            } else {
              setuserSquare(null); // Deselect if clicking another occupied square
            }
            return;
          }
        }
      }
    }

    // If no piece is selected yet
    if (userSquare === null) {
      // If the square clicked isn't empty, try to select it if it matches the current player
      if (squares[i] !== null) {
        if ((xIsNext && squares[i] === 'X') || (!xIsNext && squares[i] === 'O')) {
          setuserSquare(i);
        }
      } else {
        // Place a new piece if you haven't placed all 3 yet
        if ((xIsNext && Xcount < 3) || (!xIsNext && Ocount < 3)) {
          nextSquares[i] = currentPlayer;
          onPlay(nextSquares);
        }
      }
    } 
    // If a piece is already selected, attempt to move it
    else {
      const adjacent = adjacentSquares(userSquare);
      if (squares[i] === null && adjacent.includes(i)) {
        nextSquares[i] = squares[userSquare]; // Move selected piece
        nextSquares[userSquare] = null;       // Clear old position
        setuserSquare(null);                  // Reset selection
        onPlay(nextSquares);
      } else {
        // Deselect if invalid move
        setuserSquare(null);
      }
    }
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = 'Winner: ' + winner;
  } else {
    status = 'Next player: ' + (xIsNext ? 'X' : 'O');
  }

  return (
    <>
      <div className="status">{status}</div>
      <div className="board-row">
        <Square value={squares[0]} onSquareClick={() => handleClick(0)} />
        <Square value={squares[1]} onSquareClick={() => handleClick(1)} />
        <Square value={squares[2]} onSquareClick={() => handleClick(2)} />
      </div>
      <div className="board-row">
        <Square value={squares[3]} onSquareClick={() => handleClick(3)} />
        <Square value={squares[4]} onSquareClick={() => handleClick(4)} />
        <Square value={squares[5]} onSquareClick={() => handleClick(5)} />
      </div>
      <div className="board-row">
        <Square value={squares[6]} onSquareClick={() => handleClick(6)} />
        <Square value={squares[7]} onSquareClick={() => handleClick(7)} />
        <Square value={squares[8]} onSquareClick={() => handleClick(8)} />
      </div>
    </>
  );
}


export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];

  function handlePlay(nextSquares) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
  }


  return (
    <div className="game">
      <div className="game-board">
        {/*Board is getting called here */}
        <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
      </div>
      <div className="game-info">
      </div>
    </div>
  );
}

//Calculate adjacent squares
function adjacentSquares(square) {
  const possabilities = [
    [1, 3, 4],                  //square 0
    [0, 2, 3, 4, 5],            //square 1
    [1, 4, 5],                  //square 2
    [0, 1, 4, 6, 7],            //square 3
    [0, 1, 2, 3, 5, 6, 7, 8],   //square 4
    [1, 2, 4, 7, 8],            //square 5
    [3, 4, 7],                  //square 6
    [3, 4, 5, 6, 8],            //square 7
    [4, 5, 7]                   //square 8
  ]
  return possabilities[square];
}

//leave algorithm as is
function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}
