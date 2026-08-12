# The frozen (m=9) rotation forest has raw octagons but no post-hoc sharp native bank

Date: 2026-08-01  
Lane: L, finite calibration for the protected Catalan connector gate  
Status: exact theorem for the authenticated parity-completed (m=9)
rotation forest only.  It is not an all-(m) obstruction and does not test a
jointly reselected forest.

## 0. Verdict

The authenticated (m=9) cap-two forest has 43,758 physical edges on the
48,620 rank-nine owners and exactly 4,862 path components.  It contains many
literal quaternary octagon sides, but none has the component correlation
needed by the one-cycle/one-path absorber:

* there are 180 cyclically unindexed directed sides, equivalently 720 choices
  of the distinguished atom (o_0);
* 144 sides put their four old edges on four different forest paths;
* 36 sides have component multiplicities (2+1+1);
* no side has three old edges on one path, hence none can put
  (o_1,o_3,o_2) in the required directed order.

The complete sharp coatom owner path also cannot be embedded post hoc.
At depth (d=6) its 71 owners exceed the maximum forest-path length 66.
At depth (d=5), all eighteen length-66 paths and all four contiguous
63-owner trims in both orientations fail under every coordinate relabelling.
The obstruction is already the column-weight profile: every coordinate of
every candidate subpath occurs between 18 and 45 times, whereas a rank-nine
lift of the sharp rank-eight target requires one coordinate of weight 63 and
five coordinates of weight zero.

Thus this fixed forest exhibits a clean separation:

\[
 \text{raw octagon supply}\quad\not\Rightarrow\quad
 \text{absorber topology}\quad\not\Rightarrow\quad
 \text{sharp native owner/source bank}.
\]

The live theorem must select or rethread the upper-exact forest jointly with
the recyclable bank.  A universal post-hoc embedding in the authenticated
rotation forest is false.

## 1. Exact octagon index

Let (F) be the physical forest on rank-nine owners.  Fix a seven-set
(S\subset[18]) and (z\notin S).  On the ten labels outside
(S\cup\{z\}), define the directed graph

\[
 a\longrightarrow b
 \quad\Longleftrightarrow\quad
 \{S\cup\{z,a\},\ S\cup\{a,b\}\}\in E(F).
\tag{1.1}
\]

### Lemma 1.1

Directed simple four-cycles of (1.1), modulo cyclic rotation, are in
bijection with cyclically unindexed old quaternary-octagon sides contained in
(F).  Reversing the (a)-cycle gives the opposite octagon convention.

### Proof

For an old octagon atom,

\[
 A_i=S\cup\{z,a_i\},\qquad
 B_i=S\cup\{a_i,a_{i+1}\}.
\]

Hence its physical edge is present precisely when
(a_i\to a_{i+1}) occurs in (1.1).  Four atoms close exactly when the four
arcs form a simple directed four-cycle.  The only indexing redundancy is the
choice of (i=0), namely cyclic rotation.  \(\square\)

The exact census evaluates (1.1) for all
(inom{18}{7}\cdot11) choices of ((S,z)).  It then reconstructs every
forest path and checks the component and directed-position data of all four
old edges.  The resulting component profile is exactly

\[
             144\,[1+1+1+1] + 36\,[2+1+1].
\tag{1.2}
\]

All 144 four-path sides can be globally oriented atom by atom.  Every
two-on-one-path side has incompatible old-edge directions on its repeated
path.  In particular the stricter (o_1,o_3,o_2) path-order row is zero.

## 2. Complete arbitrary-relabeling test at (d=5)

The sharp tensor owner word at depth (d) has length (8d+23), rank
(d+3), and uses (d+7) labels.  For (d=5), it therefore has 63 rank-eight
owners on twelve labels.  A rank-nine realization on the 18-label ground set
must add one fixed core label and leave five labels unused.

For a word (W=(W_0,\ldots,W_{62})), attach to coordinate (x) its binary
column trace

\[
             \tau_x(W)=\{j:x\in W_j\}.
\tag{2.1}
\]

### Lemma 2.1 (column-trace completeness)

Two equal-length set words are related by a coordinate relabelling iff their
multisets of binary column traces agree.

### Proof

A relabelling plainly preserves the multiset.  Conversely, match equal
traces bijectively; membership at every word position is then preserved.
\(\square\)

The forest has exactly eighteen components of length 66, forming one
coordinate-rotation orbit.  These are the only components long enough for
the (d=5) packet.  The audit tests

\[
             18\cdot4\cdot2=144
\tag{2.2}
\]

oriented contiguous 63-owner words against both sharp phases.  Every
candidate has zero universal and zero unused coordinates; more sharply, its
eighteen column weights all lie in ([18,45]).  Both targets have weight
histogram

\[
 0^5\,23^1\,24^3\,30^1\,52^2\,55^5\,63^1.
\tag{2.3}

Therefore no candidate is isomorphic to either phase.  The full trace
comparison also gives zero exact embeddings.

For (d=6), the owner length is (71>66), so the length obstruction is
already complete.

## 3. Owner paths are not native source rays

The 8/9 native-ray theorem concerns fixed endpoints in an expanded
**source** word after maximal inverse reconstruction and two exterior host
splits.  A compatible owner path alone would not determine those source
letters, make the anchors legal split sites, or prove deadline, residence,
common-cap, and protected-Hall compatibility.  The present audit fails one
step earlier: even the complete (d=5) owner path is absent post hoc.

Consequently the exact conclusion is limited to the frozen forest:

* existing raw octagons cannot be promoted to the one-path absorber using
  their current component locations;
* no current long component is a relabelled sharp (d=5) owner packet;
* (d\ge6) is excluded by component length;
* a correlated forest selector, a value-preserving rethread, or newly
  planted source hosts remain open.

## 4. Replays

Run

```text
python3 scratch/search_catalan_m9_octagon_native_bank_20260801.py
python3 scratch/audit_catalan_m9_octagon_owner_path_embedding_20260801.py
```

The first replay rebuilds the authenticated forest and exhausts the indexed
octagon graphs (1.1).  The second independently rebuilds the forest and
checks the complete column-trace criterion (2.1) on all words in (2.2).

