# Adversarial cross-audit of the mesoscopic-capacity report (lane P)

Audited source: MATH_ATTACK_P_MESOSCOPIC_CAPACITY_REPORT_RAW_20260724.md.

## Verdict

The main quantitative calculus survives audit:

- the successor and centered-colour identities are exact;
- the directed and undirected locality constants are exactly \(2q\);
- the common-path refinement and the profile-\(3\) values \(8\) and
  \(4q+6\) are correct as coupling/removal masses;
- the fixed-\(A\) capacity-envelope asymptotic, including its error term and
  constants \(\kappa_A,J_A,F_A\), is correct;
- the owner-volume and seam-count ceilings are correct necessary
  inequalities;
- the two-wreath cross-matching, no-three-consecutive,
  \(2\lfloor n/3\rfloor\), and \(4\lfloor n/3\rfloor\) constants are
  correct;
- the reversal formulas and the frozen-data Hall-slack constant
  \(r_{q-1}+r_q\) are correct.

Several statements require material qualification.

1. Pointed locality requires the chosen successor orientations to agree
   outside the declared support. Undirected agreement alone is
   insufficient.
2. Every exact-factor depth histogram has exact point margins. In
   particular, the depth-\(m-1\) histogram is factor-independent, so its
   distance is zero. This invariant is omitted from the report.
3. The capacity curve is a sharp asymptotic evaluation of a universal upper
   envelope, not an attained or sign-correcting packet capacity.
4. Seam counts are potential transport, not counts of productive edges
   after histogram cancellation.
5. The asserted \(\Theta(m)\) rewiring per \(O(1)\)-wreath packet is an
   average conclusion for a specified owner-disjoint positive-density
   architecture, not a statement about every packet.
6. Undirected productive seams are necessary for unlabelled
   histogram/overload motion, but not for labelled synchronization.
   Reversal itself demonstrates the distinction.
7. Every lower bound concerns movement between specified states. It does
   not obstruct choosing a good exact factor ab initio, and it does not
   constrain a direct literal-OR-word construction.

Thus the honest result is a rigorous transition-capacity ceiling. It proves
neither MWB nor labelled synchronization and supplies no counterexample to
either.

## 1. Exact successor and centered-colour calculus

Put

\[
n=2m+1,\qquad W=\binom{n}{m},\qquad B=\frac Wn,
\qquad N_q=\binom{n}{m-q},\qquad
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor.
\]

For an oriented wreath \(\pi\), write

\[
X_s=I_\pi(s,m),\qquad \sigma X_s=X_{s+m}.
\]

Since \(2m\equiv-1\pmod n\),

\[
\sigma^{2j}X_s=X_{s-j}.
\]

Consequently, for every \(0\le q\le m\),

\[
\bigcap_{j=0}^{q}\sigma^{2j}X_s
=\bigcap_{j=0}^{q}I_\pi(s-j,m)
=I_\pi(s,m-q)
=L_q(X_s).
\]

Formula (1) of the report is therefore correct, including its direction
and endpoints. Although only the \(q+1\) parity-class vertices occur in the
intersection, determining them from \(X_s\) uses the directed successor
segment

\[
X_s,\sigma X_s,\ldots,\sigma^{2q}X_s,
\]

which has exactly \(2q\) directed arcs.

For the centered colour,

\[
\begin{aligned}
C_q(X_s)
&=\bigcap_{j=0}^{q}\sigma^{-q+2j}X_s\\
&=I_\pi(s-qm,m-q).
\end{aligned}
\]

Reversing the orientation negates the symmetric exponent set
\(\{-q,-q+2,\ldots,q\}\), so the intersection is unchanged. Moreover,
\(s\mapsto s-qm\) permutes \(\mathbb Z_n\). Hence the multiset of the
\(C_q(X_s)\) is exactly the usual unpointed depth-\(q\) cyclic-interval
histogram. The centered-colour formula and its orientation-independence are
correct.

### Correct support hypotheses

Let \(F_0,F_1\) be exact factors and let \(U\) contain every owner on which
their undirected cycle decompositions differ. Let \(L=|U|\). For the
unlabelled theorem, undirected agreement outside \(U\) is enough.

For the pointed theorem, one must additionally require that the chosen
successor arcs agree outside \(U\), or enlarge \(U\) to contain every
wreath whose orientation changes. The phrase “orient their affected
wreaths compatibly” does not by itself ensure this. Reversing an
unaffected wreath changes all its nontrivial pointed flags while leaving
the undirected factor unchanged.

With this correction, define

\[
t_{\rm und}=|E(F_0)\setminus E(F_1)|,\qquad
t_{\rm dir}=|\vec E(F_0)\setminus\vec E(F_1)|
\]

on the declared support. Then, for \(1\le q\le m-1\),

\[
D_q^{\rm hist}\le\min(L,2q\,t_{\rm und}),\qquad
D_q^{\rm point}\le\min(L,2q\,t_{\rm dir}).
\]

The constants \(2q\) are exact ledger constants. An old undirected edge
belongs to exactly \(2q\) centered segments of length \(2q\), because
\(2q<n\). An old directed arc similarly belongs to exactly \(2q\) directed
histories. Any center whose old segment contains no old-only edge has the
same colour in the new factor. This proves (2).

These remain upper bounds: meeting a changed seam does not force the final
set-valued colour to change. In a common fixed-owner coupling one also has

\[
D_q^{\rm hist}\le D_q^{\rm point},
\]

because half total variation is at most the number of mismatched coupled
occurrences. There is no converse bound.

## 2. Omitted exact point-margin invariant

For every exact factor, every \(q\), and every coordinate \(x\in[n]\),

\[
\boxed{\sum_{S\ni x}\mu_q(S)=(m-q)B.}
\]

Indeed, in each of the \(B\) wreaths, a coordinate occurs in exactly
\(m-q\) of the \(n\) cyclic intervals of length \(m-q\).

Therefore every exact-factor histogram difference has both zero total mass
and zero point margins. Two consequences matter here.

First, at \(q=m-1\),

\[
\mu_{m-1}(\{x\})=B\qquad(x\in[n]),
\]

so

\[
\boxed{D_{m-1}^{\rm hist}(F_0,F_1)=0}
\]

for every pair of exact factors. The report correctly says that both
distances vanish at \(q=0,m\), but the histogram has this additional exact
vanishing depth. Pointed distance need not vanish there.

Second, a packet cannot repair an arbitrary signed histogram defect. Any
attainable exact-factor difference lies in the affine slice with zero total
and zero coordinate margins. The opening phrase “arbitrary linear
first-shadow defects” must mean a defect already compatible with these
exact invariants, or be replaced by the conditional phrase “any packet
architecture that actually achieves a linear first-shadow improvement.”

## 3. Common-path refinement and profile-\(3\) constants

Delete the old-only edges from the affected old cycles. Omit any completely
untouched common cycle from the resulting list, and let the remaining
common path components have vertex-orders \(\ell_i\).

On a path of order \(\ell\), precisely

\[
\max(\ell-2q,0)
\]

centers have their entire length-\(2q\) segment inside the common path.
Thus the exact number of centers not certified by the common path is

\[
\ell-\max(\ell-2q,0)=\min(\ell,2q),
\]

and

\[
D_q^{\rm hist}\le\sum_i\min(\ell_i,2q).
\]

Formula (3) is correct with the untouched-cycle convention just stated.
Its right side is an exact seam-crossing coupling mass, but only an upper
bound on half-\(\ell^1\) histogram distance; changed occurrences can cancel
in the same histogram cells.

For a profile-\(3\) alternating \(C_8\), the four common path orders are

\[
3,\ n-3,\ 3,\ n-3.
\]

Hence

\[
r_1=4\min(3,2)=8
\]

and, for \(2\le q\le m-1\),

\[
r_q=2\cdot3+2\cdot2q=4q+6.
\]

These constants are correct as removal/addition or coupling masses. They
are not exact histogram distances or exact counts of nonzero cells. At
\(q=m-1\), the potential mass is \(4m+2=2n\), while the exact point-margin
invariant forces the actual histogram distance to be zero.

The pointed bounds quoted later in the report are also valid upper bounds,
not equalities. With orientations chosen to preserve the two long inherited
paths, the common directed-path orders are

\[
n-3,\ n-3,\ 3,\ 1,\ 1,\ 1.
\]

Their seam-crossing counts give \(9\) at \(q=1\) and \(4q+6\) for
\(2\le q\le m-1\).

## 4. Histogram versus pointed objectives

The overload identity

\[
O_q(F)=\min_{b\in\mathcal B_q}
\frac12\|\mu_q(F)-b\|_1,
\]

where \(\mathcal B_q\) is the factor-independent set of balanced quota
vectors of total mass \(W\), makes \(O_q\) a distance to a fixed set.
Therefore

\[
|O_q(F_1)-O_q(F_0)|\le D_q^{\rm hist}.
\]

Formula (4) is correct.

For a fixed integral balanced nested resolution \(P\), the mismatch
indicator satisfies, owner by owner,

\[
\left|
\mathbf 1_{\{L_q^{F_1}(X)\ne P_q(X)\}}
-\mathbf 1_{\{L_q^{F_0}(X)\ne P_q(X)\}}
\right|
\le
\mathbf 1_{\{L_q^{F_1}(X)\ne L_q^{F_0}(X)\}}.
\]

Summation, followed by the standard two-minimizer argument over the same
factor-independent family \(\mathscr R\), gives

\[
|\mathcal J_A(F_1)-\mathcal J_A(F_0)|
\le
\sum_{q\le K_A}\frac{D_q^{\rm point}}{c_q}.
\]

Formula (5) is correct after imposing pointed agreement outside \(U\). It
controls the change in the optimized objective value. It does not control
the distance between optimizing resolutions: a small input edit may still
cause linear argmin recourse.

The two resources must not be conflated:

\[
\begin{array}{c}
t_{\rm und}\longrightarrow D_q^{\rm hist}
\longrightarrow |\Delta O_q|,\\[2mm]
t_{\rm dir}\longrightarrow D_q^{\rm point}
\longrightarrow |\Delta\mathcal J_A|.
\end{array}
\]

Neither line reverses, and the first resource does not control the second.

## 5. Fixed-window capacity envelope

Let \(K_A=\lceil A\sqrt m\rceil\) with fixed \(A>0\). Exactly,

\[
\frac W{N_q}
=\frac{(m-q)!(m+q+1)!}{m!(m+1)!}
=\prod_{j=0}^{q-1}\frac{m+j+2}{m-j}.
\]

For \(q\le K_A\), Taylor expansion with its second-order cancellation gives

\[
\begin{aligned}
\log\frac W{N_q}
&=\sum_{j=0}^{q-1}
\left(
\frac{2j+2}{m}-\frac{2j+2}{m^2}
+O_A\!\left(\frac{(j+1)^3}{m^3}\right)
\right)\\
&=\frac{q(q+1)}m+O_A(m^{-1})\\
&=\frac{q^2}{m}+O_A(m^{-1/2}).
\end{aligned}
\]

Thus the stronger first equality in line 181 of the source report is
valid; the apparently larger cubic Taylor error cancels at second order.

Put

\[
d(x)=\lfloor e^{x^2}\rfloor.
\]

If \(c_q\ne d(q/\sqrt m)\), then \(e^{q^2/m}\) is within
\(O_A(m^{-1/2})\) of one of only \(O_A(1)\) integer thresholds. Every
threshold \(k\ge2\) localizes \(q\) to \(O_A(1)\) lattice positions around
\(\sqrt{m\log k}\); the threshold \(1\) creates no discrepancy. Hence

\[
\#\{q\le K_A:c_q\ne d(q/\sqrt m)\}=O_A(1).
\]

For \(L\ge0,t>0\), let

\[
\lambda=\frac{L}{2t\sqrt m},\qquad
F_A(\lambda)=\int_0^A\frac{\min(\lambda,x)}{d(x)}\,dx.
\]

The functions

\[
g_\lambda(x)=\frac{\min(\lambda,x)}{d(x)}
\]

have, uniformly in \(\lambda\),

\[
\|g_\lambda\|_\infty+
\operatorname{Var}_{[0,A+1]}g_\lambda
=O_A(\min(\lambda,1)).
\]

The bounded-variation Riemann estimate, together with the \(O_A(1)\)
exceptional floor indices, yields uniformly for arbitrary \(m\)-dependent
\(L,t\),

\[
\boxed{
C_A(L,t)
=\sum_{q\le K_A}\frac{\min(L,2qt)}{c_q}
=2tmF_A(\lambda)
+O_A(\min\{L,t\sqrt m\}).
}
\]

Define \(C_A(L,0)=0\). Formula (6) is correct. Similarly,

\[
\sum_{q\le K_A}\frac1{c_q}
=\kappa_A\sqrt m+O_A(1),\qquad
\sum_{q\le K_A}\frac q{c_q}
=J_A m+O_A(\sqrt m),
\]

so (7) is correct. All quantifiers are fixed-\(A\), \(m\to\infty\);
none of these estimates is uniform for an unspecified growing \(A(m)\).

The report should define its previously undefined notation

\[
\Phi_A(F)=\sum_{q\le K_A}\frac{O_q(F)}{c_q}.
\]

With that definition, its two consequences follow from (2), (4), and (5).

### What “sharp capacity” means

The formula is sharp for the numerical envelope
\(\sum_q\min(L,2qt)/c_q\). It does not prove the existence of a packet that
attains this envelope, has the desired signs, avoids cancellations, or
works simultaneously at all depths. “Sharp fixed-window capacity curve”
should therefore be read as “sharp asymptotic evaluation of the universal
fixed-window capacity envelope.”

## 6. Aggregation, owner volume, and seam ceilings

For packet parameters \((L_i,t_i)\), write

\[
V=\sum_iL_i,\qquad T=\sum_it_i.
\]

Algebraically,

\[
\sum_i\min(L_i,2qt_i)\le\min(V,2qT).
\]

Disjointness is not needed for this numerical inequality. It is needed if
\(V\) is to mean the number of distinct owners touched rather than exposure
volume counted with multiplicity. For sequential overlapping packets, the
same bound is a triangle-inequality ledger with \(V,T\) counted over uses.

If a collection actually achieves metric movement, or decreases a
one-Lipschitz objective, by at least \(D_q\) at rank \(q\), then necessarily

\[
\boxed{V\ge D_q,\qquad T\ge\frac{D_q}{2q}.}
\]

Formula (8) is correct in this conditional sense. It is not a sufficiency
statement and does not say that all defects of size \(D_q\) are reachable.
For the histogram version \(T\) is an undirected seam count; for the
pointed version it is a directed seam count.

Suppose \(p\) equal owner-disjoint packets have owner volume \(L\) and
occupy density

\[
\rho=\frac{pL}{W}.
\]

A depth-\(q\) improvement of at least \(\delta W\) forces

\[
\frac Tp\ge\frac{\delta L}{2q\rho}.
\]

At \(q=1\), constant \(\delta,\rho>0\), and \(L=\Theta(m)\), this is
\(\Omega(m)\), hence \(\Theta(m)\) because an \(O(1)\)-wreath packet has
only \(O(m)\) old edges. This is an average statement. It neither forces
every packet to be mesoscopic nor certifies that every counted seam has a
productive sign. At \(q\sim x\sqrt m\), with fixed \(x>0\), the
corresponding average lower bound is \(\Omega(\sqrt m)\).

If the same packet collection achieves \(D_q\ge\delta W\) for every
\(q\le K_A\), then, writing

\[
S_0=\sum_{q\le K_A}\frac1{c_q},\qquad
S_1=\sum_{q\le K_A}\frac q{c_q},
\]

one has

\[
\delta WS_0\le2TS_1.
\]

Since \(B=W/n\), this gives the report's constant

\[
\frac TB
\ge
\left(\frac{\delta\kappa_A}{J_A}+o(1)\right)\sqrt m.
\]

The bound is correct but non-sharp under the stated hypothesis: because
the hypothesis includes \(q=1\), formula (8) already gives

\[
\boxed{\frac TB\ge\frac{\delta n}{2}
=\delta m+\frac\delta2.}
\]

The \(\sqrt m\) estimate becomes informative for an aggregate weighted
defect hypothesis or a Gaussian annulus that excludes fixed shallow ranks.

## 7. Profile-\(3\) aggregate ledger

For \(m\ge3\), \(c_1=1\). The exact histogram envelope for one audited
profile-\(3\) switch is

\[
\begin{aligned}
\frac8{c_1}+\sum_{q=2}^{K_A}\frac{4q+6}{c_q}
&=4S_1+6S_0-\frac2{c_1}\\
&=4J_A m+O_A(\sqrt m).
\end{aligned}
\]

The pointed envelope, using \(9\) at depth one, differs only by one. Thus
the leading constant in line 259 is correct.

There are three interpretation caveats.

1. This is a formal summed removal/addition budget, not proved productive
   objective movement. Histogram cancellation can make the actual change
   much smaller, even zero at \(q=m-1\).
2. A switch uses two old wreaths. An owner-disjoint family therefore has at
   most \(B/2\) such packets. “\(B\) such switches” is legitimate only as a
   scale of sequential uses or as a formal budget, not as an asserted
   owner-disjoint reservoir.
3. At one Gaussian rank the summed envelope of \(B\) uses is
   \(O_A(W/\sqrt m)\), and at depth one it is \(8B=O(W/m)\). Therefore a
   depth-one overload reduction of \(\delta W\) needs at least
   \(\delta W/8\) legal switch uses. The pointed depth-one analogue is
   \(\delta W/9\). The latter is not a lower bound for reducing the full
   multidepth objective, whose per-switch envelope is \(O_A(m)\).

The conclusion that \(o(B)\) fixed-profile \(C_8\) uses change either
fixed-\(A\) weighted objective by only \(o(W)\) is valid. Necessity of
\(\Omega(B)\) uses is not sufficiency.

## 8. Two-wreath structural ceiling

Let \(C,D\) be disjoint wreath supports, with \(m\ge3\).

### Cross edges form a matching

If \(X\in C\) had distinct odd-graph neighbours \(Y,Z\in D\), then
\(Y,Z\subset X^c\). Since all three relevant set sizes are \(m,m,m+1\),

\[
|Y\cap Z|=m-1,\qquad Y\cup Z=X^c.
\]

The two sets \(Y,Z\) are start-adjacent cyclic \(m\)-intervals in the
coordinate order underlying \(D\), so

\[
[n]\setminus(Y\cup Z)=X
\]

is another \(D\)-interval, contradicting \(C\cap D=\varnothing\). Thus the
cross graph is a matching. The report should distinguish this
start-adjacency from adjacency in the old odd-graph cycle.

### No three consecutive cross-incident vertices

For two consecutive old-cycle vertices in \(D\), their cross preimages in
\(C\) intersect in at most one point. Intersection zero would give a
forbidden \(4\)-cycle in the odd graph; intersection one places the
preimages at old-cycle distance \(3\) in \(C\). Thus three consecutive
matched vertices of \(D\) would have preimages \(C_{-3},C_0,C_3\).

Writing the coordinate omitted by the cross-neighbour of \(C_0\) as \(w\),
disjointness from the two neighbouring matched vertices forces

\[
w\in C_0^c\cap C_3^c=\{z_0,z_2\}
\]

and

\[
w\in C_0^c\cap C_{-3}^c=\{z_{-3},z_{-1}\}.
\]

These pairs are disjoint for \(m\ge3\), a contradiction. Hence the
cross-incident vertices contain no three consecutive old-cycle vertices,
and

\[
e_{\rm cross}(C,D)\le\left\lfloor\frac{2n}{3}\right\rfloor.
\]

Formula (9) is correct.

### Replacement two-factors

Each wreath is induced and every vertex has at most one cross edge. In any
replacement two-factor on \(C\cup D\), every vertex therefore retains at
least one old edge. The removed old edges form a matching of size \(r\) in
each old cycle, while degree counting gives exactly \(2r\) selected cross
edges. Consequently

\[
t_{\rm und}=2r,\qquad
r\le\left\lfloor\frac n3\right\rfloor,\qquad
t_{\rm und}\le2\left\lfloor\frac n3\right\rfloor.
\]

All factors of two in (10) are correct.

The no-three property also implies that every common path left after
deleting old-only edges has vertex-order at least \(3\). At depth one, each
of the \(2r\) paths contributes at most \(2\), so

\[
D_1^{\rm hist}
\le4r
\le4\left\lfloor\frac n3\right\rfloor
=\left(\frac23+o(1)\right)|C\cup D|.
\]

Formula (11) is correct as an unlabelled occurrence-coupling ceiling. It is
not necessarily actual half-\(\ell^1\) transport and is not a
pointed-distance bound.

The report correctly leaves unproved the existence, for all \(m\), of a
coordinate-compatible linear cross matching that resews into the required
exact wreath cycles.

## 9. Reversal and productive-edge necessity

For one wreath, let \(X_j=I_\pi(j,m)\). The two orientations give

\[
L_q^+(X_j)=I_\pi(j,m-q),\qquad
L_q^-(X_j)=I_\pi(j+q,m-q).
\]

For \(1\le q\le m-1\), these sets differ owner by owner, but their
multisets are equal. Hence

\[
D_q^{\rm point}=n,\qquad D_q^{\rm hist}=0,\qquad
t_{\rm und}=0,\qquad t_{\rm dir}=n.
\]

The reversal formulas and constants are exact.

For a fixed resolution \(P\), partition the weighted incidences on this
wreath into those matching neither orientation (\(U_C\)), only \(+\)
(\(A_C\)), or only \(-\) (\(B_C\)). The two local costs are
\(U_C+B_C\) and \(U_C+A_C\), so the best bundled local orientation cost is

\[
U_C+\min(A_C,B_C).
\]

Formula (12) is correct locally for fixed \(P\). Contributions outside this
wreath must be added, and it is not by itself a formula for the globally
reoptimized \(\mathcal J_A\).

Two wording corrections are required.

- Reversal is an orientation-gauge change, not a nontrivial move of the
  undirected exact factor.
- One reversed wreath is dense on its \(n\)-owner support but has global
  density \(n/W=o(1)\). It should be called a support-dense pointed gauge
  packet, not a positive-density packet unless many reversals are
  explicitly bundled.

Most importantly, reversal proves that large pointed motion need not cause
any histogram motion. It does not prove that productive undirected edges
are necessary for labelled synchronization: a reversal may change labelled
mismatch and Hall data despite \(t_{\rm und}=0\). The rigorous necessity
claim is only

\[
\text{linear unlabelled histogram/overload improvement}
\Longrightarrow
\text{linear undirected seam capacity in the relevant ledger}.
\]

Even there, \(t_{\rm und}\) counts possible seam influence, not edges proved
to act with productive signs. Productive undirected transport is sufficient
only after signs, cancellations, legality, and simultaneous depth
constraints are separately controlled.

## 10. Hall-cut ceiling

Fix the quota vector, stopping-depth pattern, inclusion graph, and cut
family. If a packet transition transfers \(r_q\) frozen depth-\(q\)
occurrences, then

\[
\|g_q'-g_q\|_1\le2r_q,\qquad
|g_q'(\mathcal A)-g_q(\mathcal A)|\le r_q
\]

for every target family \(\mathcal A\). An adjacent residual Hall slack has
one term from depth \(q-1\) and one from depth \(q\), so

\[
|\Delta\operatorname{slack}_q(\mathcal A)|
\le r_{q-1}+r_q.
\]

Formula (13) is correct. If quotas vary, their transfer distance must be
added. If stopping depths vary, changed frozen-status incidences and release
sources must be charged, exactly as the report warns.

This is a cutwise Lipschitz estimate only. It supplies no favourable sign,
does not show that one packet state preserves all tight cuts
simultaneously, and gives no short-recourse theorem. Likewise, formula (5)
bounds the optimized value but not the recourse of the optimizing flow.

## 11. Correct implication scope

The proved implications are conditional transition bounds:

\[
\begin{aligned}
\text{undirected packet seams}
&\Longrightarrow
\text{an upper bound on histogram movement}
\Longrightarrow
\text{an upper bound on overload improvement},\\
\text{directed pointed seams}
&\Longrightarrow
\text{an upper bound on fixed-owner mismatch movement}
\Longrightarrow
\text{an upper bound on the optimized labelled value}.
\end{aligned}
\]

They have no proved converses. In particular:

1. A capacity ceiling supplies neither a packet construction nor an
   orientation with correct signs.
2. Owner-disjoint density conclusions do not apply unchanged to repeated,
   overlapping local trades; there \(V\) is use-volume with multiplicity.
3. Hall-value Lipschitzness does not imply Hall feasibility, simultaneous
   preservation of all cuts, or low recourse.
4. A lower bound for improving a specified bad factor does not constrain an
   existential proof that directly selects a good exact factor.
5. None of these transition bounds constrains a proof that directly builds
   a literal OR word outside the exact-factor route.
6. Unlabelled fixed-window overload is the MWB target, equivalent by the
   already-audited diagonalization over every fixed \(A\). Common-owner
   labelled synchronization is strictly stronger and only sufficient.

The opening claim of the source report should therefore be replaced by:

> If an owner-disjoint family of \(O(1)\)-wreath packets, occupying a fixed
> positive owner density, actually reduces a compatible depth-one
> histogram/overload defect by \(\delta W\), then its total undirected seam
> count is at least \(\delta W/2\); consequently its average seam count per
> packet is \(\Theta(m)\). This is a necessary potential-capacity
> condition, not an attainability, productivity, Hall-feasibility, or
> existential-MWB theorem.

## Final classification

Proved as written or after an explicit harmless hypothesis:

- formulas (1)--(8), including the exact \(2q\) constants and the fixed-\(A\)
  error term;
- the common-path refinement with untouched cycles omitted;
- the profile-\(3\) coupling constants \(8\) and \(4q+6\);
- formulas (9)--(11) for two-wreath replacements;
- the reversal identities and local fixed-\(P\) formula (12);
- the frozen-data Hall-slack formula (13).

Necessary corrections or additions:

- pointed orientation agreement outside the support;
- the exact point-margin invariant and \(D_{m-1}^{\rm hist}=0\);
- definition of \(\Phi_A\);
- “capacity envelope” in place of attained productive capacity;
- average, owner-disjoint scope for the \(\Theta(m)\)-per-packet statement;
- the stronger \(T/B\ge\delta n/2\) consequence when \(q=1\) is included;
- sequential-use qualification for “\(B\) profile-\(3\) switches”;
- separation of undirected overload transport from directed labelled
  transport;
- objective-value stability versus optimizer recourse;
- transition lower bounds versus existential factor selection.

Still unproved:

1. a positive-density legal family with mesoscopic, correctly signed
   undirected histogram transport;
2. simultaneous control of cancellations across the fixed Gaussian window;
3. one state vector preserving all residual Hall cuts with \(o(W)\) total
   labelled mismatch or recourse;
4. fixed-window overload \(o(W)\), hence MWB;
5. the stronger common-owner labelled synchronization theorem.

No audited step establishes MWB, labelled synchronization, their negations,
or a literal OR word. The mesoscopic report remains a valid and useful
capacity-ceiling theorem after the scope corrections above.
