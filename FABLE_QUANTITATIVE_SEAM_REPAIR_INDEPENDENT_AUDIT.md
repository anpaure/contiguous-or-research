# Independent audit of `FABLE_QUANTITATIVE_SEAM_TRACE_AUDIT.md`

## 1. Verdict

**PASS, with two local presentation repairs and no substantive gap.**

I reconstructed the argument without using the private Fable trace and checked
it against:

- `FABLE_RUN_SPECTRUM_AUDIT.md`;
- `FIRST_DANGEROUS_GLOBAL_SERVICE.md` and its independent audit;
- `POSITIVE_SEAM_CROSSLINE_COUPLING.md` and its independent audit; and
- the normalized plateau-measure convention

  \[
    \mu_a={1\over a}\sum_P\delta_{\lambda(P)/a},
  \]

  where the sum is over all directed internal coordinate-peak plateaux and
  `lambda(P)` is the number of word edges in the plateau.

Subject to the inherited selected-middle-order hypothesis `D=o(a^2)`, the
source really does prove that no atomic limit

\[
                 \mu_a\Longrightarrow 2\delta_x,
            \qquad {4\over3}\le x\le {3\over2},
\]

is possible.  In particular it rigorously eliminates the formerly surviving
static endpoint ledger `2 delta_(4/3)`.  This does not contradict the positive
seam/cross-line audit: that audit explicitly certified only aggregate static
data, not an ordering of the points.

The two repairs are:

1. Lemma 2's sentence about two long plateaux on the same line should use
   **plateau vertices**, not geometric edges.  Ordering edges may jump along a
   coordinate line.  Distinct same-line plateau vertex sets are disjoint, and
   each regular plateau has more than `a+1` vertices, so two cannot fit in a
   line having at most `2a+1` vertices.  The claimed capacity bound is
   unchanged.
2. In the final parameter choice it is cleanest to choose the small saving
   tolerance `epsilon` first, then choose `zeta>0` sufficiently small for the
   cost margin (and, if desired, shrink `epsilon` once more so
   `epsilon<zeta`).  Weak convergence actually makes this last inequality
   unnecessary, but stating the order prevents an apparent threshold/regular
   window ambiguity.

The first literally imprecise sentence in the source is therefore the
same-line “edge sets” sentence in Lemma 2.  It is not a mathematical gap in
the theorem because the vertex-count replacement proves exactly what is
needed.  I found no later unsupported implication and no compatible
counterexample.

## 2. Atomicity really gives the stated regular family

Fix numerical constants

\[
                1<c<x,
      \qquad 0<\varepsilon<x-1,
\]

and call a plateau regular when

\[
       (x-\varepsilon)a\le\lambda(P)
                  \le(x+\varepsilon)a.
\]

All normalized lengths lie in the common compact interval `[0,2]`.  Since
the boundary of the regular interval carries no mass under `2 delta_x`, weak
convergence gives

\[
 \#\{P:P\text{ regular}\}=(2+o(1))a,
 \qquad
 \sum_{P\text{ regular}}\lambda(P)=(2x+o(1))a^2.
                                                               \tag{2.1}
\]

For the fixed threshold `c<x`, all but `o(a)` of these are `c`-dangerous,
and all but `o(a)` dangerous plateaux are regular.  This follows directly
from the vanishing `mu_a`-mass of the closed regions separated from `x`; it
does not require a pointwise consequence of the capped-run law.

Dangerous plateau edge intervals are pairwise disjoint.  Their vertex union
has size

\[
 \sum_P(\lambda(P)+1)-\omega,
 \qquad 0\le\omega\le m-1=O(a).
\]

The exceptional dangerous edge mass is `o(a^2)`, because there are `o(a)`
exceptions and every plateau has at most `2a` edges.  Therefore the total
number `G` of complement-gap positions is

\[
                  G=(3-2x+o(1))a^2.                 \tag{2.2}
\]

This verifies both the regular count and the gap-mass input used in Section
4 of the source.  It also shows why the old rejected inference (“almost
every window is regular”) is absent here: the proof uses only (2.1)--(2.2).

## 3. Seam-local maximum lemma, including every endpoint

Let the consecutive regular dangerous plateaux be

\[
 P=[u_-,v],\qquad P'=[u,v'],\qquad v\le u,
\]

and let `d` be the strictly rising cross-coordinate on `P`.  Put

\[
 h=T_v(d),\qquad M=\max_{v\le s\le u}T_s(d).
\]

Because `d` is integer-valued and strictly increases on each of the
`lambda(P)` word edges,

\[
 h-T_{u_-}(d)\ge\lambda(P),
 \qquad h\ge\lambda(P)-a.                           \tag{3.1}
\]

Also `T_(v-1)(d)<h<=M`.  Hence a maximal component of
`{s:T_s(d)>=M}` meeting a maximum in `[v,u]` cannot extend left of `v`.

- If `T_u(d)<M`, select a top component ending before `u`; it is contained
  in `[v,u-1]`.
- If `T_u(d)=M` and `d` falls on `P'`, then `T_(u+1)(d)<M`, so the component
  containing `u` is contained in `[v,u]`.
- If `T_u(d)=M` and `d` is fixed on `P'`, then `P'` absorbs the cross at
  fixed level `M`.
- If `T_u(d)=M` and `d` rises on `P'`, then

  \[
  T_{v'}(d)\ge M+\lambda(P')
   \ge(2x-1-2\varepsilon)a>a,
  \]

  because `epsilon<x-1`; this is impossible.

Both plateaux are internal and nontrivial, so `v-1` and `u+1` exist.  In
the two cheap cases the selected full-word threshold component `R` is
therefore internal and

\[
                  R\subseteq[v,u],
      \qquad \lambda(R)\le u-v.                     \tag{3.2}
\]

For a nonoverlapping seam, with

\[
                  g=u-v-1,
\]

this is `lambda(R)<=g+1`.  At a shared endpoint `u=v`, the falling case
gives the singleton component `{v}` of cost zero.  Thus the source has the
right off-by-one in every case.

There is no partial-successor escape: in a cheap case a strict value below
the threshold occurs by `u+1`; continuing through `P'` is exactly the fixed
absorption case.  Multiple maxima in the gap also cause no problem because
one chooses a full component at the maximum threshold rather than assuming
that the maximum is unique.

## 4. Absorption capacity and long gaps

In an absorbing seam the successor is a regular plateau whose fixed
coordinate is `d` at the positive level `M`.  Equations (3.1) and regularity
give

\[
         M\ge(x-1-\varepsilon)a.                    \tag{4.1}
\]

A coordinate line at positive level `t` contains `2a-t+1` points, so a
regular successor on it requires

\[
       \lambda(P')+1\le2a-t+1,
       \qquad t\le(2-x+\varepsilon)a.               \tag{4.2}
\]

There are consequently at most

\[
       3(3-2x+2\varepsilon)a+O(1)                   \tag{4.3}
\]

possible absorbing successor lines across the three coordinate directions.
No such line can be used by two regular successors: distinct maximal
same-coordinate plateaux have disjoint vertex sets, whereas two plateaux of
more than `a` edges would require more than the at-most-`2a+1` available
vertices.  This supplies the corrected proof of the high-line capacity.

The complement gaps are disjoint.  By (2.2), the number with `g>a` is at
most

\[
                     (3-2x+o(1))a.                  \tag{4.4}
\]

There are `(2+o(1))a` dangerous plateaux, and every exceptional plateau can
destroy at most its two adjacent regular-to-regular seams.  Removing the
absorbing seams (4.3), the long-gap seams (4.4), the `o(a)` exceptional
seams, and the two word ends leaves at least

\[
       (8x-10-6\varepsilon-o(1))a                   \tag{4.5}
\]

regular, nonabsorbing seams with `g<=a`.  Recomputing the coefficient gives

\[
  2-3(3-2x+2\varepsilon)-(3-2x)
       =8x-10-6\varepsilon,
\]

so no seam or endpoint was lost twice in a way that invalidates the lower
bound; this is simply a union bound.

## 5. Exact first-dangerous service interval

For one of the seams in (4.5), write

\[
 P_{j-1}=[u_-,v],\qquad P_j=[u,v_j]
\]

and define

\[
 I_j=[\max\{u_-,v_j-L\},v-1]\cap[1,M_a-L],
 \qquad L=4a+2.                                    \tag{5.1}
\]

### 5.1 First-dangerous identity

The complete-containment condition for `P_j` in
`W_i=[i+1,i+L]` is exactly

\[
                      v_j-L\le i\le u-1.            \tag{5.2}
\]

For `i>=u_-`, the predecessor `P_(j-1)` is not complete because its first
vertex lies at or before the excluded start `i`.  Every still earlier
dangerous plateau also begins before the window.  Since `P_(j-1),P_j` are
consecutive in the full dangerous list, (5.1)--(5.2) imply that the original
first-dangerous assignment selects **exactly `P_j`** at every `i in I_j`.

### 5.2 Window containment and avoidance

The seam-local run has `R=[p,q] subseteq[v,u]`.  For every `i in I_j`,

\[
             i\le v-1<p,
 \qquad i+L\ge v_j\ge u\ge q.
\]

Hence `R subseteq W_i`, and `R` avoids its assigned index.  This proves the
full condition needed by the heterogeneous run lemma, not merely proximity
of the run to the seam.

### 5.3 Disjointness

Before global truncation,

\[
             I_j\subseteq[u_-,v-1].                 \tag{5.3}
\]

The intervals on the right are precisely the word-edge initial positions
of distinct predecessor plateaux.  Dangerous plateau word-edge sets are
pairwise disjoint, even across coordinate directions.  Therefore the
`I_j` are pairwise disjoint.  This is the key fact that prevents any saving
from being counted twice.

### 5.4 Exact cardinality and boundaries

For a nonoverlapping seam `u=v+g+1`, the untruncated interval has

\[
 |I_j|=
 \min\{\lambda_{j-1},L-\lambda_j-g-1\}.             \tag{5.4}
\]

At a shared endpoint the second term becomes `L-lambda_j`, one larger, so
the displayed lower bound remains safe.  When `g<=a`, regularity and
`x<=3/2` give

\[
 \begin{aligned}
 L-\lambda_j-g-1
  &\ge(3-x-\varepsilon)a+1\\
  &\ge(x-\varepsilon)a+1,
 \end{aligned}
\]

and therefore

\[
                   |I_j|\ge(x-\varepsilon)a-O(1).  \tag{5.5}
\]

There is no left-boundary loss because `u_->=1`.  Intersecting all of the
already disjoint intervals with `i<=M_a-L` deletes at most the final `L`
word positions **in total**, not per seam.  Thus boundary truncation loses
only `O(a)` reassigned starts and only `O(a^2)` cost saving.

## 6. Reuse, span, and congestion

Reassign each `i in I_j` from `P_j` to its seam-local run `R`.  Section 5
shows

\[
                         R\subseteq[i+1,i+L].        \tag{6.1}
\]

Thus every modified assignment points right and has one-sided span at most
`L+1=4a+3` in the audited convention.  A fixed adjacent `alpha` increment
can be crossed only by one of the preceding `L+1` starts, while no `beta`
increment is charged.  Hence

\[
                       C_\alpha\le L+1,
 \qquad C_\beta=0.                                  \tag{6.2}
\]

It is irrelevant that one threshold component can be reused by many starts:
those starts are distinct word indices and (6.1) itself bounds their number
at every charged endpoint by `L+1`.  The run-spectrum theorem has no
seam-to-run multiplicity hypothesis.  Pairwise disjointness of the `I_j`
is needed for the cost subtraction, and was proved separately in Section
5.3.

The modified assignment still omits only the final `L=O(a)` starts.  Every
chosen run has cost at most `2a`: dangerous plateaux have cost at most `2a`,
cheap first-dangerous runs cost at most `ca<2a`, and seam-local runs have
cost at most `a+1`.  Thus cap `h=3a-1` does not truncate any chosen cost for
large `a`.

## 7. First-dangerous upper cost and the cubic saving

Take

\[
                       c=x-\zeta,
 \qquad 0<\zeta<x-1.
\]

Weak convergence gives

\[
 e_c={1\over a^2}\sum_P(\lambda(P)-ca)_+
                    \longrightarrow2\zeta.          \tag{7.1}
\]

The independently audited first-dangerous theorem gives an actual
assignment whose cost satisfies

\[
 {Q_{\rm fd}\over a^3}
 \le3c+2e_c+H_c+o(1),
 \qquad H_c\le(4-c+o(1))e_c.                        \tag{7.2}
\]

Substituting (7.1) and `c=x-zeta` yields

\[
 {Q_{\rm fd}\over a^3}
 \le3x+(9-2x)\zeta+2\zeta^2+o(1).                  \tag{7.3}
\]

For every serviced start, (3.2) and `g<=a` give

\[
 \lambda(P_j)-\lambda(R)
 \ge(x-1-\varepsilon)a-O(1).                        \tag{7.4}
\]

Multiplying the number of seams (4.5), the disjoint service count (5.5),
and the per-start saving (7.4), and subtracting the `O(a^2)` global boundary
loss, gives

\[
 S\ge\left((8x-10-6\varepsilon)(x-\varepsilon)
                 (x-1-\varepsilon)-o(1)\right)a^3. \tag{7.5}
\]

Because all reassigned starts are distinct and each previously paid exactly
`lambda(P_j)`, the modified cost satisfies the exact identity

\[
                         Q_{\rm mod}=Q_{\rm fd}-S.   \tag{7.6}
\]

## 8. Comparison with the capped-run lower bound

For an assignment on all but `O(a)` indices, with span `O(a)`, the audited
subset run-spectrum inequality at `h=3a-1` says

\[
 \sum_{i\in J}\min\{\lambda_i,3a-1\}
 \ge V_a-O(a^2)-O(a)D
 =(4-o(1))a^3,                                      \tag{8.1}
\]

because `D=o(a^2)`.  By Section 6 the minimum signs may be removed for the
modified assignment.

At `epsilon=0`, write

\[
 S_0(x)=(8x-10)x(x-1).
\]

The exact margin over the amount needed to lower `3x` below four is

\[
 \begin{aligned}
 S_0(x)-(3x-4)
 &=8x^3-18x^2+7x+4.                                \tag{8.2}
 \end{aligned}
\]

Its derivative is

\[
                    24x^2-36x+7>0
 \quad(4/3\le x\le3/2),
\]

so the minimum occurs at `x=4/3` and equals

\[
                              {8\over27}.           \tag{8.3}
\]

Choose `epsilon>0` small enough that (7.5)'s coefficient retains a fixed
positive margin over `3x-4`, then choose `zeta>0` so small that the extra
term in (7.3) is less than half that margin.  Equations (7.3)--(7.6) give

\[
                         Q_{\rm mod}\le(4-\eta)a^3
\]

for a fixed `eta>0`, contradicting (8.1).  All limits are taken with
`x,epsilon,zeta` fixed numerically before `a` tends to infinity; no
nonuniform threshold is used.

## 9. Counterexample stress tests

I specifically tried the following ways to break the construction.

1. **A maximum attained at several gap positions.**  Selecting one maximal
   top-threshold component still keeps it between the strict left value and
   the strict right value; uniqueness is unnecessary.
2. **A partial successor extending the run.**  It extends only in the fixed
   absorbing case.  Falling supplies the right strict boundary immediately,
   while rising violates the coordinate cap.
3. **Shared plateau endpoints.**  The cheap run becomes a singleton in the
   only cheap shared-endpoint case; the service interval actually gains one
   available start relative to the conservative formula.
4. **A predecessor or earlier dangerous plateau also complete in the
   service window.**  Every service start is at or after the predecessor's
   first vertex, so the forward window omits that vertex.  Earlier plateaux
   begin even farther left.
5. **Overlap of service starts.**  Each service interval lies in the word
   edge interior of a different predecessor plateau, and dangerous plateau
   edge intervals are disjoint.
6. **Many seams reuse one run.**  Span, rather than run identity, controls
   endpoint congestion; every charged start still lies in one interval of
   only `L+1` possible positions.
7. **All safe service lies at the final boundary.**  The disjoint intervals
   can lose only the `L` physical starts beyond `M_a-L` in total.
8. **Long gaps consume all nonabsorbing seams.**  Their disjoint total mass
   is (2.2), which gives exactly the subtraction in (4.4)--(4.5).
9. **Abstract capped spectra with many cheap indices.**  They do not refute
   this theorem.  Unlike the rejected proof, the new proof explicitly
   constructs a positive-density family of cheap assigned indices from the
   atomic seam geometry and then contradicts only the global capped sum.

None of these produces a counterexample compatible with the audited
definitions.

## 10. Exact theorem ledger

### Certified by this audit

1. The seam-local maximum/absorption alternative.
2. The corrected high-line capacity bound.
3. A positive-density family of regular, nonabsorbing, gap-at-most-`a`
   seams under an atom `2 delta_x`, `4/3<=x<=3/2`.
4. Pairwise disjoint exact first-dangerous service intervals of
   `Theta(a)` starts per such seam.
5. A modified span-`4a+3` assignment with the cubic saving (7.5).
6. Exclusion of every atomic profile in the displayed interval when
   `D=o(a^2)`.

### Not certified or claimed

1. Any analogous exclusion for a non-atomic or mixed limiting profile.
2. A theorem reducing every survivor to one of the excluded atoms.
3. A universal strict-sub-four run assignment for an arbitrary middle
   order.
4. The full three-box obstruction or the original Boolean-array conjecture.

The repair therefore advances the ordering obstruction genuinely, but its
scope remains exactly atomic.
