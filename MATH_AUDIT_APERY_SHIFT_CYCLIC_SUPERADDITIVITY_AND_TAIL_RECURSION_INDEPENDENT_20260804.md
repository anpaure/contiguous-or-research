# Independent audit: cyclic superadditivity and Bellman recursion of Apéry shifts

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_APERY_SHIFT_CYCLIC_SUPERADDITIVITY_AND_TAIL_RECURSION_20260804.md`  
**Method:** independent symbolic proof replay; no search or numerical test.

## Verdict

**PASS after three explicit proof/scope repairs.**  The theorem now assumes
positive maximum density, translates the second attaining path before
concatenation, and treats endpoint-size parts explicitly in the Bellman
recursion.  With those repairs, every theorem and stated consequence is
correct.

## 1. Existence and attainment of the residue maxima

The reduced Cayley multigraph has `h` vertices and finitely many labelled
outgoing edges at each vertex.  Every edge weight is

\[
d_j=c_j-j\lambda\le0.
\]

The size-one edge reaches every residue, so the feasible walk family for
each residue is nonempty.  If a walk repeats a residue, delete the closed
segment between two occurrences.  The deleted segment has nonpositive
weight, so deletion cannot decrease the remaining walk's weight.  Repeating
this operation leaves a simple path.  There are only finitely many labelled
simple paths, hence the maximum `beta_r` exists and is attained.

For residue zero, the empty path has weight zero and no walk has positive
weight, so `beta_0=0` is exact even when zero-weight critical cycles exist.
Those cycles may be deleted without loss; they do not obstruct attainment.

The `r`-step size-one walk gives

\[
\beta_r\ge r(c_1-\lambda),
\]

so `s_r=r lambda+beta_r>=r c_1>=0`.  Since `beta_r<=0` and the repaired
hypothesis has `lambda>0`,

\[
0\le s_r\le r\lambda<P
\qquad(0\le r<h).
\]

The positive-density hypothesis is necessary for the strict inequality and
for convergence of the formal Gaussian train: if all `c_j=0`, then `P=0`
and the repeated train is not a finite functional.

## 2. Concatenation and the two carry inequalities

Let `Q_r,Q_t` attain `beta_r,beta_t`.  The graph is translation-invariant,
so translating `Q_t` by residue `r` and appending it to `Q_r` gives a walk
from zero to `r+t mod h` of weight `beta_r+beta_t`.  Cycle deletion is
optional here but confirms that an attaining simple candidate loses no
weight.  Hence

\[
\beta_{(r+t)\bmod h}\ge\beta_r+\beta_t.
\]

If `r+t<h`, adding `(r+t)lambda` gives

\[
s_{r+t}\ge s_r+s_t.
\]

If `r+t>=h`, use

\[
(r+t)\lambda=P+(r+t-h)\lambda
\]

to obtain

\[
P+s_{r+t-h}\ge s_r+s_t.
\]

These are exactly the no-carry and carry superadditivity inequalities for
the table `(0,s_1,...,s_(h-1),P)`.  In addition,
`s_r/r<=lambda=P/h`, so the endpoint remains a maximum-efficiency
generator.

## 3. Exact Bellman-tail recursion

The lower bound

\[
W_{qh+r}\ge qP+s_r
\]

is realized by `q` endpoint parts and one residue-`r` part.

For the reverse bound, assign state `0P+s_j` to a sub-endpoint part of size
`j<h` and state `1P+s_0` to an endpoint part of size `h`.  Combining two
states uses the appropriate inequality from Section 2 and adds one to the
quotient exactly when the residues carry through `h`.  Consequently, after
all parts of any exact fill of capacity `qh+r` are combined, their total
value is at most `qP+s_r`.  Thus

\[
                         W_{qh+r}=qP+s_r
\]

for every `q>=0` and `0<=r<h`.  Because `P>0`, its Gaussian tail converges
absolutely, so summing the exact formula yields the displayed formal Apéry
functional.

## 4. Consequence audit

1. Both ordinary and carry superadditivity of stabilized Apéry shifts are
   direct consequences of the residue maximum; the shifts cannot be chosen
   independently.
2. If `P>=A` and the Bellman inequality is known for grid size `h`, the
   constructed table lies in that theorem's domain.  Its complete formal
   tail is therefore positive.  In an availability-filtered Apéry normal
   form, only the separately displayed finite head remains to be priced.
3. In the five-slot size-three-efficient branch, the shifts

   \[
   s_1=\max(a,2b-p),
   \qquad
   s_2=\max(b,2a)
   \]

   are exactly the two Apéry residue maxima.  The no-carry inequality at
   `1+1=2` gives `s_2>=2s_1`, and the carry inequality at `1+2=3` gives
   `p>=s_1+s_2`.  Hence the eventual train is the exact Bellman clock of an
   honest three-slot table.  When `p<A`, this is structural recursion only;
   a first-crossing theorem with endpoint at least `A` cannot be invoked.

## 5. Exact scope

The theorem proves an algebraic Bellman representation of the stabilized
tail.  It neither prices an availability head nor proves positivity when
the formal period is subthreshold.  It makes no all-slot Bellman or OR-word
claim.
