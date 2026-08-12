# Thread A: the H19 common-compiler DM--Benders theorem and bounded collar exchange

Date: 2026-07-29

Status: exact common-compiler Benders projection; exact DM alternating-component
interpretation of the compatibility tax; a solver-independent proof that the
fixed-carrier tax is exactly two; complete statewise anatomy of the stored
21-mask residual; and a bounded three-seam common-word exchange theorem.  No
physical carrier-changing exchange lowering the joint deficit is constructed.

## 0. Outcome

Let \(T\) be the authoritative Hall-19 carrier

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

and let \(G_{\mathrm{out}}(T)\) be its full one-target-at-a-time compiler
graph on

\[
 n=16383
\tag{0.1}
\]

lower targets and \(19311\) physical cells.  Its matching number is

\[
 \nu_{\mathrm{out}}(T)=16364.
\tag{0.2}
\]

For one common nonempty source word \(A\) with \(D^3A=T\), every physical
cell has one literal OR trace.  Let

\[
 \tau(T)=
 \max_{A:\,D^3A=T,\ A_p\ne\varnothing}
 \#\{\text{distinct rank-one-through-seven short traces of }A\}.
\tag{0.3}
\]

The **common-compiler compatibility tax** is

\[
 \kappa(T)=\nu_{\mathrm{out}}(T)-\tau(T).
\tag{0.4}
\]

This note proves the following.

1. Eliminating the source incidences from the exact compiler gives a
   complete family of bounded minimal blocker-cover Benders cuts.  Together
   with ordinary target/cell matching constraints, these cuts are necessary
   and sufficient.
2. Relative to any maximum outer matching, \(\kappa(T)\) is exactly the
   minimum number of loss-one alternating components needed to reach a
   matching avoiding every Benders circuit.
3. The stored prefix gives

   \[
      \tau(T)\ge16362,
      \qquad \kappa(T)\le2.
      \tag{0.5}
   \]

   A universal fixed-carrier cut

   \[
      u_{685}+u_{1581}\le1
      \tag{0.6}
   \]

   handles every compiler omitting \(7267\).  If \(7267\) is covered, one of
   its three physical pins is selected.  The retained pair-Benders shore
   certificate gives conditional Hall gaps

   \[
   21,\quad21,\quad22
   \tag{0.7}
   \]

   for its singleton, pair, and triple cells.  Consequently every common
   word misses at least twenty-one targets, and the fully
   solver-independent conclusion is

   \[
      \boxed{\tau(T)=16362,\qquad\kappa(T)=2.}
      \tag{0.8}
   \]

   This proof uses only the static shore payload and a verifier with zero
   matching/SAT/CP-SAT calls.  The optimizer's unretained proof trace is not
   used.
4. For the stored \(16362\)-trace prefix, the two visible extra misses are
   exactly \(685\) and \(7267\) after four one-for-one root/envelope swaps.
   The first is the universal cut (0.6).  The second has an exact right-end
   two-relocation blocker circuit: admitting \(7267\) costs precisely the
   two incumbent targets \(7682,7683\) before any alternating rehouse.
5. A legal three-seam block braid with disjoint depth-three gaps transports
   every safe short-cell trace exactly and admits core-preserving recourse
   on at most nine letters and thirty-six short cells.  A last-witness
   surplus of one in this finite collar lowers the jointly realizable
   deficit.  In particular, an internal collar creating durable nonterminal
   copies of \(7682,7683\) composes with either audited endpoint tail to add
   \(7267\) at no old-target loss.  This is the required bounded
   compound-exchange theorem; finding a physical collar with that signature
   remains open.

The final length-\(6458\) word is a different statement: it appends a
shortest 20-letter suffix to the 21-residual prefix.  It does not turn the
fixed 6438-letter prefix into a common compiler with deficit twenty.

## 1. Fixed-middle common words

Write

\[
 T=(T_0,\ldots,T_{W-1}),
 \qquad W=\binom{15}{8}=6435,
\tag{1.1}
\]

and put

\[
 P_p=
 \bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i,
 \qquad 0\le p<W+3.
\tag{1.2}
\]

Every source word with \(D^3A=T\) satisfies \(A_p\subseteq P_p\).
Conversely, \(A\subseteq P\) has \(D^3A=T\) exactly when

\[
 [i,i+3]\cap\{p:x\in A_p\}\ne\varnothing
 \qquad(i<W,\ x\in T_i).
\tag{1.3}
\]

Let

\[
 {\cal U}=\{(p,x):x\in P_p\}.
\tag{1.4}
\]

A physical cell \(c\) has an interval \(I_c\) of length one, two, or three.
An outer pin is a pair

\[
 e=(S,c)\in E_{\mathrm{out}},
\tag{1.5}
\]

where \(S\) is individually eligible on \(c\).  The pin forbids

\[
 B_e=
 \{(p,x)\in{\cal U}:p\in I_c,\ x\notin S\}.
\tag{1.6}
\]

For a selected outer matching \(M\), define its surviving incidence set

\[
 Z(M)={\cal U}\setminus\bigcup_{e\in M}B_e
\tag{1.7}
\]

and maximal reconstructed word

\[
 A_p(M)=\{x:(p,x)\in Z(M)\}.
\tag{1.8}
\]

The relevant positive obligations are:

\[
\begin{aligned}
 O_{e,x}&=\{(p,x)\in{\cal U}:p\in I_c\},
    &&e=(S,c),\ x\in S,\\
 O_{i,x}&=\{(p,x)\in{\cal U}:p\in[i,i+3]\},
    &&x\in T_i,\\
 O_p&=\{(p,x)\in{\cal U}:x\in P_p\}.
\end{aligned}
\tag{1.9}
\]

The first is conditional on selecting \(e\); the latter two are
unconditional.

## 2. Exact logic-Benders projection

A set \(H\subseteq E_{\mathrm{out}}\) is a **blocker cover** of an obligation
\(O\subseteq{\cal U}\) if

\[
 \forall u\in O\quad \exists e\in H\quad u\in B_e.
\tag{2.1}
\]

It is minimal if no proper subset is a blocker cover.

### Theorem 2.1 (complete common-compiler Benders cuts)

Let \(y_e\in\{0,1\}\) satisfy the ordinary matching constraints

\[
 \sum_{e\ni S}y_e\le1
 \quad(S\in{\cal T}),
 \qquad
 \sum_{e\ni c}y_e\le1
 \quad(c\in{\cal C}).
\tag{2.2}
\]

The selected matching is realized by one nonempty word with middle row \(T\)
if and only if it satisfies all of the following inequalities.

For every selected-pin obligation \(O_{e,x}\) and every minimal blocker
cover \(H\) of it,

\[
 \boxed{
 y_e+\sum_{b\in H}y_b\le |H|.}
\tag{2.3}
\]

For every middle obligation \(O_{i,x}\), every row-nonempty obligation
\(O_p\), and every minimal blocker cover \(H\),

\[
 \boxed{
 \sum_{b\in H}y_b\le |H|-1.}
\tag{2.4}
\]

When these inequalities hold, the word (1.8) is the unique entrywise-maximal
realization.

#### Proof

For fixed binary \(y\), incidence \(u\in{\cal U}\) survives precisely when
no selected blocker containing \(u\) is present.  Thus an obligation \(O\)
fails precisely when the selected blockers contain a cover of \(O\).
Every finite cover contains a minimal cover.

If \(O=O_{e,x}\), the failure matters only when \(e\) is selected.  The
forbidden simultaneous selection of \(e\) and every member of \(H\) is
exactly (2.3).  For an unconditional middle or nonempty-row obligation, the
forbidden selection of every member of \(H\) is exactly (2.4).

If all cuts hold, every selected target bit survives somewhere in its
assigned interval, every required middle bit survives in its four-letter
window, and every source position contains a surviving coordinate.  The
negative part of every selected pin holds by construction of (1.8), so each
assigned interval OR is exactly its label.  Conversely, any common word
realizing the matching must retain one incidence in every obligation, and
therefore cannot select a complete blocker cover.  This proves necessity,
sufficiency, and maximality.  \(\square\)

### Proposition 2.2 (bounded cut locality at \(d=3\))

Every minimal cut in Theorem 2.1 is supported on at most eight consecutive
source positions.  More precisely:

* for a middle bit \(x\in T_i\), its actual incidence carrier
  \(K_{i,x}=\{p\in[i,i+3]:x\in P_p\}\) has size one through four, and every
  existing minimal cover has between two and \(|K_{i,x}|\le4\) blocking
  intervals;
* a nonempty-row obligation has one position and a minimal coordinate cover
  has between two and \(|P_p|\le8\) pins; and
* an anchored target-bit obligation has one to three positions and its cut,
  including its anchor, has between two and four pins.

#### Proof

Every blocking interval has length at most three.  A single blocker cannot
cover \(K_{i,x}\): that pin would itself forbid the middle bit \(x\) at
every position where it can occur, contrary to individual outer
eligibility.  In a minimal set cover every member has a private incidence,
so its size is at most \(|K_{i,x}|\le4\).
A single selected cell is individually eligible and hence cannot omit every
coordinate of \(P_p\), so a nonempty-row blocker cover has size at least two;
one blocker chosen for each coordinate gives the upper bound eight.
An anchored interval has length at most three, hence needs at most three
minimal blockers; adding the anchor gives at most four pins.  The union of a
length-four obligation with length-three blockers extending from its
endpoints lies in at most eight consecutive positions.  The other cases are
shorter.  \(\square\)

Thus the exact common compiler is an ordinary outer matching master plus a
bounded hypergraph of Benders circuits.  Marginal target/cell Hall is the
master relaxation obtained by deleting (2.3)--(2.4).

## 3. Functional trace graphs and DM alternating components

For a common word \(A\), define

\[
 \tau_A(c)=\bigvee_{p\in I_c}A_p.
\tag{3.1}
\]

Let \(G_A\) contain the one edge \(\tau_A(c)c\) whenever
\(\tau_A(c)\) has rank one through seven.  Since every cell has one trace,

\[
 \nu(G_A)=
 \#\{\tau_A(c):1\le|\tau_A(c)|\le7\}.
\tag{3.2}
\]

### Lemma 3.1 (equivalence of trace and Benders optima)

The maximum objective in Theorem 2.1 equals \(\tau(T)\) from (0.3).

#### Proof

For any common word \(A\), choose one cell for every distinct lower trace.
These target/cell pairs are a matching and are realized by \(A\), so they
satisfy all Benders cuts.  Conversely, a Benders-feasible matching of size
\(s\) is realized by (1.8), which has at least those \(s\) distinct traces.
Taking maxima in both directions proves equality.  \(\square\)

Fix a maximum outer matching \(M_*\).  For any Benders-feasible matching
\(M\), the symmetric difference \(M_*\triangle M\) consists of alternating
cycles, balanced paths, and paths containing one more \(M_*\)-edge than
\(M\).  No component can contain one more \(M\)-edge, because that would
augment the maximum matching \(M_*\).

### Theorem 3.2 (exact DM--Benders tax formula)

The compatibility tax \(\kappa(T)\) is the minimum possible number of
\(M_*\)-excess-one alternating paths among all terminal outer matchings
which satisfy every Benders cut (2.3)--(2.4):

\[
 \boxed{
 \kappa(T)=
 \min_{M\ {\rm Benders\ feasible}}
 \#\{\text{\(M_*\)-excess-one components of }M_*\triangle M\}.}
\tag{3.3}
\]

#### Proof

Every alternating cycle and balanced path contributes zero to
\(|M_*|-|M|\); every \(M_*\)-excess-one path contributes one.  There is no
\(M\)-excess component.  Hence the displayed component count equals

\[
 |M_*|-|M|=\nu_{\mathrm{out}}(T)-|M|.
\]

Minimizing over Benders-feasible \(M\), and applying Lemma 3.1, gives
(3.3).  \(\square\)

This is the exact sense in which the two-unit phenomenon is a DM/Benders
tax: it is not another outer Hall shore, but the minimum alternating loss
needed to avoid the common-word blocker circuits.

## 4. The rigorous numerical status on H19

The optimizer model has dimensions

\[
\begin{array}{c|r}
\text{targets}&16383\\
\text{cells}&19311\\
\text{outer edges}&133852\\
\text{allowed source incidences}&32202.
\end{array}
\tag{4.1}
\]

The stored prefix has \(16362\) distinct lower traces and residual

\[
\begin{split}
{\cal R}_{21}=\{&
685,960,1103,2420,2575,2676,4469,5801,7267,7504,8250,\\
&9524,12825,13616,13620,17683,17738,19098,19568,21641,
29776\}.
\end{split}
\tag{4.2}
\]

Its rank histogram is

\[
 4^1\,5^1\,6^{14}\,7^5.
\tag{4.3}
\]

The independent verifier proves that this word is nonempty, has middle row
\(T\), and has exactly (4.2) as its lower residual.  Therefore

\[
 \tau(T)\ge16362.
\tag{4.4}
\]

### Theorem 4.1 (one universal compatibility unit)

Every common compiler on the fixed H19 carrier satisfies

\[
 u_{685}+u_{1581}\le1,
\tag{4.5}
\]

where \(u_S\) indicates that \(S\) occurs as the trace of one physical
compiler cell of length at most three (equivalently, is selected as a short
pin).  It does not mean an unrestricted contiguous occurrence.

Both targets lie outside the old \(516\)-target positive DM shore and hence
are matched by every maximum outer matching.  Consequently

\[
 \tau(T)\le16363.
\tag{4.6}
\]

#### Proof

Target \(685\) has exactly one outer cell, the singleton position
\(c=1\).  It contains coordinate \(2^7=128\), so realizing \(685\) requires
that coordinate in source letter \(A_1\).

Target \(1581\) has exactly three outer cells, with intervals

\[
 \{1\},\qquad[1,2],\qquad[1,3].
\]

Every one contains position \(1\), and \(1581\) omits coordinate \(128\).
Its negative interval condition therefore deletes \(128\) from \(A_1\).
The two targets cannot coexist, proving (4.5).

If a left target lies outside the canonical alternating DM shore, it is
matched by every maximum matching: otherwise the symmetric difference with
the matching defining the shore would give an alternating path from an old
unmatched target to it, placing it in the shore.  Both \(685\) and \(1581\)
are outside.  A common matching of outer size \(16364\) would have to contain
both, contradicting (4.5).  Thus (4.6) follows.  \(\square\)

### Corollary 4.2 (the exact deficit-twenty disjunction)

Let \(X\) be the canonical positive DM left shore of size \(516\), with
\(|N(X)|=497\).  Every common compiler with residual at most twenty covers
\(7267\) and covers exactly one of \(685,1581\).

#### Proof

Every matching misses at least

\[
 |X|-|N(X)|=19
\]

targets of \(X\).  The targets \(685,1581,7267\) all lie outside \(X\).
Theorem 4.1 forces at least one miss among \(685,1581\).  If \(7267\) were
also missed, there would be at least nineteen misses in \(X\) and two
outside it, hence residual at least twenty-one.  Thus residual at most
twenty forces \(7267\) covered.  Its unique outside miss must then be
exactly one of \(685,1581\).  \(\square\)

For each anchor pin

\[
 e_c=(7267,c),
 \qquad c\in\{6437,12874,19310\},
\]

form the **pair-conditioned graph** \(G_c\) as follows.  Delete target
\(7267\), delete the occupied cell \(c\), and delete every outer edge \(f\)
for which the two-pin set \(\{e_c,f\}\) is not realized by a common word.
By Theorem 2.1, each such deletion is a rank-two Benders cut
\(y_{e_c}+y_f\le1\).

### Theorem 4.3 (three conditional pair-Benders Hall shores)

There are explicit target shores \(H_c\) and cell sets \(N_c\) satisfying

\[
 N_{G_c}(H_c)\subseteq N_c
\]

with the exact census

\[
\begin{array}{c|c|c|c|c}
c&|H_c|&|N_c|&|H_c|-|N_c|&
 \text{certified pair-incompatible edges}\\ \hline
6437&683&662&21&100\\
12874&683&662&21&145\\
19310&689&667&22&194.
\end{array}
\]

Consequently every common-compiler matching satisfies the lifted
inequalities

\[
 \boxed{
 \sum_{S\in H_c}(1-u_S)
 \ge (|H_c|-|N_c|)y_{e_c}.}
\tag{4.7}
\]

#### Proof

The static certificate contains the sorted sets \(H_c,N_c\) and a list of
pair edges sufficient to block every edge from \(H_c\) leaving \(N_c\).
Its standalone verifier rebuilds the frozen carrier's
\(16383\) targets, \(19311\) cells, \(133852\) outer edges, and \(32202\)
source incidences.  For each of the \(439\) advertised bad pairs it forms
the entrywise-maximal two-pin word and verifies a genuine missing
selected-positive or middle obligation.  It then checks, for every outer
edge from \(H_c\) to a cell outside \(N_c\), that the cell is the occupied
anchor \(c\) or that the edge is one of those certified bad pairs.  This is
exactly \(N_{G_c}(H_c)\subseteq N_c\); no matching computation is used.

If \(y_{e_c}=1\), every covered target in \(H_c\) must use a distinct cell
of \(N_c\), so at most \(|N_c|\) of them are covered.  This is (4.7).  If
\(y_{e_c}=0\), its right side is zero and the inequality is tautological.
\(\square\)

### Corollary 4.4 (the compatibility tax is exactly two)

Every common word on the fixed H19 carrier misses at least twenty-one lower
targets.  Hence

\[
 \boxed{\tau(T)=16362,\qquad\kappa(T)=2.}
\tag{4.8}
\]

#### Proof

If \(7267\) is covered, choose one physical witness cell \(c\) for it and
choose one witness cell for every other distinct trace.  The resulting
matching has \(y_{e_c}=1\), so (4.7) forces at least twenty-one misses in
\(H_c\) (twenty-two for the triple branch).

If \(7267\) is omitted, the old shore \(X\) forces nineteen misses inside
\(X\), Theorem 4.1 forces at least one of \(685,1581\) to be missed outside
\(X\), and \(7267\notin X\) is a second outside miss.  Again there are at
least twenty-one misses.  Thus \(\tau(T)\le16362\); (4.4) gives the reverse
inequality, and (0.4) gives \(\kappa(T)=2\).  \(\square\)

The proof-safe certificate and verifier are

```text
scratch/k15_h19_7267_pair_benders_shore_certificate_20260729.json
scratch/verify_k15_h19_7267_pair_benders_shore_certificate_20260729.py
```

with SHA-256 values respectively

```text
e4312b83815835b2f06433ceffb7eee52e0cb7865433db7f4de122e9c75b4ccc
91953e138342d8a4595082feb33dcf9e8f9e8a25429174ed79d19b42ac0dc763
```

and combined canonical-data hash

```text
0adaf7cca92689cb558abb27cd16a7d8119d91d7757a70dd3138d6f8dfde6d90
```

The verifier returns `PASS` with `matching_or_solver_calls=0`.  The older
CP-SAT files report the same unforced optimum and the stronger forced-
\(7267\) value \(16361\), but neither solver status is used in Corollary 4.4.

## 5. Exact anatomy of the stored two-unit difference

Let

\[
\begin{split}
\Omega=\{&
960,1103,2420,2575,2676,4213,5801,7504,8217,8218,9524,\\
&13616,13620,17683,17738,18970,19568,21641,29776
\}
\end{split}
\tag{5.1}
\]

be the exposed-root set of the root-exposing outer maximum matching from
`THREAD_A_K15_H19_STATEWISE_DM_PORT_FLOW_AND_MULTIPARENT_OBSTRUCTION_20260729.md`.
Then

\[
 {\cal R}_{21}
 =
 \bigl(\Omega\setminus\{4213,8217,8218,18970\}\bigr)
 \sqcup
 \{685,4469,7267,8250,12825,19098\}.
\tag{5.2}
\]

The four recovered roots occur uniquely in the stored prefix at

\[
\begin{array}{c|c|c|c}
\text{root}&\text{cell}&(\text{depth},\text{start})&
 \text{maximal envelope}\\ \hline
4213&18114&(2,5239)&4469\\
8217&7915&(1,1477)&12825\\
8218&2640&(0,2640)&8250\\
18970&18400&(2,5525)&19098.
\end{array}
\tag{5.3}
\]

Thus four old exposed roots are recovered through four one-for-one
envelope-to-root shrinks.  The two residual targets not paired in this way
are \(685\) and \(7267\).  This is an exact statewise decomposition of

\[
 21=19-4+4+2.
\tag{5.4}
\]

It is not by itself a global upper certificate for \(\tau(T)\).

## 6. The minimal right-end two-relocation exchange

For the stored prefix, choose for every covered target its least canonical
cell ID, where cells are ordered depth-major and then by start.  This gives
a common-word matching \(M_0\) of size \(16362\).
Among all outer edges from its twenty-one unmatched targets to
\(M_0\)-free cells, there is exactly one:

\[
 7267\longrightarrow c_{19310},
 \qquad I_{19310}=[6435,6437].
\tag{6.1}
\]

The endpoint cells on which target \(7267\) is outer-eligible are

\[
\begin{array}{c|c|c}
\text{cell}&\text{interval}&\text{incumbent target in }M_0\\ \hline
6437&\{6437\}&7682\\
12874&[6436,6437]&7683\\
19310&[6435,6437]&\text{free}.
\end{array}
\tag{6.2}
\]

The apparent free triple cell (6.1) is not the minimal common-word move.
The exact Benders projection has two smaller feasible branches.  In both,
delete

\[
 D=\{7682@6437,\ 7683@12874\}.
\tag{6.3}
\]

Then insert \(7267\) either at its singleton or at its two-letter cell:

\[
\begin{aligned}
M_s&=(M_0\setminus D)\cup\{7267@6437\},\\
M_p&=(M_0\setminus D)\cup\{7267@12874\}.
\end{aligned}
\tag{6.4}
\]

### Proposition 6.1 (two exact minimal endpoint branches)

Both \(M_s\) and \(M_p\) are common-word realizable and have size \(16361\).
Their maximal reconstructions agree before position \(6435\), and on
positions \(6432,\ldots,6437\) they are respectively

\[
\begin{aligned}
A^s&=(17937,1585,1571,1603,3651,7267),\\
A^p&=(17937,1585,1571,1603,3139,7267).
\end{aligned}
\tag{6.5}
\]

For both branches the three endpoint middle equations are

\[
 (D^3A)_{6432,6433,6434}=(18035,3699,7779)
 =(T_{6432},T_{6433},T_{6434}).
\tag{6.6}
\]

Moreover, within the endpoint catalogue (6.2), every common-word branch
covering \(7267\) deletes both incumbents \(7682,7683\).  Thus a net gain of
one through this endpoint motif is possible exactly when those two exposed
target labels can be rehoused on distinct cells by a Benders-safe
alternating completion.

#### Proof

Apply the maximal reconstruction formula (1.8) after each toggle in (6.4).
Only the endpoint blockers change.  Direct intersection of the surviving
allowed sets gives the two tails in (6.5); every letter is nonzero.  Taking
the three four-letter ORs gives (6.6).  The selected singleton or pair has
OR \(7267\), and every retained selected cell keeps all of its positive
bits.  Theorem 2.1 therefore proves common-word feasibility.

Cell capacity forces deletion of the incumbent on whichever cell in (6.2)
receives \(7267\).  In the singleton branch, retaining
\(7683@[6436,6437]\) is impossible: the bitmask of coordinates present in
\(7267\) but absent from \(7683\) is
\(96\).  Thus the singleton letter at \(6437\) already contains forbidden
bits of the pair trace \(7683\).  In the pair branch, retaining
\(7682@\{6437\}\) is impossible: the bitmask of coordinates present in
\(7682\) but absent from \(7267\) is
\(512\).  Thus the singleton letter would put a forbidden bit into the pair
trace \(7267\).  The triple branch \(7267@19310\) also omits coordinate \(512\)
throughout both incumbent intervals and forces four old endpoint pins to
move.  It is locally nonminimal in relocation count, but has a different
Benders neighbourhood and is not globally discarded.  Equivalently, these
conflicts are the endpoint blocker-cover cuts from Theorem 2.1.
Hence both old labels must be exposed.  Restoring both through
vertex-disjoint Benders-compatible alternating paths changes the
cardinality by \(-2+3=1\), and without both restorations there is no
positive gain.
\(\square\)

### Proposition 6.2 (exact two-path companion criterion)

Fix either \(M^-\in\{M_s,M_p\}\).  A terminal common compiler covering
every target covered by \(M_0\), and also \(7267\), exists if and only if
there is a pairwise vertex-disjoint alternating family consisting of two
\(M^-\)-augmenting paths starting at the exposed target labels
\(7682,7683\) and ending at distinct free cells, together with alternating
cycles and cell-to-cell balanced alternating paths, whose complete toggle
avoids every Benders circuit (2.3)--(2.4).

Any such certificate has size \(16363\) and lowers the literal common-word
residual from twenty-one to twenty.

#### Proof

Proposition 6.1 proves that \(M^-\) is common-realizable and has size
\(16361\).  The required covered set has size \(16363\), and (4.6) forbids
any common compiler of larger size.  Thus a desired terminal matching adds
precisely the two labels exposed by (6.3), while retaining \(7267\).  Its
symmetric difference with \(M^-\) therefore has two augmenting paths
starting at those labels; all
other components are alternating cycles or cell-to-cell balanced paths.
Conversely, toggling such a vertex-disjoint family restores the two labels,
does not expose any formerly covered target, and preserves target/cell
degree.  Theorem 2.1 makes avoidance
of every Benders circuit equivalent to realization by one common word.  The
terminal size is \(16361+2=16363\).  \(\square\)

The longer triple-cell toggle \(7267@19310\) is a valid four-relocation
branch.  It is locally nonminimal, but it frees different cells and induces
a different maximal word, so a global dominance map is not proved.  The
conditional shores in Theorem 4.3 prove that no fixed-carrier branch reaches
\(16363\): the two augmenting paths in Proposition 6.2 cannot both exist
without crossing a pair-Benders cut.  A carrier-changing collar can escape
only by destroying the relevant conditional shore, along either a minimal
two-relocation branch or the distinct triple-cell branch.

## 7. Bounded three-seam common-word transport

The endpoint exchange is one local signature.  The following theorem gives
a general bounded carrier-changing macro.

Let a middle path be cut into four blocks

\[
 T=A\mid B\mid C\mid D
\tag{7.1}
\]

and let

\[
 T'=A\mid\epsilon_C(C)\mid\epsilon_B(B)\mid D,
\tag{7.2}
\]

where each \(\epsilon\) is identity or reversal and \(T'\) is a legal
rank-eight Johnson path.  Assume \(|B|,|C|\ge d\), which makes the three
length-\(d\) seam gaps in each order pairwise disjoint; transported block
cores are allowed to be empty.  Let \(G_-\) be the union of the three length-\(d\)
source gaps immediately after the old seams, and \(G_+\) the corresponding
three gaps after the new seams.

Outside these gaps, translate source letters with their blocks, reversing
their order when the block is reversed.  Call the transported partial word
\(Q\).

### Theorem 7.1 (three-seam bounded common-compiler exchange)

For arbitrary depth \(d\):

1. the old and new source cores outside \(G_-\) and \(G_+\) have a
   translation/reversal bijection under which maximal erosion envelopes and
   every short-cell OR are identical;
2. at most \(3d\) new source letters are free;
3. every selected-pin obligation whose cell avoids \(G_+\), every
   row-nonempty obligation at a position outside \(G_+\), and every middle
   obligation whose \((d+1)\)-position window avoids \(G_+\) is transported
   exactly;
4. each seam gap meets at most

   \[
      \sum_{\ell=1}^{d}(d+\ell-1)
      =
      \frac{3d^2-d}{2}
   \tag{7.3}
   \]

   cells of lengths \(1,\ldots,d\); and
5. only \(2d\) middle windows per seam can change.

For \(d=3\), this transported core-preserving recourse has at most

\[
 9\text{ free letters},\qquad
 36\text{ exceptional cells},\qquad
 18\text{ affected middle windows}.
\tag{7.4}
\]

Let \({\cal C}_0\) be the set of all distinct rank-one-through-seven traces
of the old common word.  Define

\[
 R=
 \{S\in{\cal C}_0:
   \text{every old witness cell for \(S\) meets \(G_-\)}\},
\tag{7.5}
\]

and let \(L\) be the set of all rank-one-through-seven traces realized by
the new exceptional cells meeting \(G_+\).  For any completed feasible
filling \(Q\) of the at most nine new letters,

\[
 \boxed{
 {\cal C}(Q)=({\cal C}_0\setminus R)\cup L.}
\tag{7.6}
\]

Consequently the joint common-compiler coverage changes by

\[
 |L\setminus({\cal C}_0\setminus R)|-|R|.
\tag{7.7}
\]

It improves by at least one exactly when the right side of (7.7) is
positive.

#### Proof

At a source position more than \(d-1\) beyond a seam, its defining
depth-\(d\) middle window lies wholly inside one transported block.  Under a
translation the window is identical.  Under reversal, if an old middle
block occupies the half-open interval \([u,v)\) and its new slot begins at
\(u'\), a new core-source position \(p'\) corresponds to the old position

\[
 p=v+d-1-(p'-u'),
\]

and its \(d+1\) middle states are the same in reverse order.  Their
intersection, and hence the maximal erosion envelope, is identical.

A short interval disjoint from the seam gaps lies in one core.  Translation
or reversal sends it to a short interval of the same length, and OR is
order-independent.  This proves items 1--3.

A gap of \(d\) consecutive positions meets \(d+\ell-1\) intervals of length
\(\ell\).  Summing over \(\ell=1,\ldots,d\) gives (7.3).  A middle window of
length \(d+1\) meets a fixed \(d\)-gap for at most \(2d\) starts, proving
item 5 and (7.4).

Every old target outside \(R\) has a witness cell disjoint from \(G_-\), and
that cell transports with the same trace.  Every new safe trace arises by
the inverse transport from an old safe cell.  The only remaining traces are
the exceptional labels \(L\).  This proves (7.6), and cardinality gives
(7.7).  \(\square\)

### Corollary 7.2 (exceptional-cell capacity pruning)

Let \({\cal E}_+\) be the set of new exceptional cells meeting \(G_+\).
If

\[
 |R|\ge|{\cal E}_+|,
\tag{7.8}
\]

then no filling of this braid collar can improve common coverage.
At \(d=3\), \(|{\cal E}_+|\le36\).

#### Proof

Every target newly supplied beyond the transported safe set needs a distinct
exceptional cell, so

\[
 |L\setminus({\cal C}_0\setminus R)|\le|{\cal E}_+|.
\]

Insert this into (7.7).  \(\square\)

### Theorem 7.3 (exact core-preserving finite collar recourse)

Fix desired exceptional pins \((S,c)\), with pairwise-distinct target
labels \(S\), pairwise-distinct physical cells \(c\), and intervals \(I_c\)
meeting \(G_+\).  On a new gap position put

\[
 Q_p=
 P'_p\cap
 \bigcap_{(S,c):p\in I_c}S,
\tag{7.9}
\]

where an empty second intersection means the full coordinate set, while
retaining the transported core letters outside \(G_+\).  The collar is
feasible if and only if:

1. every fixed core letter lying in a selected interval is contained in its
   pin label;
2. every \(Q_p\) in (7.9) is nonempty;
3. every selected exceptional interval OR is exactly its label; and
4. every affected middle window has OR exactly \(T'_i\).

These conditions are checked on at most the bounds in (7.4).  Their minimal
failures are exact no-goods for this frozen-core collar branch.  Once a safe
witness for every retained target and every transported middle obligation
is explicitly protected, they are precisely restrictions of the global
Benders cuts of Theorem 2.1 after fixing the transported core incidences.

#### Proof

Negative pin conditions force each gap letter to lie in every label of an
interval containing it, and also in \(P'_p\); hence (7.9) is the unique
entrywise-maximal choice.  Condition 1 is the same negative requirement on
the already fixed core letters.  Conditions 2--4 are respectively
nonemptiness, selected positive-pin obligations, and the middle obligations.
All unaffected obligations transport by Theorem 7.1.  Thus the four
conditions are necessary and sufficient for this fixed core and pin set.
Minimal failures are therefore exact collar no-goods.  Under the stated
safe-witness protection, fixing the core incidences in Theorem 2.1 gives
the same obstruction family.  Without that protection, deleting a core bit
may remain legal in the full model, so no stronger identification is used.
\(\square\)

### Corollary 7.4 (bounded jointly improving compound exchange)

If a Johnson, depth-three-resident, all-upper-complete three-seam braid has
a collar filling satisfying Theorem 7.3 and

\[
 |L\setminus({\cal C}_0\setminus R)|\ge |R|+1,
\tag{7.10}
\]

then it lowers the literal common-word residual

\[
 16383-|{\cal C}(Q)|
\]

by at least one.  At \(k=15,d=3\), the complete common-word recourse is
confined to at most nine letters, thirty-six cells, and eighteen middle
windows.  Physical certification still separately requires the three new
Johnson seam tests, depth-three residence, every upper-support layer
\(q=1,\ldots,7\) across those seams, and the endpoint conditions.  Exact
middle ownership itself is automatic from block reordering.

This is a literal common-word theorem, not an outer-Hall improvement.

## 8. Application and exact remaining boundary

There are two primary concrete bounded targets.

1. **Right-end relocation.**  Realize either exact endpoint signature of
   Proposition 6.1.  A carrier-changing seam must provide two mutually
   Benders-compatible alternating rehousings for

   \[
      \{7682,7683\}
   \]

   while retaining \(7267@6437\) or \(7267@12874\).
   These are the minimum-relocation branches; the locally costlier
   \(7267@19310\) branch remains a distinct global possibility.  A single
   Theorem 7.3 collar can perform this endpoint toggle only when the terminal
   positions belong to \(G_+\), for example at a terminal seam.  Otherwise
   the endpoint toggle is a second collar and requires the separated
   composition below.
2. **Root-2420 ear.**  The audited local ear creates
   \(2420@10221\), but that three-controller rotation is not itself a
   deck-exact braid of the form (7.2): it omits two middle states and
   duplicates two.  It is only a desired local signature for a future
   deck-restoring compound exchange.  In the stored prefix the old trace of
   cell \(10221\) is \(18708\), with two other witnesses; nevertheless it
   costs no last witness only if an alternate \(18708\) witness lies outside
   the old exceptional gaps or is explicitly recreated.  Thus \(18708\),
   together with the exterior services \(10610\) and \(19796\), must be
   included in the witness-survival audit defining \(R\).  No
   multiplicity-one assertion for those two services is used.  In a literal
   block-braid realization, cell \(10221\) must meet \(G_+\); otherwise safe
   transport fixes its trace at \(18708\).

### Proposition 8.1 (separated braid-plus-endpoint absorber)

Let \(A^0=A(M_0)\) be the specific maximal reconstruction used in
Proposition 6.1; Corollary 4.4 implies that its trace set is exactly
\(\mathcal C_0\).  Suppose a physically legal internal braid is applied to
\(A^0\) using the exact core transport of Theorems 7.1 and 7.3.  Assume both
\(G_-\) and \(G_+\) are separated from the terminal support
\([6432,6437]\): no short cell and no four-letter middle window meets both.
Thus the transported word agrees with \(A^0\) on the terminal support, and
the braided middle row agrees with \(T\) on every middle window meeting that
support.  Suppose the internal collar:

1. protects the transported \(M_0\)-witness pin for every target outside
   \(\{7682,7683\}\); and
2. creates distinct nonterminal witness cells for both \(7682\) and \(7683\),
   with intervals disjoint from \([6432,6437]\).

Then applying either endpoint tail in (6.5) produces a word on the braided
carrier whose trace set contains

\[
 \mathcal C_0\cup\{7267\}.
\]

Hence its literal residual is at most twenty.

#### Proof

The separation hypothesis says that the internal collar obligations and the
endpoint collar obligations have disjoint supports in both the short-cell
and \(D^3\) systems.  Therefore their verified source assignments can be
combined.  Because the terminal baseline is exactly \(A^0\), Proposition
6.1 preserves every transported \(M_0\) pin except the two deliberately
deleted endpoint pins, preserves the endpoint middle windows, and creates
\(7267\).  The two new nonterminal witnesses survive by disjointness and
replace those deleted pins.  Thus all \(16362\) old targets and \(7267\)
occur.  \(\square\)

If the two supports overlap, Proposition 8.1 is unavailable: one must audit
one joint maximal \(Q\)-table on their union.

A third, conceptually clean target is a carrier-changing collar that creates
an interior occurrence of either \(685\) or \(1581\) compatible with the
other.  The fixed-carrier inequality (0.6) is universal only because every
available \(1581\)-interval meets the unique \(685\)-position; an interior
socket is exactly how a braid could escape it.

The interior \(685/1581\) signature lowers the residual when it is realized
in one physically legal exceptional collar satisfying (7.10).  The endpoint
signature lowers it either through a terminal joint collar or through
Proposition 8.1.  The \(2420\) signature requires the same exceptional-cell
condition.  No such physical certificate is known.

The proved boundary is:

* the common compiler is exactly outer matching plus bounded Benders cuts;
* the compatibility tax is exactly an alternating-component loss;
* the fixed-carrier tax is exactly two: omission of \(7267\) is certified by
  the old DM shore plus \(685/1581\), while coverage of \(7267\) is certified
  by the three conditional pair-Benders shores;
* the minimal endpoint attempt is the exact \(7267\) two-relocation
  exchange, and its fixed-carrier two-path completion is now ruled out;
* the three-seam transport subclass admits exact core-preserving finite
  recourse on at most \(9\) letters and \(36\) cells; but
* no physically legal carrier-changing positive-surplus collar is presently
  known.

No heavy local search was run.  All numerical statements above were obtained
from the stored prefix, frozen full graph, and lightweight deterministic
parsing.

## 9. Authoritative inputs

The fixed numerical frontier and literal word are from

```text
MATH_CERTIFICATE_K15_EXPLICIT_6458_UPPER_BOUND_20260729.md
scratch/k15_h19_exact_compiler_maxcoverage_s1501.incumbent.word
scratch/k15_h19_exact_compiler_maxcoverage_s1501.verify.json
```

The outer DM state and its statewise obstruction are from

```text
THREAD_A_K15_H19_STATEWISE_DM_PORT_FLOW_AND_MULTIPARENT_OBSTRUCTION_20260729.md
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

The solver-free tax-two proof object is

```text
scratch/k15_h19_7267_pair_benders_shore_certificate_20260729.json
scratch/verify_k15_h19_7267_pair_benders_shore_certificate_20260729.py
```

The older optimization reports, retained only as redundant evidence, are

```text
scratch/optimize_k15_exact_compiler_maxcoverage.py
scratch/k15_h19_exact_compiler_maxcoverage_s1501.json
scratch/k15_h19_common_compiler_portfolio_20260729/authoritative.force7267.solve.json
```
