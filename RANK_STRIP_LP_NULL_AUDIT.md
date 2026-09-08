# Audit of the rank-strip LP experiment

## Verdict

The reported equalities

```text
minholes = allowed
```

for odd `k=11,13,...,21` are identities forced by the equality constraints
of the LP.  They are not an optimization result and provide no evidence for
or against `nu(k)=B(k)`.

No "two-core theorem" was stated or proved in the accompanying trace.

## The forced objective

In the experiment `d=3`, `n=M+3`, and the variables are

* `z[l,s]`: selected targets of rank `s` in physical window row `l`, for
  `l=0,1,2` (window lengths `1,2,3`);
* `h_l`: unused cells, called holes, in row `l`.

The three physical-row equalities are

\[
 \sum_s z_{l,s}+h_l=n-l\qquad(l=0,1,2).
\]

The rank-total equalities are

\[
 \sum_{l=0}^2 z_{l,s}=\binom{k}{s}
 \qquad(1\le s\le r).
\]

Summing the first family and subtracting the second gives

\[
 \begin{aligned}
 h_0+h_1+h_2
   &= (n+(n-1)+(n-2))-\sum_{s=1}^r\binom{k}{s}\\
   &=3M+6-\sum_{s=1}^r\binom{k}{s}.
 \end{aligned}
\]

For odd `k`, the two middle binomial coefficients agree, so with
`M=C(k,r)=C(k,r+1)` this is exactly the script's `sig`:

\[
 3M+6-\left(M+\sum_{s=1}^{r-1}\binom{k}{s}\right)
 =2M+6-\sum_{s=1}^{r-1}\binom{k}{s}.
\]

But the objective minimized by `linprog` is precisely

\[
                         h_0+h_1+h_2.
\]

It is therefore constant on the feasible region.  The additional expansion
inequalities may test feasibility of that rank-marginal relaxation, but they
cannot lower or raise the displayed objective.

## What can legitimately be retained

The finite LP runs show only that this particular coarse rank-marginal
relaxation is feasible for the printed cases.  The relaxation forgets:

* physical order inside each row;
* simultaneous realization of nested windows;
* coordinatewise contamination and pin survival;
* the upper-rank interval maxima.

Thus any useful strengthening must introduce at least one of those coupled
structures.  Adding further inequalities while retaining only row-by-rank
totals is unlikely to address the actual obstruction.

