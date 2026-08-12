# Independent audit of `FIRST_DANGEROUS_GLOBAL_SERVICE.md`

## 1. Verdict

The first-dangerous assignment and its main estimate are mathematically
sound under the dangerous-plateau convention already fixed in
`BRAID_GAP_SERVICE_AUDIT.md`:

* dangerous plateaux remain the original, untruncated maximal peak
  plateaux;
* their **vertex union** is used when defining the intervening gaps;
* a shared endpoint is omitted only as an assignment start, and is not put
  back into a gap; and
* containment in a forward window always refers to the original plateau.

In particular, I could not construct a counterexample to

\[
 n_j\le
 \min\{L-\lambda_j,\lambda_{j-1}+1+g_{j-1}\}.       \tag{1.1}
\]

There is a short direct proof which is slightly cleaner than the prose in
the source.  A start assigned to `P_j` lies in

\[
 [u_{j-1},u_j-1],                                   \tag{1.2}
\]

and this interval has at most
`lambda_(j-1)+1+g_(j-1)` positions.  If two consecutive dangerous
plateaux share an endpoint, it actually has one fewer position, so the
claimed bound remains safe.

The following claims all check out:

1. the dangerous-free-window reduction;
2. all forward-window and internality quantifiers;
3. the `L+1=4a+3` one-sided span and congestion bound;
4. the first-dangerous localization (1.1);
5. the cyclic secant calculation and the coefficient `2e_c`;
6. both displayed seam bounds; and
7. the component-free conclusion from `e_c=o(1)` for a fixed
   `c<4/3`.

There are only minor qualifications.

* The sentence in Section 4 saying that the interval from `u_(j-1)` to
  `u_j-1` “consists of the `lambda_(j-1)+1` vertices” is not literally
  correct when the two plateaux share an endpoint.  In that case it
  contains only `lambda_(j-1)` vertices of the preceding plateau.  This is
  slack in the safe direction and does not affect (4.1) or anything after
  it.
* The proof should split off the vacuous case `m=0` before referring to
  `P_1`, `lambda_m`, or a cyclic sum.  When `m=0`, every forward window is
  cheap and the theorem follows immediately.
* In the phrase `sigma=cs+o(1)`, the inherited notation
  `s=m/a` should be stated.  Then `e_c=sigma-cs` holds identically.
* Shared endpoints must remain in the dangerous vertex union.  Literally
  deleting them before defining the gaps would invalidate the gap formula
  and could invalidate the dangerous-free interpretation.  The source's
  reference to the audited convention is enough, but this point should not
  be weakened in later reuse.

There is also a free strengthening of the first seam estimate:

\[
 H_c\le
 \left(4-c+{2\over a}\right)e_c
 -{1\over a^3}\sum_j\delta_j^2
 \le(4-c+o(1))e_c.                                  \tag{1.3}
\]

The source's `(4+o(1))e_c` is valid, just looser.

## 2. Plateau geometry and overlap conventions

Write the dangerous plateaux as their original word intervals

\[
                         P_j=[u_j,v_j],
 \qquad \lambda_j=v_j-u_j>ca.                       \tag{2.1}
\]

Their ordering-edge sets are pairwise disjoint.  Indeed, if plateaux of two
different coordinates shared one ordering edge, the two endpoints would
agree in two coordinates; the zero-sum constraint would force agreement in
the third coordinate as well, contradicting distinctness of the ordered
points.  Plateaux of the same coordinate are distinct maximal constant
intervals and likewise share no edge.

It follows that, in word order,

\[
                         v_{j-1}\le u_j.             \tag{2.2}
\]

Equality is the only possible vertex overlap.  Such an overlap is a common
endpoint of the two plateaux.  No three nontrivial plateaux can share one
position, because only two ordering edges meet a position.  Consequently,
if

\[
 \omega=\sum_j(\lambda_j+1)
          -\left|\bigcup_jP_j\right|,
\]

then

\[
                         0\le\omega\le m-1.          \tag{2.3}
\]

The required convention is therefore:

\[
 \mathcal P=\bigcup_jP_j,
 \qquad
 \text{gaps are the components of }[1,M_a]\setminus\mathcal P. \tag{2.4}
\]

A common endpoint remains in `mathcal P`; it may separately be omitted
from the set of starts.  Under this convention, the number of positions
outside all dangerous plateaux is exactly

\[
 G=M_a-\sum_j(\lambda_j+1)+\omega
   =M_a-\sum_j\lambda_j-m+\omega.                   \tag{2.5}
\]

Since every dangerous plateau has more than `ca` edges and all these edge
sets are disjoint,

\[
 mca<\sum_j\lambda_j\le M_a-1,
 \qquad m=O(a).                                     \tag{2.6}
\]

Thus omitting all shared endpoints costs only `O(a)` starts, and any later
fan-capped penalty for them is `O(a^2)`.

## 3. Dangerous-free windows

For

\[
                         1\le i\le M_a-L,
 \qquad W_i=[i+1,i+L],                              \tag{3.1}
\]

`W_i` contains exactly `L` word positions and lies inside `[1,M_a]`.
The universal peak-mesh theorem applies even to the final such window,
which ends at `M_a`: it supplies a maximal internal peak plateau whose two
strictly smaller boundary values are also inside the window.  Hence the
supplied run is internal in the full word, not merely relative to the
window.

Suppose `W_i` contains no complete directed dangerous plateau.  The peak
supplied by the mesh theorem has one of two forms.

* If its cost is at most `ca`, it is already a cheap internal threshold
  run.
* If its cost is greater than `ca`, it cannot be directed.  Along that
  constant-coordinate plateau the two cross-coordinate values are distinct
  and complementary.  Nonmonotonicity gives an interior strict maximum or
  minimum in one cross-coordinate; a minimum becomes a maximum in the
  complementary coordinate.  This is a cost-zero singleton internal peak.

This proves Lemma 3 with all quantifiers in the required full-word sense.

The word “complete” is essential but causes no problem.  A maximal
dangerous plateau crossing the left boundary of `[i+1,i+L]` contains the
start `i`; it is not contained in the window and therefore cannot be the
maximal peak supplied inside the window.  Similarly, a plateau crossing
the right boundary is not a complete internal peak of that window.

## 4. Exact localization of starts assigned to `P_j`

### 4.1 Containment count

The plateau `P_j=[u_j,v_j]` is contained in `W_i` exactly when

\[
 i+1\le u_j,
 \qquad v_j\le i+L,
\]

or equivalently

\[
                         v_j-L\le i\le u_j-1.        \tag{4.1}
\]

Before intersecting with the global start range, this interval has

\[
 (u_j-1)-(v_j-L)+1=L-(v_j-u_j)=L-\lambda_j          \tag{4.2}
\]

integer starts.  Global boundaries and omitted shared starts can only
decrease this number.  Thus

\[
                         n_j\le L-\lambda_j          \tag{4.3}
\]

is exact in the interior and always valid.

### 4.2 Why no assigned start can precede `u_(j-1)`

Take `j>=2`, and suppose that `P_j` is complete in `W_i` and
`i<u_(j-1)`.  Since indices are integral,

\[
                         i+1\le u_{j-1}.             \tag{4.4}
\]

By word order and (2.2),

\[
 v_{j-1}\le u_j\le v_j\le i+L.                    \tag{4.5}
\]

Equations (4.4)--(4.5) show that the whole original plateau
`P_(j-1)` is also contained in `W_i`.  It occurs earlier than `P_j`, so the
first-dangerous rule cannot assign `i` to `P_j`.  Therefore every assigned
start satisfies

\[
                         u_{j-1}\le i\le u_j-1.      \tag{4.6}
\]

This argument does not assume that the two plateaux are in the same direct
rotating component.  It uses only their word order.  This is exactly why
the new assignment removes the old component count.

### 4.3 Counting the localized interval

There are two cases.

1. If the plateaux do not share an endpoint, the `g_(j-1)` gap positions
   are

   \[
      v_{j-1}+1,\ldots,u_j-1,
      \qquad g_{j-1}=u_j-v_{j-1}-1,
   \]

   and hence

   \[
    u_j-u_{j-1}
      =(v_{j-1}-u_{j-1}+1)+g_{j-1}
      =\lambda_{j-1}+1+g_{j-1}.                    \tag{4.7}
   \]

2. If the plateaux share an endpoint, then
   `u_j=v_(j-1)` and `g_(j-1)=0`.  Consequently

   \[
    u_j-u_{j-1}=v_{j-1}-u_{j-1}=\lambda_{j-1},      \tag{4.8}
   \]

   one less than the source's upper bound.

Combining (4.3), (4.6), (4.7), and (4.8) proves

\[
 n_j\le
 \min\{L-\lambda_j,\lambda_{j-1}+1+g_{j-1}\}.      \tag{4.9}
\]

The subsequent inequality

\[
 \min(A,B+C)\le B+\min(A,C)                         \tag{4.10}
\]

for nonnegative `A,B,C` is immediate: if `C<=A`, the right side is
`B+C`; if `C>A`, it is `B+A>=A`.  Taking

\[
 A=L-\lambda_j,
 \quad B=\lambda_{j-1}+1,
 \quad C=g_{j-1}
\]

gives the claimed (4.2).

### 4.4 Counterexample search

Every possible counterexample to (4.9) would need an assigned start in one
of two forbidden regions.

* A start `i<u_(j-1)` is impossible by (4.4)--(4.5), because it makes the
  predecessor complete.
* A start `i>=u_j` is impossible because `P_j` then begins at or before
  the excluded start rather than inside `[i+1,i+L]`.

Plateau overlap cannot open a third region.  A positive-length overlap
would share an ordering edge and is impossible; a one-point overlap merely
reduces the interval (4.6) by one relative to the displayed upper bound.
Global word boundaries and omitted starts only remove candidates.  Thus
there is no interval-geometric counterexample compatible with the audited
plateau axioms.

## 5. Span, congestion, and omitted indices

Every selected run `[x,y]` is contained in `[i+1,i+L]`.  Hence it avoids
the assigned index and satisfies

\[
                         y+1-i\le L+1=4a+3.         \tag{5.1}
\]

The extra one is the correct one-sided-span convention and is attained
when `y=i+L`.  All runs point to the right.  Therefore a fixed adjacent
`alpha` increment can be charged only by one of the preceding `L+1`
starts, while no `beta` increment is charged:

\[
                         C_\alpha\le L+1,
 \qquad C_\beta=0.                                  \tag{5.2}
\]

The starts `1,...,M_a-L` are the complete forward-window range, leaving
the last `L` word positions unassigned.  One may additionally omit the at
most `m-1=O(a)` shared plateau endpoints.  Section 3 informally assigns
all forward starts, whereas Theorem 1 allows these extra omissions; either
choice is safe.  If they are omitted, the base term `ca(M_a-L)` in the
cost proof merely overcounts by a nonnegative `O(a^2)` amount.

## 6. Cost ledger and cyclic secant algebra

Let `Q` be the sum of the costs of the selected runs.  A cheap assignment
costs at most `ca`, while an assignment to `P_j` costs
`lambda_j=ca+delta_j`.  Therefore

\[
 Q\le ca(M_a-L)+\sum_j\delta_jn_j.                 \tag{6.1}
\]

For `j>=2`, (4.2) gives

\[
 \delta_j n_j
 \le\delta_j\lambda_{j-1}+\delta_j
   +\delta_j\min\{g_{j-1},L-\lambda_j\}.           \tag{6.2}
\]

The first plateau contributes at most

\[
 \delta_1n_1\le\delta_1(L-\lambda_1)=O(a^2),       \tag{6.3}
\]

because `0<delta_1<=(2-c)a` and `L-lambda_1=O(a)`.
Moreover,

\[
 \sum_j\delta_j\le\sum_j\lambda_j\le M_a-1
 =O(a^2).                                           \tag{6.4}
\]

For `m>=1`, adding the nonnegative closing term
`delta_1 lambda_m` changes the predecessor products into the cyclic sum

\[
 \sum_{j=1}^m\delta_j\lambda_{j-1},
 \qquad \lambda_0:=\lambda_m.                      \tag{6.5}
\]

This remains valid for `m=1`; the closing term is then
`delta_1 lambda_1`.  The case `m=0` should simply be handled before this
notation is introduced.

For `x,y in [ca,2a]`, put

\[
                         x=ca+u,
 \qquad y=ca+v,
 \qquad 0\le u,v\le(2-c)a.
\]

The elementary inequality

\[
                         2uv\le(2-c)a(u+v)          \tag{6.6}
\]

is equivalent, after expansion, to

\[
 xy\le\left(1+{c\over2}\right)a(x+y)-2ca^2.        \tag{6.7}
\]

Apply this to `(lambda_(j-1),lambda_j)` and sum cyclically.  Every
`lambda_j` occurs twice in the linear part, including with multiplicity
two in the one-plateau case.  Hence

\[
 \sum_j\lambda_{j-1}\lambda_j
 \le(2+c)a\sum_j\lambda_j-2ca^2m.                  \tag{6.8}
\]

Now subtract

\[
 ca\sum_j\lambda_{j-1}=ca\sum_j\lambda_j
\]

to obtain

\[
 \begin{aligned}
 \sum_j\delta_j\lambda_{j-1}
 &=\sum_j(\lambda_j-ca)\lambda_{j-1}\\
 &\le2a\sum_j\lambda_j-2ca^2m\\
 &=2a\sum_j(\lambda_j-ca)\\
 &=2a\sum_j\delta_j.
 \end{aligned}                                      \tag{6.9}
\]

This is the claimed exact simplification.  Combining (6.1)--(6.4) and
(6.9), and absorbing `caL=O(a^2)`, proves (1.1).  Since

\[
 M_a=3a^2+3a+1,
 \qquad {caM_a\over a^3}=3c+O(a^{-1}),
\]

division by `a^3` gives (1.2).

## 7. Seam bounds

### 7.1 Excess-mass bound

The source uses

\[
 \min\{g_{j-1},L-\lambda_j\}\le L=4a+2,
\]

so

\[
 H_c\le(4+2/a)e_c=(4+o(1))e_c.                     \tag{7.1}
\]

This is valid.  Because `lambda_j=ca+delta_j`, one can retain the
available subtraction:

\[
 L-\lambda_j=(4-c)a+2-\delta_j.                    \tag{7.2}
\]

Therefore

\[
 \begin{aligned}
 H_c
 &\le {1\over a^3}\sum_j
       \delta_j(L-\lambda_j)\\
 &=\left(4-c+{2\over a}\right)e_c
   -{1\over a^3}\sum_j\delta_j^2,
 \end{aligned}                                      \tag{7.3}
\]

which proves the strengthening (1.3).

### 7.2 Gap-mass bound

Every dangerous plateau has at most `2a+1` vertices, hence

\[
                         0<\delta_j\le(2-c)a.       \tag{7.4}
\]

The intervals of gap positions between consecutive dangerous plateaux are
pairwise disjoint.  The prefix and suffix gaps are not used by the seam
sum, so

\[
                         \sum_{j=2}^m g_{j-1}\le G. \tag{7.5}
\]

Consequently,

\[
 \sum_{j=2}^m\delta_j
      \min\{g_{j-1},L-\lambda_j\}
 \le(2-c)aG.                                       \tag{7.6}
\]

Using (2.5), `sum lambda_j=sigma*a^2`, `m=O(a)`, and
`omega=O(a)`, we get

\[
 {G\over a^2}=3-\sigma+O(a^{-1}).                  \tag{7.7}
\]

Multiplication by `(2-c)` proves

\[
                         H_c\le(2-c)(3-\sigma)+o(1).\tag{7.8}
\]

The `o(1)` absorbs the harmless possibility that `sigma` differs from its
limiting range by `O(1/a)`.

## 8. Component-free corollary

Assume `c<4/3` is fixed and `e_c=o(1)`.  Since `e_c>=0`, either (7.1) or
the stronger (7.3) gives

\[
                         H_c=o(1).                  \tag{8.1}
\]

Substitution in (1.2) yields

\[
                         Q\le3ca^3+o(a^3).          \tag{8.2}
\]

Put `epsilon=4-3c>0`.  For all sufficiently large `a`, the `o(a^3)` term
has magnitude less than `epsilon*a^3/2`, and therefore

\[
                         Q<(4-\epsilon/2)a^3<4a^3. \tag{8.3}
\]

No direct-component count occurs anywhere in this argument.

If the inherited normalized variables are

\[
                         \sigma={1\over a^2}\sum_j\lambda_j,
 \qquad s={m\over a},                               \tag{8.4}
\]

then

\[
 e_c={1\over a^2}\sum_j(\lambda_j-ca)
     =\sigma-cs.                                    \tag{8.5}
\]

Thus the stated mass-feasibility endpoint
`sigma=cs+o(1)` implies `e_c=o(1)` directly, independently of whether the
number `r` of maximal direct rotating components is `o(a)` or
`Theta(a)`.

## 9. Final theorem ledger

### Proved

* the forward first-dangerous assignment on all but `O(a)` starts;
* full-word internality of every chosen run;
* one-sided span and endpoint congestion at most `4a+3`;
* the first-contained-dangerous localization and its seam-sensitive count;
* the service inequalities (1.1)--(1.2);
* the cyclic secant reduction to `2e_c`;
* both source seam bounds, plus the stronger bound (7.3); and
* the component-free strict sub-four conclusion under the explicit
  hypothesis `e_c=o(1)` for fixed `c<4/3`.

### Not proved

* that every ordering admits a useful threshold with `e_c=o(1)`;
* a uniform strict sub-four inequality when the excess mass stays positive;
* the proposed multiscale coupling of the profiles `e_c` and `H_c`;
* the universal three-box obstruction; or
* the original Boolean-array conjecture.

The source is therefore a valid and useful strengthening of the previous
componentwise gap service.  Its remaining gap is exactly the one it states:
finding, or forcing, a threshold whose excess profile makes
`3c+2e_c+H_c<4`.
