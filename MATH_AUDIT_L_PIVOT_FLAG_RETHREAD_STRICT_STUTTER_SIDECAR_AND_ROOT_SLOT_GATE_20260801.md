# Independent audit: pivot lower ray, strict-stutter sidecar, and root-slot gate

**Date:** 2026-08-01  
**Verdict:** PASS after separating three different objects: the weak
owner-changing pivot rethread, the lower-only transported matching, and the
auxiliary repeated-owner strict sidecar. The first two do not imply the
third. Physical planting of the third inside one carrier/cap remains open;
no additive-constant bound follows.

## 1. Scope and source identities

The audit compares the tight source (4.17) of
MATH_THEOREM_A_SPLIT_PIVOT_PHYSICAL_COLLAR_AND_BPLUS1_TERMINAL_PATH_20260801.md,
monotone occurrence transport from
MATH_THEOREM_R_MONOTONE_PIVOT_OCCURRENCE_COMMONQ_AND_EXPORTED_GUARD_STATE_20260801.md,
the pull-clock criterion in
MATH_THEOREM_L_LABELLED_HIGH_SEPARATOR_RIGIDITY_AND_PULL_CLOCK_RAY_GATE_20260801.md,
and the strict-gammoid deletion identity in
MATH_THEOREM_L_DUAL_GAMMOID_ROOT_SLOT_RESERVE_AND_BOUNDED_DEPTH_RECURSION_20260801.md.

All sets below are occurrence-labelled. Equal target masks at different
cells are not identified. All matching assertions use one declared cap
state, not the union of marginal cap graphs.

## 2. Saturated pivot rethread: PASS, lower-only

On the saturated face \(C=\varnothing\), \(B=X\), put

\[
 q=B+\lambda_1+\cdots+\lambda_h,
 \qquad s=q-\lambda_1+\rho_1.
\]

At the pivot, compare the newborns

\[
                    B,\qquad B-x_R+\rho_1.                    \tag{2.1}
\]

The previous \(h\) source letters contain neither \(x_R\) nor \(\rho_1\),
so (2.1) has equal intersections with every predecessor age block. The
next source letter \((B-x_L)+\rho_1\) contains both exchanged labels, so it
masks the difference. Hence the two middle states have the same neighbors
and type.

For \(1\le j\le h\), the changed lower cells are exactly

\[
\begin{aligned}
 T_j&=s-\{\rho_1,\lambda_2,\ldots,\lambda_j\},\\
 T'_j&=s-\{x_R,\lambda_2,\ldots,\lambda_j\}.
\end{aligned}                                                 \tag{2.2}
\]

Thus the occurrence identities and the common-root flag interpretation
are correct. In particular

\[
                Q^-=s-\rho_1,\qquad Q^+=s-x_R.                \tag{2.3}
\]

This is not merely rankwise Hall. Under monotone insertion, the complete
fan is disjoint from the image of every old interval cell. At a
rank-saturated cut, the only expelled width-\(h\) old cells have rank \(r\),
so a strict-lower matching uses none. If every fan target is kept on its
old provider, the transported matching avoids the whole fan, hence all
cells in (2.2), and matches \(Q^-\) externally. Since only those lower-band
addresses change between the two phases, the same matching works in both.

The hypothesis about old providers is necessary. If \(B=X\) is a fresh
required target without one, deleting the singleton fan address isolates
that obligation.

## 3. Full-transparency and root-slot claims: correctly negative

The local owner path changes from \(p-q-s\) to \(p-q'-s\), where

\[
                        q'=q-x_R+\rho_1.
\]

The exact signed collateral is

\[
 e_{q'}-e_q,\qquad
 e_{s-x_R}-e_{s-\rho_1},\qquad
 e_{q-x_R+\eta+\rho_1}-e_{q+\eta}.                            \tag{3.1}
\]

There is no earlier reset containing both exchanged labels in the native
pivot collar, so intervals ending at the pivot may continue changing above
the lower band. Therefore the rethread is neither owner-transparent nor
upper-/arbitrary-width-transparent.

On the same-type rank-\((r-1)\) slice, the longest physical cell has only
the two coatom values in (2.3). It cannot realize, for example,
\(s-\lambda_2\), because that interval forces \(\lambda_2\). Hence it is a
two-flag column, not the universal Boolean root slot required by Definition
3.1 of the strict-gammoid reserve note. The ordered endpoint mismatch is
also literal: the owner portal deletes \(x_R\), whereas the old \(q\)-flag
begins by deleting \(\lambda_1\).

The complete refresh audit of the native \(4h+1\)-letter tight source also
passes. For every center with full predecessor history and successor
inside the block, the pull-clock set

\[
 S_t=\left(a_{t-h}\setminus
            \bigcup_{u=t-h+1}^{t-1}a_u\right)\cap a_{t+1}
\]

is empty except at the \(A^-\) and \(P^+\) centers, where it is respectively
\(X-x_R\subseteq A^-\) and \(C\cup X_R\subseteq P^+\). A nontrivial fixed-
owner fibre needs a proper nonempty selected subset of \(S_t\). None exists.
This audit does not cover boundary centers whose history or successor lies
in the exterior word.

## 4. Explicit repeated-owner sidecar: PASS

Let \(K=B-x_R\). Use the \(h+2\) source positions

\[
 \{x_R,\rho_1\},\quad
 \{\lambda_2\},\ldots,\{\lambda_h\},\quad
 K+x_R\ \longleftrightarrow\ K+\rho_1,\quad
 \{x_R,\rho_1\}.                                             \tag{4.1}
\]

In the predecessor state, the last active cell is
\(\{x_R,\rho_1\}\) and the other active cells are the lambda singletons.
The two newborns in (4.1) have equal size and equal intersection size with
every predecessor cell. Their symmetric difference is contained in the
next newborn. Thus same-neighbor and same-type are exact.

Both middle owners and the next owner are

\[
                 s=B+\rho_1+\lambda_2+\cdots+\lambda_h.
\]

Exactly the \(h\) intervals ending at the center change. At length
\(\ell\), their values are

\[
 K+x_R+\{\lambda_{h-\ell+2},\ldots,\lambda_h\}
 \longleftrightarrow
 K+\rho_1+\{\lambda_{h-\ell+2},\ldots,\lambda_h\}.            \tag{4.2}
\]

The earlier and later reset letters contain both exchanged labels, so every
longer interval and every interval continuing right is unchanged. This
proves literal owner, immediate-upper, arbitrary-width boundary, and
prefix/suffix return.

One mixed/private cap suffices: the center lower bound is \(K\), its cap is
\(K+\{x_R,\rho_1\}\), and every other position is fixed. The center is a
phase-private address under a common cap; it must not be described as one
common maximal source letter for both phases.

## 5. Matching and robustness audit

Declaring \(s\) as a prepared root in the static protected flag theorem
quarantines the \(h\) physical addresses of (4.2). Either phase flag may be
prepared; both use the same addresses, so the flexible matching avoids them
in both phases and supplies external occurrences for the coatoms. This is
an exact static occurrence-transversal statement for pairwise-distinct
prepared roots, not a physical chronology statement or a duplicate-root
supply theorem.

For a physically planted sidecar bank, let \(D\) be the full ray union,
\({\cal T}\) the full target shore, and \(M_\theta\) the cell transversal
matroid of the one-cap background compiler. The baseline condition

\[
                  r_{M_\theta}({\cal C})=|{\cal T}|           \tag{5.1}
\]

is load-bearing. Under it,

\[
       r_{M_\theta^*}(D\cup F)=|D\cup F|                       \tag{5.2}
\]

is exactly the condition that every target, including all old and new
ports, can be matched outside the sidecars and protected deletion \(F\).
For any chosen terminal subset, remove the external matching edges of those
new ports, toggle the corresponding sidecars, and assign their new physical
ports. All other targets keep their external matches. This proves the
adaptive-rematching, declared-terminal-bank property

\[
              {\rm BD}^{\rm rem}_{\mathbf Q^+}
                    (H,1,{\cal F}_B).                         \tag{5.3}
\]

The quantifiers are \(\forall F\,\exists M_F\). They do not prove
item2543L's one-fixed-matching \({\rm BD}(H,1,B)\). A one-target/two-cell
calibration is sharp: with allowed deletions \(\{a\}\) and \(\{b\}\), each
deletion admits a matching, but no one matching survives both.

Put \(F_\cup=\bigcup_{F\in{\cal F}_B}F\). The stronger single test

\[
 r_{M_\theta^*}(D\cup F_\cup)=|D\cup F_\cup|                 \tag{5.4}
\]

is exactly the existence of one background matching avoiding all potentially
deleted cells at once. It gives the fixed-matching property on the declared
terminal bank, still not paths to arbitrary holes.

With \(B+1\) resource-private copies per named transfer, let each broader
resource deletion \(G\) project to one allowed compiler-cell deletion
\(F(G)\), and require each deleted resource to disable at most one copy.
Then at most \(B\) protected deletions kill at most \(B\) copies, so one
direct copy survives while (5.2) handles the compiler-cell projection.
This gives the exact conditional count \(H(B+1)\) and adaptive height
\(L=1\).
It does not prove that the copies, their matching, and their fixed cap occur
in one physical child chronology.

## 6. Final scope

The audited implications are

\[
\begin{array}{c}
\text{saturated collared pivot}
 \Longrightarrow
 \text{literal lower two-flag ray + one avoiding lower matching},\\[2mm]
\text{auxiliary repeated-owner collar}
 \Longrightarrow
 \text{strict returned stutter},\\[2mm]
\text{strict returned bank + (5.1)--(5.2)}
 \Longrightarrow
 \text{declared-bank }{\rm BD}^{\rm rem}_{\mathbf Q^+},\\[2mm]
\text{strict returned bank + (5.1) + (5.4)}
 \Longrightarrow
 \text{one-fixed-matching direct bank}.
\end{array}
\]

The missing implication is physical cohabitation: the tight pivot source
does not contain an internal strict stutter, while the static quarantine
does not serialize the auxiliary sidecar inside the same chronology and
cap. Repeating (4.1) separately costs \(\Theta(Hh)\) source positions.
Consequently neither zero-stretch same-parity regeneration nor
\(\nu(k)\le B(k)+O(1)\) is proved here.
