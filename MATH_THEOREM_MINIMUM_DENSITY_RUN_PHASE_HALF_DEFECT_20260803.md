# Minimum-density run phases lose asymptotically half the lower targets

**Date:** 2026-08-03  
**Status:** unconditional density obstruction on every complete resident
cyclic Johnson carrier **when each positive run is represented by an exact
minimum owner-hitting net**, or by one canonical residue class plus its
mandatory endpoint corrections.  No computation is used.  The half-defect
conclusion does not apply to arbitrary denser, two-rail, or multi-rail
occurrence systems.

## 0. Outcome

Put

\[
 W={k\choose r},\qquad
 \Lambda=\sum_{s=1}^{r-1}{k\choose s},\qquad
 M=\sum_{s=1}^{r-1}s{k\choose s},                    \tag{0.1}
\]

and let \(d\) be the optimal lower-bound depth.  Write

\[
                         D=d+1.                       \tag{0.2}
\]

Assume \(1\le d<W\); the finitely many depth-zero cases have no nontrivial
run-phase question.

Let \(T_0,\ldots,T_{W-1}\) be any cyclic Johnson carrier which visits the
complete rank-\(r\) layer once and whose positive coordinate runs all have
length at least \(D\).

For every coordinate and every one of its positive owner runs of length
\(L\), the erosion interval has \(L-d\) source positions.  Any occurrence
set which

* contains both mandatory erosion endpoints, and
* hits every length-\(D\) owner window

has minimum possible cardinality

\[
                         \tau(L)=\left\lceil{L\over D}\right\rceil
                                                               \tag{0.3}
\]

points at minimum density.

The crucial global identity is

\[
 \boxed{\text{the complete cyclic carrier has exactly \(W\)
 positive coordinate runs in total}.}                 \tag{0.4}
\]

There is one run birth at every Johnson transition.  Also the sum of all
run lengths is \(rW\).  Consequently the total number \(P\) of occurrence
points in all exact minimum-density run nets satisfies

\[
                         P\le {W(r+d)\over d+1}.       \tag{0.5}
\]

For any phase choices, the total rank mass of all cyclic \(q\)-cell
signatures, \(1\le q\le d\), is at most

\[
 \boxed{
 \sum_{q=1}^{d}\sum_{j\in\mathbb Z_W}|V_Z(j,q)|
 \le {Wd(r+d)\over2}.}                                \tag{0.6}
\]

By contrast, the strict lower ideal has total rank mass \(M\).  Therefore,
if \(\delta\) lower targets are omitted, then even after granting every
linear boundary cell its maximum possible lower rank,

\[
 \boxed{
 \delta\ge
 \left\lceil
 {\,M-\frac12Wd(r+d)
       -(r-1){d+1\choose2}\over r-1}
 \right\rceil_+.}                                    \tag{0.7}
\]

For the central ranks \(r=\lceil k/2\rceil\),

\[
 \boxed{
 \delta\ge
 \left({1\over2}-O(k^{-1/2})\right)\Lambda.}          \tag{0.8}
\]

Thus choosing one minimum-density net on every erosion run cannot give
bounded lower-target deficiency.  It misses asymptotically at least half of
the entire lower ideal, regardless of how those per-run nets are correlated
or phased.  This statement is not asserted for a denser occurrence system.

The usual canonical phase

\[
 \{\text{both endpoints}\}\cup
 \{h:h\equiv\theta\pmod D\}                           \tag{0.9}
\]

uses at most one point more than minimum on each run.  It obeys the robust
variant

\[
 \sum_{q,j}|V_Z(j,q)|
 \le {Wd(r+2d+1)\over2},                              \tag{0.10}
\]

and hence has the same asymptotic half-defect (0.8).

Equivalently, every bounded-defect signature needs asymptotically twice the
number of occurrence points supplied by a minimum owner-hitting net.  A
single run phase is therefore the wrong integral object; two rails are the
first density scale not ruled out by rank mass.

## 1. Exact minimum owner nets on one run

Consider one positive owner run

\[
                         T_s,T_{s+1},\ldots,T_t
                                                               \tag{1.1}
\]

of length

\[
                         L=t-s+1\ge D.                \tag{1.2}
\]

Its erosion interval is

\[
                         R=[s+d,t],                   \tag{1.3}
\]

with

\[
                         |R|=L-d=L-D+1.               \tag{1.4}
\]

The positions \(s+d\) and \(t\) are mandatory: they carry respectively
the lagged arrival and current departure of the coordinate.

Here and below a cyclic run is first unwrapped to an integer interval.  If
the run coordinate is `x`, then the transition into the run is
`beta_(s-1)=x`, the transition out is `alpha_t=x`, and an occurrence marker
at source index `h` means `x in A_h`.  The mandatory-collar lemma therefore
places the two compulsory source markers at

\[
 (s-1)+d+1=s+d
 \qquad\hbox{and}\qquad
 t.                                                     \tag{1.4a}
\]

This convention is the reason the erosion interval is `[s+d,t]`; neither
endpoint is shifted by one transition.

### Lemma 1.1 (exact transversal number)

The minimum size of a set \(Z\subseteq R\) which contains both endpoints
and hits every owner-supplier interval is

\[
                         |Z|_{\min}=\left\lceil{L\over D}\right\rceil.
                                                               \tag{1.5}
\]

#### Proof

Write the selected positions in increasing order.  The two endpoints are
selected, and every gap between consecutive selected positions is at most
\(D\); otherwise a length-\(D\) source window inside that gap misses \(Z\).
Conversely, endpoint inclusion and gaps at most \(D\) hit every clipped or
unclipped owner-supplier interval.

The endpoint span is

\[
                         |R|-1=L-D.                   \tag{1.6}
\]

If \(p\) points are selected, their \(p-1\) gaps have total \(L-D\) and
size at most \(D\), so

\[
 p\ge1+\left\lceil{L-D\over D}\right\rceil
   =\left\lceil{L\over D}\right\rceil.                \tag{1.7}
\]

Taking successive gaps of size \(D\), followed by the final remainder,
attains the bound. \(\square\)

### Lemma 1.2 (canonical residue phases cost at most one extra point)

For any \(\theta\in\mathbb Z_D\), put

\[
 Z_\theta=\{s+d,t\}\cup
 \{h\in[s+d,t]:h\equiv\theta\pmod D\}.                \tag{1.8}
\]

Then \(Z_\theta\) is an owner-hitting net and

\[
                         |Z_\theta|\le\tau(L)+1.      \tag{1.9}
\]

#### Proof

Successive lattice points have gap \(D\), while each endpoint is within
\(D\) of the nearest lattice point, so the set is an owner net.

Put \(n=|R|\).  If \(D\nmid n-1\), the lattice contributes at most
\(\lfloor(n-1)/D\rfloor+1\) points and the two endpoints give at most
\[
 \left\lfloor{n-1\over D}\right\rfloor+3
 =1+\left\lceil{n-1\over D}\right\rceil+1
 =\tau(L)+1.                                         \tag{1.10}
\]

If \(D\mid n-1\), a lattice phase with the maximum
\((n-1)/D+1\) points contains both endpoints.  Every other phase has at
most \((n-1)/D\) points before the endpoints are added.  The same bound
follows. \(\square\)

## 2. The global run ledger

### Lemma 2.1 (exactly one run per carrier transition)

Across all coordinates, the carrier has exactly \(W\) positive runs, and
their lengths sum to \(rW\).

#### Proof

At every Johnson transition

\[
                         T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}, \tag{2.1}
\]

the inserted coordinate \(\beta_i\) was absent from \(T_i\), so this
transition begins one new positive run.  Every positive run has exactly
one such arrival transition.  There are \(W\) cyclic transitions, proving
the run count.

Counting coordinate-owner incidences first by owners and then by positive
runs gives

\[
                         \sum_R L(R)=\sum_i|T_i|=rW.  \tag{2.2}
\]

\(\square\)

### Theorem 2.2 (global minimum-net size)

If every run uses an exact minimum net, then

\[
                         P:=\sum_R|Z\cap R|
                         \le {W(r+d)\over D}.          \tag{2.3}
\]

If every run uses a canonical residue phase with endpoint corrections,
then

\[
                         P\le {W(r+d)\over D}+W
                         ={W(r+2d+1)\over D}.          \tag{2.4}
\]

#### Proof

For minimum nets, Lemmas 1.1 and 2.1 give

\[
\begin{aligned}
 P
 &=\sum_R\left\lceil{L(R)\over D}\right\rceil\\
 &\le\sum_R{L(R)+D-1\over D}
 ={rW+dW\over D}.
                                                               \tag{2.5}
\end{aligned}
\]

Lemma 1.2 adds at most one point on each of the exactly \(W\) runs, proving
(2.4). \(\square\)

## 3. Signature rank mass

For a cyclic \(q\)-cell \(c=(j,q)\), define its signature

\[
                         V_Z(j,q)=
 \{x:[j,j+q-1]_W\cap Z_x\ne\varnothing\}.             \tag{3.1}
\]

### Lemma 3.1 (one occurrence has \(q\) cell flags)

For every coordinate \(x\) and every \(1\le q\le d\),

\[
 \left|\{j:[j,j+q-1]_W\cap Z_x\ne\varnothing\}\right|
 \le q|Z_x|.                                         \tag{3.2}
\]

#### Proof

One occurrence position belongs to exactly \(q\) forward cyclic intervals
of length \(q\).  Taking the union of these \(q\)-element start sets over
the points of \(Z_x\) gives (3.2).  Overlaps only decrease the count.
\(\square\)

### Theorem 3.2 (total cyclic signature mass)

If \(P=\sum_x|Z_x|\), then

\[
\begin{aligned}
 H_Z
 &:=\sum_{q=1}^{d}\sum_{j\in\mathbb Z_W}|V_Z(j,q)|\\
 &\le\sum_x|Z_x|\sum_{q=1}^{d}q
 ={dD\over2}P.                                       \tag{3.3}
\end{aligned}
\]

Consequently exact minimum nets satisfy

\[
                         H_Z\le {Wd(r+d)\over2},       \tag{3.4}
\]

and canonical residue phases with endpoint corrections satisfy

\[
                         H_Z\le {Wd(r+2d+1)\over2}.   \tag{3.5}
\]

#### Proof

Interchange the coordinate and cell sums:

\[
 \sum_{q,j}|V_Z(j,q)|
 =\sum_x\sum_q
   |\{j:[j,j+q-1]_W\cap Z_x\ne\varnothing\}|.
                                                               \tag{3.6}
\]

Apply Lemma 3.1, sum \(q=1,\ldots,d\), and then use Theorem 2.2.
\(\square\)

This is independent of all phase choices.  Phase tuning redistributes the
rank mass among cells but cannot increase its total beyond (3.4) or (3.5).

## 4. Exact lower-defect inequality

Let \({\cal B}_{<r}\) be the family of all nonempty targets of rank below
\(r\).  Its cardinality and rank mass are \(\Lambda\) and \(M\) from
(0.1).

Suppose distinct cyclic \(q\)-cells realize all but \(\delta\) members of
\({\cal B}_{<r}\).  The omitted targets have rank at most \(r-1\), so the
matched targets have total rank at least

\[
                         M-\delta(r-1).               \tag{4.1}
\]

Their cells are a subfamily of all cyclic \(q\)-cells.  Hence (4.1) is at
most \(H_Z\).

A linear word of length \(W+d\) has, beyond the \(W\) cyclic positions in
each row, at most

\[
                         B_\partial={d+1\choose2}     \tag{4.2}
\]

additional short boundary cells.  Even if every one carries a distinct
rank-\((r-1)\) target, their total extra rank mass is at most
\((r-1)B_\partial\).

### Theorem 4.1 (exact phase-only defect bound)

For exact minimum-density run nets,

\[
 \delta\ge
 \left\lceil
 {\,M-\frac12Wd(r+d)
       -(r-1){d+1\choose2}\over r-1}
 \right\rceil_+.                                     \tag{4.3}
\]

For canonical residue phases with endpoint corrections,

\[
 \delta\ge
 \left\lceil
 {\,M-\frac12Wd(r+2d+1)
       -(r-1){d+1\choose2}\over r-1}
 \right\rceil_+.                                     \tag{4.4}
\]

#### Proof

Combine (4.1), Theorem 3.2, and the maximal boundary allowance (4.2), then
rearrange. \(\square\)

### Corollary 4.2 (necessary occurrence density)

Any signature system with lower-target defect at most \(\delta\) must have

\[
 \boxed{
 \sum_x|Z_x|
 \ge {2\bigl(M-\delta(r-1)
 -(r-1){d+1\choose2}\bigr)\over d(d+1)}.}             \tag{4.5}
\]

Thus the obstruction is not peculiar to residue grids.  It is a necessary
total occurrence count for every protected signature.

## 5. Central-rank asymptotics

Take \(r=\lceil k/2\rceil\).  The total target rank has the exact forms

\[
\begin{array}{ll}
k=2m+1,\ r=m+1:&
\displaystyle
 \Lambda=4^m-1,\qquad
 M={2m+1\over2}
   \left(4^m-{2m\choose m}\right),\\[3mm]
k=2m,\ r=m:&
\displaystyle
 \Lambda={4^m-{2m\choose m}\over2}-1,\qquad
 M=2m\left(4^{m-1}-{2m-1\choose m-1}\right).
\end{array}                                             \tag{5.1}
\]

These follow from

\[
 \sum_{s=1}^{r-1}s{k\choose s}
 =k\sum_{t=0}^{r-2}{k-1\choose t}.                    \tag{5.2}
\]

The central-binomial estimate gives

\[
                         {M\over\Lambda}
                         =r-\Theta(\sqrt k).          \tag{5.3}
\]

The optimal-depth definition gives

\[
                         d=\Theta(\sqrt k),\qquad
                         Wd=\Lambda\bigl(1+O(d^{-1})\bigr).
                                                               \tag{5.4}
\]

Indeed, minimality of \(d\) and the triangular correction imply

\[
 \Lambda-(d+1)d/2\le dW<\Lambda+W.                    \tag{5.5}
\]

Substituting (5.3)--(5.5) into either (4.3) or (4.4),

\[
\begin{aligned}
 M-\frac12Wd\bigl(r+O(d)\bigr)
 &=\Lambda\left({r\over2}-O(\sqrt k)\right),\\
 (r-1){d+1\choose2}&=o(\Lambda).
                                                               \tag{5.6}
\end{aligned}
\]

Division by \(r-1=\Theta(k)\) proves

\[
                         \delta\ge
 \left({1\over2}-O(k^{-1/2})\right)\Lambda.           \tag{5.7}
\]

This proves (0.8).

## 6. The precise structural lesson

Owner coverage alone asks only for gaps at most \(D=d+1\).  A minimum net
therefore has approximately one occurrence per \(D\) positions of a
positive run.  But the lower ideal is concentrated within
\(O(\sqrt k)\) ranks of the middle layer, so a typical compiled cell needs
roughly twice the rank mass generated by those sparse nets.

Quantitatively, Corollary 4.2 and (5.3)--(5.4) require

\[
                         \sum_x|Z_x|
 \ge (2-o(1)){rW\over d+1}                            \tag{6.1}
\]

for bounded defect.  Exact minimum owner nets have at most

\[
                         {W(r+d)\over d+1}
 =(1+o(1)){rW\over d+1}.                              \tag{6.2}
\]

No independence hypothesis is needed for this comparison: arbitrary
correlation among the per-run minimum nets leaves their total occurrence
count unchanged.  What is load-bearing is the one-net-per-run density
bound, not probabilistic independence.

Therefore:

\[
\boxed{
\begin{gathered}
\text{one minimum-density residue phase per run cannot support}\\
\text{an exact or additive-constant lower compiler;}\\
\text{two occurrence rails are the first density scale not ruled out.}
\end{gathered}}                                       \tag{6.3}
\]

This is only a density theorem.  Its half-defect conclusion is confined to
the exact-minimum and single-residue-plus-endpoints classes specified
above.  Corollary 4.2 is the broader necessary occurrence-count statement;
it does not say that every arbitrary signature has half defect.  Two rails
may still fail aperture, matching, owner, upper, or regeneration
constraints.  The positive all-\(k\) target should now be a protected
**two-rail signature theorem**, not a one-phase matching theorem.
