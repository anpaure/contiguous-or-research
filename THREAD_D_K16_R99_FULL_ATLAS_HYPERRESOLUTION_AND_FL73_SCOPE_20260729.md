# Thread D — full-atlas guarded hyperresolution and fl73 scope

**Date:** 2026-07-29  
**Status:** exact solver-free audit complete. The four resistant motifs admit
syntactically clean depth-two resolvents, but every such resolvent is
dominated by an already available primitive portal clause. Consequently the
effective full-atlas closure remains $143/147$, not $147/147$.

## 1. Frozen quotient instance

Let $F$ be the 858-edge quotient factor in
`scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json`, and let
$\mathcal A$ be the complete set of 26,570 loopless off-source quotient
edges. Write $c_e=1$ when $e\in F$ is cut and $a_f=1$ when
$f\in\mathcal A$ is added. Exact degree restoration is

\[
 \sum_{f\in\mathcal A:f\ni v}a_f
 =\sum_{e\in F:e\ni v}c_e.                         \tag{1.1}
\]

For a lower or upper $q1$ colour $\gamma$, let
$S_\gamma\subseteq F$ and $A_\gamma\subseteq\mathcal A$ be its complete
source and off-source provider sets.

### Provider-current lemma

Let $Z$ be a vertex cover of the graph $A_\gamma$, and put

\[
 B_F(Z)=\{e\in F:\operatorname{ends}(e)\cap Z\ne\varnothing\}.
\]

Every exact $q1$-complete degree-restored repair satisfies

\[
 \bigwedge_{e\in S_\gamma}c_e
 \quad\Longrightarrow\quad
 \bigvee_{h\in B_F(Z)}c_h.                         \tag{1.2}
\]

Indeed, if every source provider is cut, $q1$ coverage selects some
$f\in A_\gamma$. The cover gives an endpoint $v\in f\cap Z$. The left side
of (1.1) is positive at $v$, so the right side is positive and some source
edge in $B_F(Z)$ is cut. This uses the complete provider atlas and does not
assume a candidate endpoint halo.

## 2. Exact one-level criterion

Let $M$ be a hard residence motif, so
$\sum_{e\in M}c_e\ge1$. Choose a $q1$ colour $\gamma_e$ carried by each
$e\in M$, and define

\[
 K=\bigcup_{e\in M}(S_{\gamma_e}\setminus\{e\}).     \tag{2.1}
\]

Applying (1.2) to whichever motif edge is cut gives

\[
 \bigwedge_{k\in K}c_k
 \quad\Longrightarrow\quad
 \bigvee_{h\in B}c_h,
 \qquad B=\bigcup_{e\in M}B_F(Z_e).                 \tag{2.2}
\]

This guarded clause is non-tautological exactly when the covers can be
chosen with $K\cap B=\varnothing$.

**Trapped-provider criterion.** Put
$V(K)=\bigcup_{k\in K}\operatorname{ends}(k)$. Covers $Z_e$ with
$K\cap B=\varnothing$ exist if and only if

\[
 \operatorname{ends}(f)\not\subseteq V(K)
 \quad\text{for every }e\in M\text{ and }f\in A_{\gamma_e}. \tag{2.3}
\]

For sufficiency, choose from every provider $f$ one endpoint outside
$V(K)$; their union covers the provider graph while avoiding all guard
endpoints. Conversely, if a provider lies wholly in $V(K)$, every cover
selects an endpoint of some guard edge and therefore puts that guard edge in
$B$.

The full-atlas replay checks all $2^{|M|}$ lower/upper choices. It produces
665 direct rows covering 130 motifs and 13 additional multi-source/parallel
rows, for 143 of the 147 motifs. The failures are exactly

\[
\begin{array}{c|l|c}
M&\text{source edge IDs}&\text{colour choices checked}\\ \hline
6&25152,25170&4\\
122&10917,10919,11115,13230&16\\
123&10917,11115,13230,13521&16\\
146&24778,24978,25152,25170&16.
\end{array}                                           \tag{2.4}
\]

For each of these 52 assignments the saved certificate identifies a literal
off-source provider trapped in $V(K)$. Thus (2.3), rather than a
restricted-atlas accident, is the precise obstruction to one-level closure.

## 3. Depth-two hyperresolution

Represent an implication by

\[
 C(N,P):\quad \bigwedge_{e\in N}c_e
 \Longrightarrow\bigvee_{h\in P}c_h.               \tag{3.1}
\]

A resistant base clause has $O=N_0\cap P_0\ne\varnothing$. For every
$x\in O$, choose a second complete-provider clause $C(N_x,P_x)$ with
$x\in N_x$. Resolving every old overlap gives

\[
 N=N_0\cup\bigcup_{x\in O}(N_x\setminus\{x\}),
 \qquad
 P=(P_0\setminus O)\cup\bigcup_{x\in O}P_x.          \tag{3.2}
\]

The audit enumerates every inclusion-minimal provider cover, rejects
persistent and newly introduced polarity collisions, and rejects a positive
side containing any complete hard motif. Its exact census is

\[
\begin{array}{c|r|r|r|r|c}
M&\text{raw roots}&\text{distinct bases}&
 \text{secondary products after safe pruning}&\text{clean rows}&(|N|,|P|)\\ \hline
6&225&170&61&1&(2,46)\\
122&53760&24528&8502&47&(2,59)\\
123&53760&14558&2841&16&(2,59)\\
146&54000&30807&6881&16&(2,65).
\end{array}                                           \tag{3.3}
\]

Thus there is a literal syntactic depth-two certificate for each resistant
motif. This does **not** yield four new master cuts.

### Collision-safe depth-two dominance theorem

For every secondary parent in (3.2),

\[
                         N_x\subseteq N,
 \qquad                   P_x\subseteq P.             \tag{3.4}
\]

The pivot $x$ remains negative because it was already in $N_0$; the other
negative literals are added to $N$, and the complete positive head is added
to $P$. Therefore the parent clause $C(N_x,P_x)$ is a literal subset of, and
logically subsumes, $C(N,P)$.

The domination also holds for the standard $0\le c\le1$ linear rows. From

\[
 \sum_{e\in N_x}c_e-\sum_{h\in P_x}c_h\le |N_x|-1
\]

and (3.4), adding at most $|N\setminus N_x|$ remaining negative variables
and dropping the remaining nonnegative positive variables gives

\[
 \sum_{e\in N}c_e-\sum_{h\in P}c_h\le |N|-1.         \tag{3.5}
\]

In the four canonical certificates the dominating parents are already among
the 1,328 eager singleton portal rows:

- for $M_6,M_{146}$, the lower clauses at source edges 18499 and 26654;
- for $M_{122},M_{123}$, the upper clause at source edge 11009.

The 665 direct and 13 incremental motif-compressed rows were also checked;
none is the relevant dominator. The primitive portal parents are. Hence

\[
 \boxed{\text{syntactically clean depth-two rows}=4,\qquad
        \text{genuinely new master rows}=0.}          \tag{3.6}
\]

This is structural: resolving only the positive copy of a base polarity
overlap while retaining its negative copy cannot strengthen a model that
already contains the secondary parent. A useful next row must use aggregate
endpoint current or multiplicity, a joint motif demand, or a deeper
resolution that actually eliminates the secondary parent literals.

## 4. Geometry of the surviving gate

The four labels contain only two local structures. First,

\[
                       M_6\subset M_{146}.             \tag{4.1}
\]

Thus $M_{146}$ contributes no independent hitting demand once $M_6$ is
enforced. It remains useful only as an occurrence/geometry label.

Second, put

\[
 A=\{10917,11115,13230\},\qquad b=10919,\qquad d=13521.
\]

The two motif rows are

\[
 \left(\bigvee_{e\in A}c_e\right)\vee c_b,
 \qquad
 \left(\bigvee_{e\in A}c_e\right)\vee c_d.           \tag{4.2}
\]

If all three shared edges are retained, both $b$ and $d$ must be cut. The
next potentially new separator is therefore a **joint two-demand
endpoint-current cut**, not another single-head portal implication. This is
the precise interface to the joint double-hypergraph cover and the universal
seam assumption-core Benders subproblem.

Operationally, the four syntactic rows must remain audit-only; installing
them in the r99 master would add size without changing either the integer
feasible set or its current portal LP relaxation.

## 5. Reconciliation with fl73

The r99 source is equivariant: its 858 quotient edges lift to 12,870 physical
edges. The artifact
`scratch/k16_q1_endpoint_resume1_failedlit73_20260729.json` is instead a
non-equivariant physical factor. Exact comparison gives

\[
 |E_{r99}\cap E_{fl73}|=12726,\qquad
 |E_{r99}\setminus E_{fl73}|=|E_{fl73}\setminus E_{r99}|=144. \tag{5.1}
\]

Fl73 meets 919 quotient orbits, with multiplicity histogram

\[
 1^{55},\ 2^3,\ 3^3,\ 12^3,\ 13^6,\ 14^{49},\ 15^{800}. \tag{5.2}
\]

All nine quotient orbits appearing in (2.4) have multiplicity 15 in fl73.
Consequently each of the four signatures has exactly 15 physical occurrences
there. Nevertheless the numeric motif IDs index the sorted quotient-motif
list of the r99 source; they are not physical occurrence IDs in fl73. A
quotient cut row cannot be copied to fl73 without rebuilding its provider and
endpoint-current proof occurrence by occurrence.

Fl73 has four components, 2,240 short occurrences, perfect lower and upper
$q1$, and failed-literal potential 73. It is now an intermediate endpoint:
exact descendants at potentials 69 and 68 have been recorded. The present
audit makes no descendant-row transport claim; any such use still requires
the same physical occurrence-labelled reconstruction.

## 6. Reproducible artifacts

- One-level generator:
  `scratch/audit_threadD_k16_r99_guarded_motif_portal_rows_20260729.py`,
  SHA-256
  `136416b7ade3a2050c3e505325e5818346965f02c6794202ac5a802f12b70f0a`.
- One-level audit:
  `scratch/threadD_k16_r99_guarded_motif_portal_rows_20260729.audit.json`,
  SHA-256
  `f80338f80a2558bac5326192159dc580bbc7e1bc661e35116e723cd6d7b3e084`.
- Depth-two generator:
  `scratch/audit_threadD_k16_r99_two_level_guarded_hyperresolution_20260729.py`,
  SHA-256
  `c1f8684ecea1cbe3097799fb07ff9e7992dff90961a3ad4189548255aabf1c11`.
- Depth-two audit:
  `scratch/threadD_k16_r99_two_level_guarded_hyperresolution_20260729.audit.json`,
  SHA-256
  `48e436246c4f9dd2ecaf2acfd4cea880e93687115d535a9930899625931191fb`;
  embedded payload
  `ac4f00d64c2557c2139840cfa28cc472b737d7f6a5ad6cb2ac3c6c3010974833`.
- Physical reconciliation generator:
  `scratch/audit_threadD_k16_r99_resistant_motifs_vs_fl73_20260729.py`,
  SHA-256
  `085d104cf603bb92ca5a706e3ce3361fb150e3da13acbf6e318efe6ed4aa6167`.
- Physical reconciliation audit:
  `scratch/threadD_k16_r99_resistant_motifs_vs_fl73_20260729.audit.json`,
  SHA-256
  `109c95a22e885b184035b0cb5a84a6d0fbe751cab8d5fc98c0d770c707583999`.

All three audit generators replay from the frozen catalogue and complete provider
sets without a SAT, CP, LP, or H100 invocation.
