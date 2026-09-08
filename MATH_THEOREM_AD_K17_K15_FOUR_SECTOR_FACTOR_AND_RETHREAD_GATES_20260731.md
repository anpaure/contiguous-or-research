# The exact K15-to-K17 four-sector factor and its rethread gates

Date: 2026-07-31  
Status: literal factor constructed and independently audited; two exact
small-rethread obstructions proved  
Scope: the authenticated two-cycle K15 resident factor and the direct
Catalan-leave four-sector formulas

## 0. Verdict

The fixed-K16 occurrence-transversal route is already solver-free UNSAT, so
this note changes the carrier.  Starting from the exact resident K15 factor,
it constructs a literal spanning Johnson 2-factor on the K17 middle layer
with sector sizes

\[
 |U|=5005,\qquad |X|=|Y|=|A|=6435,
 \qquad 5005+3\cdot6435=24310.
\]

Every one of the \(24310=\binom{17}{8}\) immediate lower colours occurs on
exactly one factor edge.  Thus the Catalan-leave construction is not merely
an abstract deck: it is integral and literal on the current exact parent.

The first deterministic occurrence transversal and cap-two factor are not
near a passing carrier.  The child has 17 cycles, cyclic minimum positive run
two, 3823 length-two runs, 1386 length-three runs, and 4045 arbitrary-width
upper holes.  A canonical linearization has

\[
 (\rho_1,\rho_2,\rho_3)=(1073,24301,24301),
 \qquad \sum_j\rho_j=49675>7401.
\]

There are two stronger conclusions.

1.  For this natural factor, any rethread obtained only by cutting old
    factor edges and reordering/reversing the resulting arcs must delete at
    least **49 edges of its 19170-cycle** before the K17 staircase can
    possibly pass.
2.  More generally, every factor produced by the direct four-sector formulas
    from this parent has a solver-free upper-q1 contradiction.  There are 60
    disjoint opposite-occurrence conflicts.  Any subsequent edge rethread
    must add at least **60 rank-ten edges absent from the chosen direct
    factor**; a Hamilton path must therefore delete at least **61 edges of
    that factor**.

Consequently a few sector reroots cannot finish this lift.  The viable next
neighbourhood is a genuinely global radius-at-least-61 rethread, or a
different four-sector braid whose internal edge formulas are changed before
the occurrence transversal is imposed.

No K17 word or upper bound is claimed.

## 1. Authenticated parent data

The parent is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
    from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

It consists of two directed Johnson cycles of lengths 6390 and 45.  Write
their vertices as \(T_i\), with `succ` and `pred` always interpreted inside
the same parent cycle, and put

\[
 C_i=T_i\cap T_{\operatorname{succ}(i)},\qquad
 V_i=T_i\cup T_{\operatorname{succ}(i)}.
\tag{1.1}
\]

Direct replay gives:

\[
 \{C_i\}=\binom{[15]}7
\]

with multiplicity one, while the \(V_i\) cover
\(\binom{[15]}9\) with multiplicity histogram

\[
 1^{3675}2^{1230}3^{100}.
\tag{1.2}
\]

Choose one occurrence of every \(V\); let \(I\) be the 5005 selected edge
indices and \(J=I^c\).  Then

\[
 |J|=6435-5005=1430=C_8.
\tag{1.3}
\]

This is the exact Catalan leave.

## 2. Literal four-sector factor theorem

Add coordinates \(x,y\).  Define owners

\[
 A_i=C_i\cup\{x,y\},\quad
 X_i=T_i\cup\{x\},\quad
 Y_i=T_i\cup\{y\},\quad
 U_i=V_i\quad(i\in I).
\tag{2.1}
\]

Let \({\cal Z}=\binom{[15]}6\).  Form the bipartite graph

\[
 Z\sim i\quad\Longleftrightarrow\quad i\in I, Z\subset C_i.
\tag{2.2}
\]

Assume it has a simple factor \(K\) of degree two on both shores.  If the
two \(K\)-neighbours of \(Z\) are \(i,j\), include the edge

\[
 A_iA_j.
\tag{2.3}
\]

For every parent edge index \(i\), include

\[
 \begin{cases}
 X_iX_{\operatorname{succ}(i)},&i\in I,\\
 X_iA_i,&i\in J,
 \end{cases}
\qquad
 \begin{cases}
 Y_iY_{\operatorname{succ}(i)},&i\in I,\\
 A_iY_{\operatorname{succ}(i)},&i\in J.
 \end{cases}
\tag{2.4}
\]

Finally put

\[
 L_i=
 \begin{cases}
 U_{\operatorname{pred}(i)},&\operatorname{pred}(i)\in I,\\
 X_i,&\operatorname{pred}(i)\in J,
 \end{cases}
\qquad
 R_i=
 \begin{cases}
 U_i,&i\in I,\\
 Y_i,&i\in J,
 \end{cases}
\tag{2.5}
\]

and include \(L_iR_i\).

### Theorem 2.1

Equations (2.3)--(2.5) form a spanning simple Johnson 2-factor on
\(\binom{[17]}9\).  Its edge intersections enumerate
\(\binom{[17]}8\) exactly once.

### Proof

If \(i,j\) are the two neighbours of \(Z\), then the distinct rank-seven
sets \(C_i,C_j\) both contain the rank-six set \(Z\), so

\[
 A_i\cap A_j=Z\cup\{x,y\}.
\]

The other sector intersections are

\[
 X_i\cap X_{\operatorname{succ}(i)}
 =X_i\cap A_i=C_i\cup\{x\},
\tag{2.6}
\]

\[
 Y_i\cap Y_{\operatorname{succ}(i)}
 =A_i\cap Y_{\operatorname{succ}(i)}=C_i\cup\{y\}.
\tag{2.7}
\]

The four cases in (2.5) all have intersection \(T_i\).  The only nontrivial
case is \(U_{\operatorname{pred}(i)}\cap U_i\).  Both rank-nine sets contain
\(T_i\), and they are distinct because an occurrence transversal cannot
select two occurrences of one \(V\); hence their intersection is exactly
the rank-eight set \(T_i\).

The degree ledger is exact.

* If \(i\in I\), \(A_i\) has its two \(K\)-edges.  If \(i\in J\), it has
  \(X_iA_i\) and \(A_iY_{\operatorname{succ}(i)}\).
* \(X_i\) has its index-\(i\) x-edge and either the predecessor x-edge or
  the \(T_i\)-edge.
* \(Y_i\) has its predecessor y-edge and either the index-\(i\) y-edge or
  the \(T_i\)-edge.
* \(U_i\) has exactly the \(T_i\)- and
  \(T_{\operatorname{succ}(i)}\)-edges.

Thus every owner has degree two.  Simplicity of \(K\) rules out loops.  Two
different \(Z\)'s cannot induce the same \(A_iA_j\), since two distinct
rank-six common subsets would force \(C_i=C_j\).

The four lower-colour classes are

\[
 Z+xy,\qquad C+x,\qquad C+y,\qquad T.
\tag{2.8}
\]

They partition the rank-eight layer, and every member of every class occurs
once.  The owner classes in (2.1) similarly partition the rank-nine layer.
\(\square\)

The indexing details in (2.4)--(2.5) are essential: `pred/succ` are
componentwise, the y-leave edge is \(A_iY_{\operatorname{succ}(i)}\), and
the conditions on \(L_i\) and \(R_i\) use `pred(i)` and `i`, respectively.

## 3. The first exact K17 factor

Take the minimum global parent index in every occurrence class.  For this
fixed \(I\), graph (2.2) has 5005 vertices on each shore and 35035 incidence
edges.  The integral cap-two flow has value

\[
 10010=2\cdot5005.
\]

Applying Theorem 2.1 gives the frozen factor

```text
scratch/ad_k17_k15_four_sector_factor_20260731.json
SHA-256 542a40b2ba905a939e157bdb973b59d873cf22b9b7c3eb86bc15d11ff078a7f3
```

with component lengths

\[
 19170,4067,455,442,135,6,4,4,3,3,3,3,3,3,3,3,3.
\tag{3.1}
\]

Every one of its 24310 edges is Johnson and its lower-q1 palette is the full
24310-element rank-eight layer, with no repetitions.

Its upper-q1 palette has 17709/19448 colours.  The 1739 holes split by the
new-coordinate signature as

\[
 1425\text{ in the }xy\text{ sector},\qquad
 314\text{ in the no-new sector},
\tag{3.2}
\]

with no x-only or y-only hole.  Full cyclic arbitrary-width upper replay has
4045 holes:

\[
 10^{1739},\quad11^{1711},\quad12^{509},\quad13^{86}.
\tag{3.3}
\]

The cyclic lower trace counts by depth are

\[
\begin{array}{c|rrrrrrrr}
q&1&2&3&4&5&6&7&8\\ \hline
\text{missing}&0&2157&1044&310&50&0&0&0.
\end{array}
\tag{3.4}
\]

The cyclic residence histogram begins

\[
 2^{3823}3^{1386};
\tag{3.5}
\]

there is no length-one cyclic run, but the minimum is two.  Listing the
cycles in increasing length is not a proposed carrier—it creates 16
non-Johnson seams—but its exact staircase diagnostic is

\[
 (\rho_1,\rho_2,\rho_3)=(1073,24301,24301).
\tag{3.6}
\]

## 4. Exact q1 master for all transversals and cap-two factors

The direct architecture has a compact exact 0-1 description.

For every parent edge index \(i\), let \(s_i=1\) mean \(i\in I\), and impose

\[
 \sum_{i:V_i=V}s_i=1
 \qquad\left(V\in\binom{[15]}9\right).
\tag{4.1}
\]

For each \(Z\in\binom{[15]}6\) and unordered pair \(i<j\) with
\(Z\subset C_i,C_j\), let \(k_{Zij}=1\) select the two \(K\)-neighbours.
Since exactly nine rank-seven sets contain a fixed \(Z\), there are

\[
 5005\binom92=180180
\tag{4.2}
\]

pair variables.  Impose

\[
 \sum_{i<j}k_{Zij}=1,
\tag{4.3}
\]

and, for every parent index \(i\),

\[
 \sum_{Z,\,j:\,i\in\{i,j\}}k_{Zij}=2s_i.
\tag{4.4}
\]

Introduce four state variables \(q_i^{ab}\), where

\[
 (a,b)=(s_{\operatorname{pred}(i)},s_i),
\]

with one-hot and the two obvious marginal equalities.

The complete rank-ten provider table is then:

\[
\begin{array}{c|c|c}
\text{indicator}&\text{edge}&\text{union}\\ \hline
k_{Zij}&A_iA_j&(C_i\cup C_j)+xy\\
s_i&X_iX_{\mathrm{succ}(i)}&V_i+x\\
1-s_i&X_iA_i&T_i+xy\\
s_i&Y_iY_{\mathrm{succ}(i)}&V_i+y\\
1-s_i&A_iY_{\mathrm{succ}(i)}&T_{\mathrm{succ}(i)}+xy\\
q_i^{11}&U_{\mathrm{pred}(i)}U_i&V_{\mathrm{pred}(i)}\cup V_i\\
q_i^{10}&U_{\mathrm{pred}(i)}Y_i&V_{\mathrm{pred}(i)}+y\\
q_i^{01}&X_iU_i&V_i+x\\
q_i^{00}&X_iY_i&T_i+xy.
\end{array}
\tag{4.5}
\]

For every \(S\in\binom{[17]}{10}\), require the OR of all indicators in
table (4.5) whose union is \(S\).  This is exact: a rank-ten contiguous OR
in a rank-nine Johnson path contains an adjacent pair of distinct rank-nine
facets of \(S\), and that edge itself has union \(S\).

The abstract CP-SAT model has

\[
 6435+180180+4\cdot6435=212355
\]

Boolean variables and 55198 high-level rows.  Every target row is nonempty;
row sizes range from 1 to 31.  The deterministic natural assignment replays
exactly the 1739 physical holes in (3.2), independently validating (4.5).

## 5. A solver-free direct-factor q1 no-go

Among the 19448 target rows, exactly 1140 have one provider.  Every such
provider is a state literal \(q_i^{11}\).  Sixty repeated old rank-nine
colours have all of their occurrences forced selected by these unique rows.

The smallest displayed core is

\[
 V=0x0bf5,qquad O(V)=\{1531,2971\}.
\]

The target

\[
 0x1bf5
\]

has the unique provider \(q_{1531}^{11}\), and therefore forces
\(s_{1531}=1\).  The target

\[
 0x0ff5
\]

has the unique provider \(q_{2971}^{11}\), and therefore forces
\(s_{2971}=1\).  Equation (4.1) permits only one occurrence of `0x0bf5`.
This proves:

### Theorem 5.1 (direct four-sector formula no-go)

No occurrence transversal \(I\) and no cap-two factor \(K\) make the direct
four-sector factor upper-q1 complete on this K15 parent.

The audit finds 60 such conflicting occurrence classes.  Their forced target
families contain 150 target occurrences and all 150 target masks are
distinct.  Whichever occurrence is retained in one conflicting class, at
least one target attached only to an unretained occurrence needs an edge
absent from the selected direct factor.  That edge may still belong to the
ambient catalogue in table (4.5) under a different state; it is new relative
to the chosen factor.  Since one new edge has one rank-ten union, these
repairs add:

### Corollary 5.2 (external q1 edge lower bound)

Every upper-q1-complete rethread of a chosen direct-formula factor must add at
least 60 edges absent from that factor.  If the output is a Hamilton path, it
has one fewer edge than the input 2-factor, so it must delete at least 61 old
factor edges.

The lower bound 60 is exact for the unique-provider subsystem.  Choosing the
smaller forced side in each of the sixty conflicts gives sixty distinct
targets; after declaring precisely those rows externally repaired, all 1140
remaining unique rows admit a common occurrence assignment.  The frozen
60-target list has SHA-256

```text
227d7e578e8bf27e21a99279244a0a49aefd4478b3172b2c0c65bd6c2aa4a22a
```

This does not satisfy the non-unique q1 rows, cap-two degrees, residence, or
connectivity.  It only proves that no stronger bound follows from the
unique-row core alone.

This is an exact edge-count statement.  It does not say that radius 61 is
sufficient, nor does it constrain a braid that changes the internal formulas
before forming the factor.

## 6. Independent staircase cut lower bound for the natural factor

The 19170-cycle in (3.1) has exactly 3372 cyclic positive runs of length at
most three.  Their cyclic start positions are all distinct, and the largest
gap between consecutive starts is 61.

Consider a rethread that deletes \(s\) old edges of this cycle, reverses or
reorders the resulting arcs, and adds arbitrary seams.  One deleted Johnson
edge can lie not only on the boundary of a short run but also inside one.
The exact incidence audit on this frozen cycle assigns to each old edge every
length-at-most-three run containing it as an internal or boundary edge.  Its
histogram is

\[
 0^{11413}1^{5398}2^{1797}3^{562}.
\]

Thus one deleted old edge touches at most three short runs.  This is a frozen
cycle census, not a generic consequence of Johnson adjacency.  No extra
global-endpoint exemption is needed: if an old short run becomes a boundary
run of the final path, the old edge that opens that endpoint is one of the
run's boundary or internal edges, so that run is already touched by a
deleted edge.

If a short run survives inside an arc, reversal can move its start only from
its first to its last 1-position, a displacement at most two.  Deleting
\(s\ge1\) edges from a cycle leaves exactly \(s\) retained path arcs.  A
terminal staircase suffix intersects each oriented arc in at most one old
subarc.  Every whole suffix arc contains no untouched short run: both the old
start and, after reversal, the new start remain inside that suffix arc.  At
most one arc straddles the prefix/suffix threshold.  Trimming its first two
suffix vertices removes the only possible untouched length-at-most-three run
whose new start lies before the threshold.

If the suffix subarcs span \(t\) touched old short-run starts in total, the
maximum-gap ledger therefore gives

\[
 (t+s)61+2.
\]

Using \(t\le3s\), this is

\[
 4s\cdot61+2=244s+2.
\tag{6.1}
\]

The staircase condition implies \(\rho_3\le7401\).  Its allowed prefix has
7402 vertices, so at least

\[
 19170-7402=11768
\]

vertices of the large cycle must lie in the short-start-free suffix.  At
\(s=48\), (6.1) is only 11714.  Therefore:

### Theorem 6.1 (natural-factor reroot lower bound)

At least 49 old edges of the natural 19170-cycle must be deleted before any
arc reordering/reversal can satisfy the K17 staircase budget.

This theorem is only for the frozen first-occurrence/cap-two factor.  The
q1 lower bound in Corollary 5.2 is broader and dominates it for direct-formula
Hamilton rethreads.

## 7. Correct next model and exact remaining boundary

The 212355-variable model in Section 4 should **not** be solved: Theorem 5.1
already proves it UNSAT.  A useful successor must expose Johnson edges beyond
the currently selected direct factor from the beginning.

The complete undirected edge catalogue is still finite and structured.  A
rank-ten set has ten rank-nine facets and therefore 45 Johnson edges; every
Johnson edge has one rank-ten union.  Hence the full K17 middle Johnson graph
has

\[
 \binom{17}{10}\binom{10}{2}=19448\cdot45=875160
\]

edges.  An exact rethread master may use one Boolean per allowed edge and
impose:

1. path degrees and \(24309\) selected edges;
2. lazy connectivity/subtour cuts;
3. one ALO row for every rank-ten union;
4. a radius lower bound of 61 relative to any direct-formula factor;
5. exact staircase replay with lazy short-run cuts or explicit order
   variables; and
6. target-specific connected-path witnesses for every deeper upper mask.

SAT at this layer remains only a carrier certificate.  A final K17 proof
still needs an exact monotone schedule with

\[
 \rho_1+\rho_2+\rho_3\le7401,
\]

then the lower Hall/common-cap compiler and literal replay of all 131071
nonzero masks.

The sharp proved boundary is therefore:

* the four-sector deck and a lower-q1-rainbow factor exist integrally;
* every unmodified direct-factor formula is upper-q1 impossible;
* at least 61 old factor edges must change in any Hamilton-path repair;
* the displayed natural factor independently needs at least 49 large-cycle
  cuts for residence; and
* existence of a radius-at-least-61 upper-complete, staircase-compatible
  rethread remains open.

## 8. Reproducible artifacts

```text
scratch/build_audit_ad_k17_k15_four_sector_factor_20260731.py
  SHA-256 cddb8b40a235214a44e57a5c7722019374d8d8168f6659134e45ecb97503934f
scratch/ad_k17_k15_four_sector_factor_20260731.json
  SHA-256 542a40b2ba905a939e157bdb973b59d873cf22b9b7c3eb86bc15d11ff078a7f3
scratch/ad_k17_k15_four_sector_factor_20260731.audit.json
  SHA-256 c029c6e6d4ecfa4ce21ec7a1a7823b5969e146ee73102f51f1d27c48155f3050
  payload 4359111995fe915e448763b8388dfbb520e96b8b8af84b7fb1f49de85b33a160
scratch/audit_ad_k17_four_sector_bounded_reroot_obstruction_20260731.py
  SHA-256 0df201cfc70deff7da2172fa8f8cdf9075b3fe1c95a89155362cf1bff0cce305
scratch/ad_k17_four_sector_bounded_reroot_obstruction_20260731.audit.json
  SHA-256 bbc63b87f7807a4a408ea61bafb2e7d73c4fdd34a34d426bd8abcd954b778612
  payload 5f6517990930ff5847d214d5bea1c39379b3df94766e612a1f0fdacfcb113b6d
scratch/audit_ad_k17_four_sector_q1_master_20260731.py
  SHA-256 b43dc8cf280af9b484bb41158029efb3f314e47861a9c319c4a3f14337a9926f
scratch/ad_k17_four_sector_q1_master_20260731.audit.json
  SHA-256 6d3a6985c77ac04530808108ab8d4abd623162bad43e1db53dd18ac55a229778
  payload 867f97a372445e467760223edc2d69d8ed9848c24aa967ed0de734f5a1a05139
```

All computations are deterministic finite audits.  No SAT solver, web
query, stochastic search, or long local job is used.
