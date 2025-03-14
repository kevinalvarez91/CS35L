(defun transpose-chars (args)
  "Interchage characters around point, moving forward one charcter."
  (interactive)
  (if (and (not (bobp))
	   (not (get-text-property (- (point) 1) 'read-only)))
      (forward-char -1))
  (transpose-subr 'forward-char 1))

#Write an Emacs Lisp function transpose2
(defun transpose2 (args)
  "Behavior like transpose, but transposes in terms of 2"
  (interactive)
  (if (and (not (bobp))
	   (not (get-text-property (- (point) 2) 'read-only)))
      (forward-char -2)
    (transpose-subr 'forward-char 2)
    (forward-char -1)
    (transpose-subr 'forward-char 3)
    ))
