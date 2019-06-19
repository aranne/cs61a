; If we don't use macro.
> (define (check val) (if val 'passed 'failed))

; test it:
> (define x -2)
> (check (> x 0))
failed


; However if we use a macro, we can see the checked expression.
> (define-macro (check expr)
                (list 'if expr
                               ''passed                               ;Here we use double '' because (list ...) will consume one '
                               (list 'quote (list 'failed: expr))
                )
  )

; now test the new macro one:
> (define x -2)
> (check (> x 0))
(failed: (> x 0))           ; expr is substituted by (> x 0) before we evaluate it.


; We can also use Quasi-quotation(a backtick `) to simplify the macro procedure.
> (define-macro (check expr)
                `(if ,expr 'passed '(failed: ,expr))
  )
