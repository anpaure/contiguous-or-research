# First-dangerous global service across every braid seam

## 1. Outcome

Work in the middle hexagon

\[
 H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                 \ |x|,|y|,|z|\le a\},
 \qquad M_a=3a^2+3a+1,
\]

and put `L=4a+2`.  Fix `1<c<2`.  A **dangerous plateau** is a
directed internal constant-coordinate peak plateau of edge cost

\[
                         \lambda>ca.
\]

List the dangerous plateaux in word order as `P_1,...,P_m`, and write

\[
 \delta_j=\lambda_j-ca,
 \qquad e_c={1\over a^2}\sum_j\delta_j,
 \qquad s={m\over a},
 \qquad \sigma={1\over a^2}\sum_j\lambda_j.
\]

The direct-component assignment in `BRAID_GAP_SERVICE.md` pays an
`O(a^2)` interface term for every maximal rotating component.  The theorem
below removes that component count from the extremal case.

### Theorem 1 (first-dangerous global assignment)

There is a forward internal-run assignment on all but `L+O(a)` indices,
with one-sided span and endpoint congestion at most `L+1=4a+3`, such that

\[
 \boxed{
 Q\le caM_a
       +2a\sum_j\delta_j
       +\sum_{j=2}^m
          \delta_j\min\{g_{j-1},L-\lambda_j\}
       +O(a^2).}                                    \tag{1.1}
\]

Here `g_(j-1)` is the number of word positions strictly between
`P_(j-1)` and `P_j`, after using the dangerous-plateau vertex-union
convention from `BRAID_GAP_SERVICE_AUDIT.md`.  Shared plateau endpoints
are omitted and absorbed by `O(a^2)`.

In normalized form, if

\[
 H_c={1\over a^3}\sum_{j=2}^m
          \delta_j\min\{g_{j-1},L-\lambda_j\},
\]

then

\[
 \boxed{Q\le(3c+2e_c+H_c)a^3+O(a^2).}              \tag{1.2}
\]

The seam term has the two unconditional bounds

\[
 H_c\le(4-c+o(1))e_c,
 \qquad
 H_c\le(2-c)(3-\sigma)+o(1),                       \tag{1.3}
\]

where `sum lambda_j=sigma*a^2`.

### Corollary 2 (component-free endpoint closure)

If, for one fixed `c<4/3`,

\[
                         e_c=o(1),                  \tag{1.4}
\]

then `H_c=o(1)` and

\[
                         Q\le3ca^3+o(a^3)<4a^3.     \tag{1.5}
\]

No hypothesis on the number of direct rotating components is needed.
Thus the mass-feasibility endpoint `sigma=cs+o(1)` is closed even when
`r=Theta(a)`.  What remains is to prove that every putative survivor has a
threshold with small excess mass `e_c`, or to exploit the weighted seam
term in (1.1) when `e_c` is bounded away from zero.

This does not solve the universal three-box obstruction.  It removes the
transparent-separator/component-count obstruction at the exact endpoint.

## 2. The dangerous-free window lemma

We use the audited lemma from `BRAID_GAP_SERVICE.md`.

### Lemma 3

If an `L`-position window contains no complete directed peak plateau of
cost greater than `ca`, then it contains a full-word internal threshold run
of cost at most `ca`.

#### Proof

The universal peak-mesh theorem supplies an internal peak plateau contained
in the window.  If its cost is at most `ca`, use it.  Otherwise it is not
directed.  Along a nondirected constant-coordinate plateau one cross
coordinate has an interior strict extremum; this is a singleton peak in
that coordinate or in the complementary cross coordinate.  Hence a
cost-zero internal threshold run lies in the window.  \(\square\)

The word "complete" matters.  A dangerous plateau crossing the left edge
of a forward window contains the assigned start immediately before that
window and cannot itself be the internal peak supplied by the theorem.

## 3. Assignment rule

For every

\[
                         1\le i\le M_a-L,
\]

look at the forward window

\[
                         W_i=[i+1,i+L].             \tag{3.1}
\]

* If `W_i` contains one or more complete dangerous plateaux, assign `i`
  the **first** one in word order.
* If it contains none, assign the cost-at-most-`ca` run from Lemma 3.

The chosen run never contains `i`, is internal in the full word, and ends
at most at `i+L`.  In the audited convention its one-sided span is at most
`L+1`.  All assignments point right, so

\[
                         C_\alpha\le L+1,
 \qquad C_\beta=0.                                  \tag{3.2}
\]

The final `L` indices are left unassigned.  Their later fan-capped penalty
is only `O(a^2)`.

If `m=0`, every forward window uses the cheap branch and the theorem follows
immediately.  Hence the remaining sections may assume `m>=1`.

Let `n_j` be the number of starts assigned to `P_j`.  Since a forward
window contains `P_j=[u_j,v_j]` exactly when

\[
                         v_j-L\le i\le u_j-1,
\]

we always have

\[
                         n_j\le L-\lambda_j.         \tag{3.3}
\]

## 4. First-dangerous localization

For `j>=2`, a start assigned to `P_j` cannot lie strictly before the start
of `P_(j-1)`.  Indeed, if `i<u_(j-1)` and `P_j` is complete in `W_i`, then
the earlier plateau `P_(j-1)` is also complete in `W_i`, contradicting the
choice of the first dangerous plateau.

After omitting a shared endpoint, the interval from `u_(j-1)` through
`u_j-1` consists of the `lambda_(j-1)+1` vertices of `P_(j-1)` followed by
`g_(j-1)` gap positions.  Consequently

\[
 n_j\le
 \min\{L-\lambda_j,
        \lambda_{j-1}+1+g_{j-1}\}.                 \tag{4.1}
\]

For nonnegative `A,B,C`,

\[
                         \min(A,B+C)\le B+\min(A,C).
\]

Applying this to (4.1) gives

\[
 n_j\le \lambda_{j-1}+1
       +\min\{g_{j-1},L-\lambda_j\}.               \tag{4.2}
\]

The first dangerous plateau has no predecessor.  Its entire excess charge
is at most

\[
 \delta_1(L-\lambda_1)=O(a^2),                     \tag{4.3}
\]

and is absorbed into the boundary term.

## 5. The cyclic secant ledger

Every cheaply assigned index costs at most `ca`; an index assigned to
`P_j` costs `lambda_j=ca+delta_j`.  Hence

\[
 Q\le ca(M_a-L)+\sum_j\delta_j n_j.                \tag{5.1}
\]

Use (4.2), absorb `sum delta_j=O(a^2)` from the added `+1`, and add the
nonnegative closing term `delta_1 lambda_m`.  We obtain

\[
 \sum_j\delta_j n_j
 \le \sum_j\delta_j\lambda_{j-1}
   +\sum_{j=2}^m\delta_j
       \min\{g_{j-1},L-\lambda_j\}
   +O(a^2),                                        \tag{5.2}
\]

with cyclic indices in the first sum.

For `x,y in [ca,2a]`, the audited secant inequality is

\[
 xy\le\left(1+{c\over2}\right)a(x+y)-2ca^2.       \tag{5.3}
\]

Summing (5.3) cyclically gives

\[
 \sum_j\lambda_{j-1}\lambda_j
 \le(2+c)a\sum_j\lambda_j-2ca^2m.                 \tag{5.4}
\]

Subtracting `ca sum lambda_(j-1)` yields the exact simplification

\[
 \begin{aligned}
 \sum_j\delta_j\lambda_{j-1}
 &=\sum_j(\lambda_j-ca)\lambda_{j-1}\\
 &\le2a\left(\sum_j\lambda_j-cam\right)\\
 &=2a\sum_j\delta_j.                               \tag{5.5}
 \end{aligned}
\]

Equations (5.1), (5.2), and (5.5) prove (1.1)--(1.2).

## 6. Bounds on the seam term

First, put `delta_j=lambda_j-ca`.  Then

\[
 \delta_j(L-\lambda_j)
 =\delta_j\big((4-c)a+2-\delta_j\big).
\]

Therefore

\[
 H_c\le\left(4-c+{2\over a}\right)e_c
       -{1\over a^3}\sum_j\delta_j^2
 \le(4-c+o(1))e_c.                                 \tag{6.1}
\]

Second, `delta_j<=(2-c)a`, and distinct gap positions are counted at most
once.  If `G` is their total number, then

\[
 \sum_{j=2}^m\delta_j
       \min\{g_{j-1},L-\lambda_j\}
 \le(2-c)aG.                                       \tag{6.2}
\]

The dangerous-plateau vertex union has size
`sum_j(lambda_j+1)-omega`, where `0<=omega<=m-1` is the shared-endpoint
overlap.  Hence

\[
 G=M_a-\sum_j\lambda_j-m+\omega
  =(3-\sigma)a^2+O(a),                              \tag{6.3}
\]

which proves the second inequality in (1.3).

If `e_c=o(1)`, (6.1) gives `H_c=o(1)`.  Substitution into (1.2) proves
Corollary 2.

## 7. Exact remaining question

The old many-component loss was a raw `O(a^2r)` term.  The first-dangerous
assignment replaces it by the geometrically meaningful weighted seam sum

\[
 \mathcal H_c
 =\sum_{j=2}^m(\lambda_j-ca)
        \min\{g_{j-1},L-\lambda_j\}.                \tag{7.1}
\]

Transparent one-point separators now cost only
`O(a sum_j delta_j)`, rather than one full `O(a^2)` terminal penalty each.
Thus they do not obstruct the endpoint `e_c=o(1)`.

The universal three-box theorem would follow from finding a threshold
`c<4/3` for which

\[
                  3c+2e_c+H_c<4-o(1).              \tag{7.2}
\]

for every surviving order, or from a multiscale average of (7.2).  The
remaining adversarial profile must simultaneously carry positive excess
length above every useful threshold and place that excess immediately after
large gap mass.  This is narrower than the former arbitrary
`r=Theta(a)` transition problem.

## 8. Theorem ledger

Proved:

* the first-dangerous forward assignment;
* span/congestion `4a+3` with only `O(a)` omissions;
* the exact service bound (1.1);
* the cyclic secant reduction to `2e_c`;
* both seam bounds (1.3); and
* component-free sub-four service when `e_c=o(1)` and `c<4/3`.

Not proved:

* existence of such a threshold for every order;
* a uniform strict sub-four bound when `e_c` is positive;
* a multiscale inequality coupling the profiles `e_c,H_c`; or
* the three-box impossibility theorem and the Boolean-array conjecture.
