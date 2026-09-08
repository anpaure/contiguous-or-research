# Lane R: deterministic \(k=15\) fusion component atlas

Date: 2026-07-28

Status: exact finite obstruction; no Hall-zero fusion certificate is claimed.

## 0. Exact outcome

Let \(P_0=H29\) be the current deficiency-29 rank-eight Hamilton path on
\(\binom{[15]}8\). Two exact negative results close the elementary
deterministic fusion lane.

1. For every one of the \(96\) raw choices of one listed
   \(\tau P_0\)-interior motif for each of the seven zero-candidate targets,
   the resulting \(P_0/\tau P_0\) component closure has neither a spanning
   merge-only \(C_4\) tree nor a spanning merge-only hypertree made from
   initially loose assignment components. Every Hamilton completion in this
   two-parent component cube must use at least one component initially
   nonloose relative to \(M_w\), hence a genuine split/remerge monodromy
   interaction.
2. In the union of the five canonical parents there are exactly \(404\)
   simple base-relative transfer \(3\)-cycles, equivalently alternating
   \(C_6\) switches. Exactly \(202\) give a Hamilton child, and all \(202\)
   retain the two \(H29\) endpoints. Of these, \(174\) are not depth-three
   factorable and \(28\) are resident/factorable. Every one of the \(28\) is
   parent-pure. Exact endpoint-conditioned matching on all \(28\) gives

   \[
   \begin{array}{c|rrrrrr}
   \text{Hall deficiency}&29&30&31&32&33&34\\ \hline
   \text{number of children}&13&3&2&1&6&3.
   \end{array}
   \]

   Thus no single base-relative Hamilton \(C_6\) switch in this five-parent
   atlas yields a factorable child of deficiency below \(29\). In particular,
   all \(29\) Hamilton intrinsic-rainbow \(C_6\) switches are nonresident.

The first statement is a topological obstruction before collars or Hall are
examined. The second is a complete exact Hall screen of the stated
single-\(C_6\) class. Neither statement rules out a product of several
components, a nonloose compound deck, or one simple transfer cycle of length
at least five and odd length.

## 1. Frozen inputs and coordinate convention

Put

\[
 \Omega=\binom{[15]}8\sqcup\{\partial\},\qquad |\Omega|=6436,
\tag{1.1}
\]

where \(\partial\) closes a Hamilton path through the dummy arcs. The five
parent paths, their linear endpoints, and their base-relative transfer data
are as follows.

\[
\begin{array}{c|l|c|c|c|c}
i&\text{parent file}&\text{start}&\text{end}&
 \#\text{ nontrivial transfer cycles}&\#\text{ changed tails}\\ \hline
0&\texttt{k15\_doubletrans\_05\_213\_hall29.json}&9901&7779&0&0\\
1&\texttt{k15\_outer2\_p1\_h30\_bridge.json}&9901&7779&683&5531\\
2&\texttt{k15\_trans1113\_balanced\_hall31.json}&3757&13923&98&6018\\
3&\texttt{k15\_transposition\_parent\_winner.json}&9901&7779&815&4081\\
4&\texttt{k15\_accumulated\_zero\_parent\_winner.json}&9901&7875&794&4038.
\end{array}
\tag{1.2}
\]

The metadata transposition in \(P_3\) is **zero-based** \([1,12]\), hence it
is the one-based coordinate transposition \((2,13)\). Direct reconstruction
verifies

\[
 P_3=\tau P_0,\qquad
 \tau=(1,12)_{\rm zero\ based}=(2,13)_{\rm one\ based}.
\tag{1.3}
\]

This is not the older program which swapped zero-based coordinates \(0,11\).

The SHA-256 values of \(P_0,\ldots,P_4\), in order, are

    5516482eadaba4f8fb9549b41c79c3b949df2e3224ce68f9dacd3b5b6bc2d21c
    6ea03a3d48a7dd4462d936218385c5cacc17957bbe3be377ca2e00a360487d91
    6d7cee2418f10dbd02076971fdd119d7bc7c35d154430522a70c06f953687ea7
    8d0f732c28a552e919857b1a1c80794ac65f390816d2b89b66a67ed63475d2dd
    2b25279185b50a9485c65cbc727a08d95b71a1d310332cbdcb23dd6b0b3d2cb7

The seven-target motif file is
scratch/t1_12_h29zero7.interior.tsv, SHA-256

    7c472a1a98f8d43f114e6b973ffe3b7b0f8e1aa8cee8f7e3d3f590b03b65b9db

It contains \(16\) interior directed motif words and no endpoint motif:

\[
\begin{array}{c|rrrrrrr}
z&2575&5801&13616&13620&17738&21641&29776\\ \hline
|\mathcal W_z|&4&1&4&1&2&1&3.
\end{array}
\tag{1.4}
\]

Thus there are exactly

\[
                         4\cdot1\cdot4\cdot1\cdot2\cdot1\cdot3=96
\tag{1.5}
\]

raw tuples. Six motif words contain \(10\) directed arcs and ten contain
\(11\). These are the complete words as represented in this fixed-motif
file; no endpoint upper relaxation is used in the component-signature
calculation.

## 2. Exact \(H29/\tau H29\) component signatures

Let \(p,q\in\operatorname{Sym}(\Omega)\) be the dummy-closed successors of
\(P_0,P_3\), and put

\[
                         \phi=p^{-1}q,\qquad q=p\phi.
\tag{2.1}
\]

The permutation \(\phi\) has \(815\) nontrivial cycles on \(4081\) tails and
\(2355\) fixed tails. Its exact nontrivial length histogram is

\[
\begin{array}{c|rrrrrrrrrrrrrr}
\ell&2&3&4&5&6&7&8&9&10&11&12&13&14&15\\ \hline
n_\ell&295&123&75&62&54&46&33&28&23&10&14&5&12&12
\end{array}
\tag{2.2}
\]

and

\[
\begin{array}{c|rrrrrrrrr}
\ell&16&17&18&19&20&22&23&26&28\\ \hline
n_\ell&5&7&4&1&2&1&1&1&1.
\end{array}
\tag{2.3}
\]

Every motif word in (1.4) was checked arc by arc. Each arc is either common
to \(p,q\) or is \(q\)-exclusive; no word contains a \(p\)-exclusive arc or
an arc outside the two-parent union. A \(q\)-exclusive arc forces the whole
\(\phi\)-cycle containing its tail to the \(q\)-shore. Hence a tuple \(w\)
has a consistent forced set \(F_w\) of nontrivial \(\phi\)-cycles and the
minimal forced cover is

\[
                         M_w=p\phi_{F_w}.
\tag{2.4}
\]

All \(96\) sets \(F_w\) are distinct. Their sizes range from \(29\) to \(49\),
and \(M_w\) has from \(6\) to \(23\) directed cycles.

For an optional component \(\gamma\notin F_w\), let

\[
 e_w(\gamma)=\{K:\ K\text{ is an }M_w\text{-cycle and }
                        K\cap\operatorname{supp}(\gamma)\ne\varnothing\}.
\tag{2.5}
\]

Define three incidence objects on the \(M_w\)-cycles.

* \(G_2(w)\) has an edge \(e_w(\gamma)\) for every optional transposition
  \(\gamma\) whose two tails lie on distinct \(M_w\)-cycles.
* \(L(w)\) has the hyperedge \(e_w(\gamma)\) for every optional component
  meeting every \(M_w\)-cycle in at most one tail and meeting at least two
  such cycles. Call these components **initially loose**.
* \(A(w)\) has \(e_w(\gamma)\) for every optional component, without a
  multiplicity restriction.

### Theorem 2.1 (all \(96\) merge-only certificates are obstructed)

For every one of the \(96\) tuples \(w\), both \(G_2(w)\) and \(L(w)\) are
disconnected. The loose hypergraph has between \(3\) and \(12\) connected
components. The unrestricted hypergraph \(A(w)\) is connected for every
tuple.

Consequently:

1. no tuple admits a protected merge-only \(C_4\) spanning-tree fusion using
   optional \(P_0/P_3\) whole-component switches;
2. no tuple admits a merge-only assignment hypertree using only initially
   loose optional \(P_0/P_3\) components; and
3. every Hamilton whole-component completion of \(M_w\) must select at least
   one optional component \(\gamma\) for which

   \[
     |K\cap\operatorname{supp}(\gamma)|\ge2
   \tag{2.6}
   \]

   on some initial \(M_w\)-cycle \(K\).

These conclusions remain true after protecting arcs already selected in
\(M_w\), or after imposing residence-collar and seam-safety restrictions:
such conditions restrict the admissible set of products and therefore cannot
destroy the invariant blocks or restore a Hamilton product within the
obstructed switch family. They are not claimed for an additional requirement
which forces a formerly optional component to the opposite shore; that
operation must first be absorbed into a new base cover and its incidence
objects recomputed.

#### Proof

Let \(\mathcal S\) be any allowed switch subfamily and form its incidence
hypergraph on the cycles of \(M_w\). For a connected component \(B\) of this
hypergraph, let \(V_B\) be the union of the vertices on its \(M_w\)-cycle
nodes. The base cover \(M_w\) preserves \(V_B\). The support of every
\(\gamma\in\mathcal S\) is contained wholly in \(V_B\) for one \(B\), so
\(\gamma\) also preserves every \(V_B\). Therefore

\[
                 M_w\prod_{\gamma\in J}\gamma
\tag{2.7}
\]

preserves every \(V_B\), for every \(J\subseteq\mathcal S\). If the incidence
hypergraph is disconnected, (2.7) cannot be one cycle.

Apply this argument first to all optional transpositions. A transposition
whose two tails lie on one \(M_w\)-cycle has a singleton footprint and also
preserves the \(G_2(w)\) blocks. Thus disconnection of \(G_2(w)\) rules out
every Hamilton product of optional transpositions, not merely one chosen
tree. Apply the same argument to all initially loose optional components;
the invariant-block argument using the hyperedges of \(L(w)\) rules out every
Hamilton product using only initially loose components and proves (2.6).

The asserted finite counts and disconnections are the exhaustive records in
scratch/k15_fusion_signature_atlas_20260728.json: the Cartesian product in
(1.5) is enumerated literally, and every component support and every tuple
record is stored. The mathematical implication from those incidence records
is the invariant-block argument above.

The \(96\) tuples are raw choices of one listed \(P_3\)-motif for each old
zero. They are not asserted to be simultaneous distinct-cell matchings, and
they contain no separately protected incumbent \(P_0\) windows. The universal
incidence obstruction applies to every physically valid subfamily of these
raw tuples, but does not enlarge their physical meaning. \(\square\)

### Why unrestricted connectivity is not a certificate

The connectivity of \(A(w)\) supplies no positive monodromy statement. It
forgets support multiplicity, cyclic order, residence collars, and physical
Hall capacity. In fact it is forced here: toggling every optional component
in (2.4) gives \(q\), which is one Hamilton parent. If \(A(w)\) were
disconnected, the proof of Theorem 2.1 would contradict this fact. Thus every
useful mixed/Hall-repairing completion in this two-parent whole-component
cube must include an initially nonloose component and audit the exact
single-or-compound split/remerge monodromy.

## 3. The complete single-\(C_6\) atlas base-relative to \(P_0\)

For each parent successor \(p_i\), define its base-relative transfer
permutation

\[
                         \pi_i=p^{-1}p_i.
\tag{3.1}
\]

At each tail \(x\), retain every labelled transfer arc
\(x\to\pi_i(x)\). A simple directed transfer cycle

\[
                         \gamma=(x_1\ x_2\ \cdots\ x_s)
\tag{3.2}
\]

gives the degree-correct successor \(p\gamma\): its replacement normal arc at
\(x_j\) is

\[
                         x_j\longmapsto p(x_{j+1}),
\tag{3.3}
\]

which occurs in every parent label stored on the transfer arc
\(x_j\to x_{j+1}\). In the bipartite successor overlay, (3.2) is an
alternating \(C_{2s}\).

Call (3.2) **intrinsic-rainbow** when no one parent supplies all \(s\)
replacement arcs. This does not mean that all seam labels are distinct.

The exact simple-cycle atlas through \(s=4\) is

\[
\begin{array}{c|r|r|r|r|r}
s&\text{all cycles}&\text{intrinsic-rainbow}&
 \text{Hamilton}&\text{Hamilton rainbow}&
 \text{endpoint-preserving Hamilton rainbow}\\ \hline
2&818&32&0&0&0\\
3&404&68&202&29&29\\
4&314&116&0&0&0.
\end{array}
\tag{3.4}
\]

All \(202\) Hamilton \(s=3\) children, not only the \(29\) rainbow ones,
preserve the \(P_0\) endpoints \(9901,7779\).

### Lemma 3.1 (exact \(C_6\) monodromy)

Let \(\alpha\) be the cyclic order in which the three support tails of
\(\gamma\) occur along the one-cycle \(p\). Then

\[
                         c(p\gamma)=c(\gamma\alpha).
\tag{3.5}
\]

Thus \(p\gamma\) is one cycle exactly when \(\gamma=\alpha\); for the reverse
orientation \(\gamma=\alpha^{-1}\), the child has three cycles.

#### Proof

Cut \(p\) at the three support tails. The three resulting directed segments
are connected before the switch according to \(\alpha\), and after the switch
according to \(\gamma\alpha\). This is the cut-segment cycle identity. There
are only two directed \(3\)-cycles on the support. If \(\gamma=\alpha\), then
\(\gamma\alpha=\alpha^2\), one cycle. If
\(\gamma=\alpha^{-1}\), then \(\gamma\alpha\) is the identity, with three
cycles. \(\square\)

This explains the exact \(202+202\) split in (3.4). For even \(s\), parity
already excludes a Hamilton child: \(p\) is a \(6436\)-cycle and has sign
\(-1\), while an even-length transfer cycle has sign \(-1\), so \(p\gamma\)
has sign \(+1\) and cannot be a \(6436\)-cycle. This explains the \(s=2,4\)
Hamilton zeros.

## 4. Exact residence, upper, endpoint, and all-shore audit

Every one of the \(202\) Hamilton \(C_6\) children was reconstructed as a
literal \(6435\)-vertex path. Each path contains every rank-eight mask once,
has no non-Johnson arc, and has start/end \(9901,7779\).

Depth-three residence forbids, in every coordinate trace, an internal word

\[
                         0\,1^j\,0,\qquad 1\le j\le3.
\tag{4.1}
\]

The residence-violation histogram over all \(202\) children is

\[
\begin{array}{c|rrrrrrrr}
\#\text{ violations}&0&1&2&3&4&5&6&7\\ \hline
\#\text{ children}&28&21&38&45&36&30&3&1.
\end{array}
\tag{4.2}
\]

The exact linear-erosion compiler graph reports NOT_FACTORABLE on exactly
the \(174\) nonresident children. It builds successfully on exactly the \(28\)
residence-zero children. All \(28\) are parent-pure in the precise sense that
the three donor sets in (3.3) have nonempty intersection:

\[
\begin{array}{c|rrr}
\text{common donor}&P_1=H30&P_3=\tau_{(1,12)}P_0&P_4=\tau_{(5,7)}P_0\\ \hline
\text{resident children}&2&14&12.
\end{array}
\tag{4.3}
\]

In particular, every one of the \(29\) Hamilton intrinsic-rainbow children
is nonresident. Their violation histogram is

\[
\begin{array}{c|rrrrr}
\#\text{ violations}&1&2&3&4&5\\ \hline
\#\text{ rainbow children}&2&5&9&8&5.
\end{array}
\tag{4.4}
\]

For every factorable child, the endpoint-conditioned all-lower graph has
\(16383\) targets and \(19311\) physical cells. Exact maximum matching gives

\[
\begin{array}{c|r|r|r}
\text{deficiency}&\text{matching size}&\text{number of children}&
\text{number also passing all }q+1\text{ upper screens}\\ \hline
29&16354&13&8\\
30&16353&3&2\\
31&16352&2&0\\
32&16351&1&0\\
33&16350&6&3\\
34&16349&3&0.
\end{array}
\tag{4.5}
\]

The last column totals \(13\). Those \(13\) jointly resident and
\(q+1\)-upper-complete paths are all parent-pure: nine have common donor
\(P_3\), and four have common donor \(P_4\). Their frozen files are in
scratch/k15_fusion_all202_c6_candidates_20260728/. Grouped by deficiency,
they are

    Hall 29: fusion_0835_hall29.json, fusion_0939_hall29.json,
             fusion_0993_hall29.json, fusion_1100_hall29.json,
             fusion_1149_hall29.json, fusion_1187_hall29.json,
             fusion_1197_hall29.json, fusion_1216_hall29.json
    Hall 30: fusion_1028_hall30.json, fusion_1166_hall30.json
    Hall 33: fusion_0987_hall33.json, fusion_1012_hall33.json,
             fusion_1160_hall33.json

The Hall pass was also run **before** upper screening on every Hamilton child.
Thus no Hall improvement is hidden among the \(15\) resident children which
fail the \(q+1\) upper screen. No candidate has deficiency below \(29\); the
frozen-candidate list is empty and no below-29 file was produced.

### Independent audit

The native graph/matching result in (4.5) was independently replayed on one
H100 CPU core using the Python incidence builder and a separate
Hopcroft--Karp maximum matching. It rebuilt all \(28\) factorable graphs and
reported the same deficiency for every child, with zero disagreements. The
audit artifact is
scratch/k15_fusion_all202_c6_fullhall_python_verify_20260728.json.

The thirteen jointly resident/upper-complete paths were additionally replayed
from their three transfer tails. Their endpoints, Johnson arcs, residence,
upper loads, transfer order, and exact donor sets all reproduce.

### Scope of the physical checks

The zero-hole \(q+1\) upper audit is a sound upper-shadow certificate. Failure
of that screen is only a conservative rejection if arbitrary longer literal
intervals are allowed. This distinction does not affect the no-Hall-\(<29\)
statement, because Hall was evaluated on all \(28\) resident children before
upper rejection.

The all-lower matching in (4.5) is the exact endpoint-conditioned compiler
Hall graph. A perfect matching would still need a literal compiler assignment
and a full contiguous-OR verifier before proving a word. Here every matching
is deficient, so no such positive inference is made.

## 5. Monitored five-parent jobs, not used as proofs

The retained large jobs were monitored and not duplicated.

* The residence-on five-face run ended UNKNOWN after
  \(604.6651673601009\) seconds with no candidate.
* The residence-skipped run ended UNKNOWN after
  \(303.9574286690913\) seconds with no candidate.
* The later \(1800\)-second hint-parent run was stopped by the user to free
  H100 CPU. It produced no summary or candidate and carries no mathematical
  conclusion.
* The separately monitored dynamic-DM run
  global_exact_dm_fixed_h29 generated one exact deficit-29 cut and ended its
  next round UNKNOWN; its best_key field is null. It did not improve Hall 29.

The frozen summaries are

    scratch/exactdm_5cycle_boundaryupper.summary.json
    scratch/exactdm_5cycle_boundaryupper_nores.summary.json
    scratch/global_exact_dm_fixed_h29.summary.json

The ten two-parent endpoint-upper CP-SAT models in
scratch/k15_exact_pair_nogos_20260728/ report INFEASIBLE. They use exact
interior fixed-shore thresholds and a proof-safe optimistic endpoint upper
palette. No independently checkable solver proof trace is stored, so those
statuses are not used in Theorem 2.1 or the exact matching census (4.5), and
they are not promoted here to a hand proof.

## 6. Precisely open boundary

No concrete fusion certificate exists in the classes just audited. A
successful continuation must leave both elementary classes:

1. For any of the \(96\) seven-motif \(P_0/P_3\) closures, it must use at
   least one initially nonloose optional component and explicitly verify its
   exact single-or-compound split/remerge monodromy.
2. Relative to \(P_0\), a final successor has the form \(p\psi\), where the
   nonfixed part of \(\psi\) decomposes into disjoint simple transfer cycles.
   Any final successor achieving factorability and Hall deficiency below
   \(29\) must therefore have at least two nontrivial cycle components, or
   exactly one odd cycle of length at least five. A lone even cycle is
   excluded by parity. For a lone \(3\)-cycle, all \(28\) factorable Hamilton
   children have Hall deficiency at least \(29\), while the other \(174\)
   Hamilton children are structurally nonfactorable.
3. Any surviving candidate must retain the prescribed endpoints or audit its
   new endpoint palettes literally, have zero depth-three residence defects,
   audit both linear boundary seams, and pass a \(16383/16383\) all-shore
   matching. Only then may a compiler and full contiguous-OR word be
   attempted.

The present result does **not** rule out nonloose \(H29/\tau H29\) products,
five-parent support-seven cycles, multiple \(C_6\) switches whose signed
residence defects cancel, longer transfer cycles, or a general directed-union
Hamilton path. It proves that none of these can be replaced by the previously
proposed protected \(C_4\)/loose-hypertree certificate or by one isolated
base-relative alternating \(C_6\).

## 7. Reproducibility and hashes

The lightweight auditors are

    scratch/analyze_k15_fusion_signatures.py
    scratch/search_k15_fusion_atlas.py
    scratch/audit_k15_fusion_all_c6_hall.py
    scratch/verify_k15_fusion_all_c6_hall_python.py
    scratch/verify_k15_fusion_certificate.py

Their SHA-256 values, in order, are

    17ef385dfbe7a315548ab98f39a8ac9b48d6990873ea046c954f616a4c823ca0
    1d02ee78d45fa28499335519e7c7b05c5f94755e59d3f053f71f30af8c90acd6
    ddfd0f834f5abf76743fb203914ada5ee09ba148d4c2202f6ec6c70ff9e2a6e8
    45b665908ac193db3c52e100382a8a2559e186b37dfff609890d535a95df7fcf
    99cc1d86e02b0a9a851670730b3021213b0e139ff427843476f07b8f8b18969c

The decisive output artifacts are

    scratch/k15_fusion_signature_atlas_20260728.json
    scratch/k15_fusion_c6_audit_20260728.json
    scratch/k15_fusion_all202_c6_audit_20260728.json
    scratch/k15_fusion_all202_c6_fullhall_20260728.json
    scratch/k15_fusion_all202_c6_fullhall_python_verify_20260728.json

with SHA-256 values

    cc0f0709f38f3ce550c761061bd58e306f831934fb2342084f5ca07bf7c5c562
    f3fa4cc58a0e1b85b64f43790ad21c4a3636ab1c5ae4dbd712434304daeefdaf
    b26702c586888d350d3345cf7dc81b68b24bdda93d2a7b892fedc432efab4a99
    16a8bf66a41ae633a75d0ebfa0b56fe1167f2638be279812b07821ad3c2cf7b1
    8bfaaa9f3171647eae6b09525f1d8c7ed6bedd2863dedd91d806e20d50ea3b8d

The first JSON stores every \(\phi\)-component support, every motif signature,
and all \(96\) tuple-incidence records. The fourth stores the exact Hall result
or NOT_FACTORABLE status for every one of the \(202\) Hamilton \(C_6\)
children. Hence both obstruction layers are independently inspectable without
rerunning an optimization solver.

The generated all-202 and candidate JSON files retain the bare remote parent
basenames, and the full-Hall JSON records its source atlas under the undated
remote alias k15_fusion_all202_c6_audit.json. Their mathematical contents and
hashes are frozen, but a rerun from the problem root must resolve those names
to the corresponding files under scratch/ (or run from that directory).
