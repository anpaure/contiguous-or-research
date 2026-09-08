# Audit of the K17 tight-staircase integrated-fragment compiler theorem

Date: 2026-07-31  
Lane: K, pure mathematics  
Audited theorem:
`MATH_THEOREM_K17_TIGHT_STAIRCASE_RAINBOW_GUARD_ORBIT_COMPILER_20260731.md`  
Theorem SHA-256:
`9e8b81652176031790c8b60cac33c6d9062f4d4fad5c3bf61bec28afe7dcab83`

## 1. Verdict

PASS after correction.  Three independent adversarial audits checked the
staircase/chain ledger, orbit-flow and sector arithmetic, and the
maximal-common-cap implications.  A fourth focused audit checked the final
pair-choice provider theorem.

The result is conditional.  It proves no K17 carrier and no K17 upper bound.
The presently available lower-rainbow 2-factor has 4413 upper-q1 holes and a
large short-run frontier, so it is explicitly outside the theorem's carrier
hypotheses.

## 2. Exact arithmetic independently checked

The following constants and identities were recomputed independently.

1. (W=24310), (L=24313), lower demand (65535), and staircase budget
   (7401).
2. The arbitrary-start loss, chain counts (N_1,N_2,N_3), and the
   rank-only condition

   \[
   \tau_1+(\tau_2-\alpha_1)_+
   +(\tau_3-\alpha_2)_+ +(W-\alpha_3)\le3
   \]

   are exact in their stated rank-relaxation scope.
3. The one-pivot atlas consists of all 24313 singleton cells, all 24312
   adjacent pairs, and the 16910 triples starting at positions
   (7401,\ldots,24310).  Its surplus is zero.
4. The spectral identity

   \[
   H_Q=D_Q+R_Q-\Omega
   \]

   is exact.  The empty-target correction in the zeta moments is included:
   (h_0=65535), not 65536.
5. The four lower-signature masses are

   \[
   (22818,16384,16384,9949),
   \]

   and after all rank-eight pins the residual masses are

   \[
   (16383,9949,9949,4944),
   \]

   totalling 41225.
6. The natural (C_{15}) target census is

   \[
   (1520,1091,1091,662)
   \]

   free orbits and exceptional physical masses ((18,19,19,19)).

## 3. Integrated-fragment audit

For (f=737) protected (U)-fragments inserted into distinct no-new YAX
junctions, the exact edge-slot identity is

\[
(1429-f)+(5005-f)+2f=6434.
\]

At (f=737), this is

\[
692+4268+1474=6434.
\]

This proves component neutrality only at the slot-count level.  The literal
palette theorem additionally requires the disjoint identity

\[
\binom{[15]}8
=C_U\dot\cup C_{\rm YAX}\dot\cup C_{\rm cross}
 \dot\cup\{c_\star\}.
\]

The provenance-erasure lemma is correctly scoped: two histories with the
same final ordered chronology, schedule, baseline caps, and pins give the
same compiler instance.  It says nothing about existence of that chronology.

## 4. Collar and staircase audit

If (K) is an additional reserved collar-cell set, disjoint from the
rank-eight pin cells, and (Pi_K) pins distinct targets into cells of (K),
then

\[
\Omega_{\rm res}=\Omega-(|K|-|\Pi_K|).
\]

Thus orphan cells, not seams, are charged.  The one-pivot cut formula

\[
\kappa(B)=|B|+
\left|\{p\in[7401,24310]:\{p+1,p+2\}\cap B\ne\varnothing\}\right|
\]

was independently verified.  The 1474 insertion interfaces have union
bounds 4422 lower cells and 8844 windows of lengths two through four, but
zero slack permits no orphan loss.

The balanced core has 16445 contracted components, not 1430: it consists of
1430 nontrivial paths plus 15015 isolated owners.  After opening one residual
edge, 16444 residual connectors remain.  A separate orphan cell at each
connector would already cost (16444>7401); hence almost every connector
must be transparent or discharge a jointly legal target.

The (Sigma_3) summary is complete only when it carries fragment length,
capped prefix/suffix runs, all-one flags, and internal short-run maxima.
The budget is not automatic from Johnson legality or q1 balance.  It is
automatic under full composed depth-three safety; otherwise the exact
one-pivot run gate is

\[
\rho_1=\rho_2=0,\qquad \rho_3\le7401.
\]

## 5. Balanced core and common-cap audit

The proposed residual counts

\[
(AA,XX,YY,AX,AY)=(5005,5005,5005,715,715)
\]

contribute degree vector

\[
(11440,10725,10725,0).
\]

The fixed path bank must contribute

\[
(1430,2145,2145,10010).
\]

Counts prove only sector quotas.  Literal validity separately requires
vertexwise complementary degree, disjoint colour coverage, and connected
2-regular monodromy after contracting the spanning linear forest.

The sector-complete residual Hall cuts have singleton demands
((16383,9949,9949,4944)), distinct pair demands
((26332,21327,19898,14893)), distinct triple demands
((36281,31276,24842)), and full demand 41225.  They are sufficient only
for a matching-closed guarded final bank with identical neighbourhoods in
each signature.

## 6. Pair-choice provider theorem audit

The final formulation passed a separate focused audit.

- A local pair option is a full two-edge pair containing every fixed
  (P_0)-edge at its owner.  It therefore gives residual deficits 0, 1, or
  2 correctly at internal vertices, endpoints, and isolates.
- The complete unary provider domain is

  \[
  {\cal P}^{\max}_y(S)=
  \{J:\Gamma_p(y)\cap S\ne\varnothing\ (p\in J),
       \ S\subseteq\bigvee_{p\in J}\Gamma_p(y)\}.
  \]

- For fixed pair choices, opening, orientation, and schedule, the exact-one
  target constraints, cell injection, and maximal-cap equations are
  necessary and sufficient for a literal lower compiler.
- The survival-literal CNF is exact for fixed pair choices.  A joint
  pair/provider model additionally needs activation, chronology, and
  envelope clauses.
- The 41225-square residual statement applies only after 24310 injective
  rank-eight pins are incorporated and contracted with no orphan
  reservation.

## 7. Sharp remaining invariant

A future upper-aware, resident balanced factor closes the lower compiler if
one opening simultaneously supplies:

1. vertexwise degree, literal q1 palette, and one-cycle monodromy;
2. a legal run/scalar schedule and nonempty owner envelopes;
3. all upper witnesses;
4. a physical, jointly collar-absorbed rank-eight slot basis; and
5. either the exact pair-choice maximal-cap provider system, or a
   matching-closed guarded residual bank satisfying physical/weighted Hall.

Cap-two and PBBS lower-rainbow factors address the first item only.  Their
regularity does not imply the residual common-cap Hall system.

No computation, K16 collar search, or finite K17 solver run was used in this
audit.
