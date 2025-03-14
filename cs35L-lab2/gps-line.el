(defun gps-line ()
  "Print the current buffer line number and narrowed line number of point."
  (interactive)
  (let ((start (point-min))
        (n (line-number-at-pos))
        (total-line (line-number-at-pos (point-max)))
	(lines (count-matches "\n" 0))
	)
    (if (= start 1)
        (message "Line %d/%d" n lines)
      (save-excursion
        (save-restriction
          (widen)
          (message "line %d (narrowed line %d)"
                   (+ n (line-number-at-pos start) -1) n))))))


(defun gps-count-newlines()
  "this function counts the number of newlines"
  (let ((line-count 0))
    (save-excursion
      (goto-char (point-min))
      (while (re-search-forward "\n" nil t) ;; searching for newlines
	(setq line-count (1+ line-count))) ;; increment line count
      (if (not (eq (char-before (point-max)) ?\n)) ;; If the last character is not a newline
	  (setq line-count (1- line-count))) ;; subtract 1 to not count the last
      )
    line-count)) ;; retun line count
