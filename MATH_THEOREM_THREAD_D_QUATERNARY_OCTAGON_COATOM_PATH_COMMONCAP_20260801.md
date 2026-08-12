# A quaternary-octagon coatom tensor gives a resident common-cap path macro

Date: 2026-08-01  
Lane: D, local positive replacement for the literal two-star no-go  
Status: exact local owner-path, residence, interval-OR, maximal-erosion and
common-cap theorem.  The construction is not a four-source-star inverse and
does not include a global host or connector theorem.

## 0. Outcome

The quaternary octagon has a particularly useful three-edge common path
completion.  Its old and new parities extend to the two Hamilton paths

\[
\begin{aligned}
 W^0&=(B_2,A_2,A_0,B_0,B_1,A_1,A_3,B_3),\\
 W^1&=(B_2,A_3,A_1,B_0,B_1,A_2,A_0,B_3).                 \tag{0.1}
\end{aligned}
\]

They have the same endpoints and owner set.  The three common connector
edges are

\[
                    A_0A_2,\qquad A_1A_3,\qquad B_0B_1.  \tag{0.2}
\]

Tensor (0.1) with `d+2` filler coatoms.  At the seven block boundaries use
intersection and union screens in the pattern

\[
                              I,U,I,U,I,U,I.              \tag{0.3}
\]

Thus the union screens lie exactly on the three common connectors and the
intersection screens lie exactly on the four octagon edges.  For every
`d>=1` this gives two literal rank-`r` Johnson paths with the following
properties.

1. Both paths have length `8d+23`, all owners are distinct, and their owner
   sets and endpoints agree.  Their immediate lower and upper palette
   multisets agree; all `8d+22` lower colours are distinct.
2. Every strict internal positive coordinate run has length at least
   `d+1`; the complete clipped boundary residence signatures agree.
3. Their complete distinct-value internal interval-OR decks agree and have
   exactly `8d+49` values.
4. Their prefix profiles differ in one value in each direction, and their
   suffix profiles do likewise.  Consequently their local exterior boundary
   signature has four **typed occurrences** (three distinct values), not an
   unbounded internal bank.  Literal host-crossing transparency still needs
   the two screens in Proposition 3.2.
5. Maximal depth-`d` erosion gives nonempty source words in both phases and
   reconstructs the two owner paths exactly.  The two erosions agree on
   the first and last `d+2` source positions.
6. If `E_p^epsilon` denotes the two maximal erosion letters, then

   \[
                         Q_p=E_p^0\cup E_p^1              \tag{0.4}
   \]

   is one literal Boolean cap family supporting both terminal words.
   For prescribed caps, the exact screened-maximal criterion is stated in
   Theorem 4.2.

This is a positive nonflat `O(d)`-width local macro, with zero phase-length
charge.  It does **not** realize the requested action using only three or
four phase-changing source cells.  The two maximal inverses differ at
exactly `4d+16` source positions; exact thinning reduces this to the sharp
minimum eight for `d>=2` (and twelve for `d=1`).  Equivalently, the
construction has three common union screens and four octagon intersection
screens at the owner level, but its literal source realization is an
eight-address macro rather than a three-/four-star one.

## 1. The active octagon path pair

Let

\[
          \Omega=\{z,a_0,a_1,a_2,a_3\},\qquad
          A_i=\{z,a_i\},\qquad B_i=\{a_i,a_{i+1}\},       \tag{1.1}
\]

where indices are modulo four.  These are the active quotients of the
owners in the quaternary-octagon theorem; any fixed old core may be absorbed
into the core `K` below.  Let the old and new octagon matchings be

\[
       O=\{A_iB_i:0\le i<4\},\qquad
       N=\{A_iB_{i-1}:0\le i<4\}.                        \tag{1.2}
\]

### Lemma 1.1 (three-connector Hamilton completion)

With

\[
                     F_*=\{A_0A_2,A_1A_3,B_0B_1\},       \tag{1.3}
\]

`O union F_*` and `N union F_*` are the two Hamilton paths in (0.1).
Every displayed edge is a Johnson edge.  In particular the two paths have
the same endpoints `B_2,B_3` and the same eight active owners.

#### Proof

Successive pairs in `W^0` are, in order,

\[
 B_2A_2,\ A_2A_0,\ A_0B_0,\ B_0B_1,\
 B_1A_1,\ A_1A_3,\ A_3B_3,                            \tag{1.4}
\]

namely four old octagon edges alternating with the three edges (1.3).
The analogous list for `W^1` is

\[
 B_2A_3,\ A_3A_1,\ A_1B_0,\ B_0B_1,\
 B_1A_2,\ A_2A_0,\ A_0B_3,                            \tag{1.5}
\]

namely four new octagon edges alternating with the same connectors.  An
octagon edge changes `z` for one `a`-label.  An `A_iA_j` connector changes
`a_i` for `a_j`, and `B_0B_1` changes `a_0` for `a_2`.  Hence every edge is
Johnson.  The lists prove all other assertions. \(\square\)

### Proposition 1.2 (complete common-connector census)

Among the eight active owners there are 18 Johnson edges.  Removing the
eight octagon edges in `O union N` leaves ten possible common connector
edges.  Exactly eight of their 120 three-edge subsets make both
`O union F` and `N union F` spanning Hamilton paths with common endpoints:

\[
\begin{array}{c|c}
\{A_0A_2,A_1A_3\}&B_0B_1,\ B_0B_3,\ B_1B_2,\ B_2B_3\\
\{A_0A_2\}&\{B_0B_1,B_2B_3\},\ \{B_0B_3,B_1B_2\}\\
\{A_1A_3\}&\{B_0B_1,B_2B_3\},\ \{B_0B_3,B_1B_2\}.
\end{array}                                               \tag{1.6}
\]

The endpoint choices give 16 oriented path pairs.  None has pointwise-equal
prefix and suffix OR profiles.  Twelve oriented pairs, including (0.1),
are optimal: each side has one pointwise mismatch, and each directed
set-profile difference consists of one value.  The other four oriented
pairs have three pointwise mismatches on each side and two values in each
directed set-profile difference.

This is a census only inside the ten-edge active common-connector fibre; it
does not rule out extra active labels, longer connectors, or non-Johnson
source-level guards.

#### Proof

The ten candidates are the six `A_iA_j` edges and the four cyclic
`B_iB_(i+1)` edges.  Checking the degree sequence and connectivity of
`O union F` and `N union F` leaves exactly the eight rows in (1.6).
Orienting each from either common endpoint and taking cumulative unions
gives the stated `12+4` profile split.  The dependency-free audit enumerates
all ten choose three subsets and records both orientations. \(\square\)

## 2. The coatom/screen tensor

Fix `d>=1` and put

\[
             n=d+2,\qquad \Phi=\{f_0,\ldots,f_{n-1}\},
             \qquad C_t=\Phi-\{f_t\}.                    \tag{2.1}
\]

Let `K`, `Omega` and `Phi` be pairwise disjoint and take

\[
                              |K|=r-d-3.                  \tag{2.2}
\]

Thus `r>=d+3`.  The total number of named roles is

\[
                 |K|+|\Omega|+|\Phi|=r+4,               \tag{2.3}
\]

so a literal realization requires ground size `k>=r+4`.  Replace an active
owner `V` by the coatom block

\[
 \mathcal B(V)=
 (K\cup V\cup C_0,\ldots,K\cup V\cup C_{n-1}).          \tag{2.4}
\]

For adjacent active owners `V,V'`, define

\[
\begin{aligned}
 I(V,V')&=K\cup(V\cap V')\cup\Phi,\\
 U(V,V')&=K\cup(V\cup V')
              \cup(\Phi-\{f_0,f_{n-1}\}).               \tag{2.5}
\end{aligned}
\]

Both have rank `r`.  Between consecutive blocks of either word (0.1), use
`I` at transition positions `0,2,4,6` and `U` at positions `1,3,5`.
Denote the resulting words by `T^0,T^1`.

### Theorem 2.1 (literal equicardinal path tensor)

For every `d>=1`, `T^0,T^1` are rank-`r` Johnson paths of common length

\[
                              8n+7=8d+23.                 \tag{2.6}
\]

All owners in either word are distinct, and

\[
                     \{T_i^0\}=\{T_i^1\},\qquad
                     T_0^0=T_0^1,\quad
                     T_{8d+22}^0=T_{8d+22}^1.             \tag{2.7}
\]

#### Proof

Relative to the last letter of `B(V)`, the intersection screen removes the
unique active label in `V-V'` and inserts `f_(n-1)`.  Relative to the first
letter of `B(V')`, it removes `f_0` and inserts the unique label in `V'-V`.
For the union screen the two exchanges are reversed: from the left it
removes `f_0` and inserts `V'-V`, and toward the right it removes
`V-V'` and inserts `f_(n-1)`.  Hence all joins are Johnson.

The active parts of the seven screens are

\[
\begin{array}{c|ccccccc}
 &0&1&2&3&4&5&6\\ \hline
 T^0&a_2&za_0a_2&a_0&a_0a_1a_2&a_1&za_1a_3&a_3\\
 T^1&a_3&za_1a_3&a_1&a_0a_1a_2&a_2&za_0a_2&a_0.
\end{array}                                               \tag{2.8}
\]

The two rows are permutations of the same seven distinct values.  The
eight active block labels are also a common set.  Block letters, intersection
screens and union screens have different filler parts, so no cross-class
collision is possible.  This proves distinctness and (2.7); (2.6) is the
eight blocks plus seven screens. \(\square\)

### Corollary 2.2 (exact immediate palettes)

The two phases have identical multisets of consecutive lower intersections
and consecutive upper unions.  Every lower colour is distinct, so the lower
support has size `8d+22`.  The upper support has exactly 14 distinct values.

#### Proof

The within-block edges depend only on the active block owner, and the block
owner set is common.  For the two edges incident with each screen, substitute
the seven active screen rows (2.8).  The four octagon transitions have the
same lower/upper resource multisets by the quaternary identity, while the
three connector transitions are common.  The same finite table shows that
the lower values do not repeat and that the upper support has size 14.
\(\square\)

### Proposition 2.3 (template-sharp support width)

More generally, if the same tensor uses `n` filler coatoms, its shortest
strict internal filler run is exactly `n-1`.  Hence depth-`d` residence in
this coatom/screen template requires

\[
                              n\ge d+2.                   \tag{2.9}
\]

Consequently `8d+23` is the minimum owner support of this fixed eight-block,
seven-screen template.  This is not a lower bound for arbitrary nonflat
three-/four-star macros.

#### Proof

At a union screen both endpoint fillers `f_0,f_(n-1)` are absent.  Following
either one to its next block omission exhibits a strict positive run of
length `n-1`; all other filler gaps are at least this long.  A depth-`d`
resident word requires every strict positive run to have length at least
`d+1`, giving (2.9).  Equality is Theorem 3.1 below. \(\square\)

## 3. Exact residence and upper-deck ledger

### Theorem 3.1 (resident internal-deck transparency)

The two tensor phases satisfy all of the following.

1. Every strict internal positive run has length at least `d+1`.
2. Their leading and trailing positive-run lengths, clipped at `d+1`, and
   their endpoint bits agree coordinatewise.
3. Their complete distinct-value interval-OR decks agree and have size

   \[
                               8n+33=8d+49.               \tag{3.1}
   \]

#### Proof

Every active-coordinate occurrence meeting a screen also meets an adjacent
whole block: an intersection-screen coordinate belongs to both endpoint
owners and a union-screen coordinate belongs to at least one.  Thus every
strict active run contains a full block and has length at least `n`.

Each filler coordinate is absent once in each block.  Intersection screens
contain all of `Phi`, while a union screen omits only `f_0,f_(n-1)`.
Counting between consecutive absences gives minimum positive run `n-1=d+1`,
and this value is attained.  The screen pattern and filler order are
positionwise phase-independent.  Both phases begin with the complete
`B_2` block and end with the complete `B_3` block, proving the clipped
boundary assertion.

For the OR deck, an interval has filler union smaller than `Phi` only in
one of the following classes:

* one block letter, giving `8n` values;
* one union screen, giving three values;
* the last block letter followed by its union screen, giving three values;
* a union screen followed by the first letter of the next block, giving
  three values.

These four classes agree between phases by the common block set and the
common union-screen set in (2.8).  Every other interval has full filler
union.  Its active OR belongs to the same 24-element family in both phases:
all nonempty subsets of `Omega` except

\[
\begin{gathered}
 \{z\},\ \{a_0,a_2\},\ \{a_1,a_3\},\
 \{a_0,a_2,a_3\},\ \{a_1,a_2,a_3\},\\
 \{a_0,a_1,a_3\},\ \{a_0,a_1,a_2,a_3\}.                \tag{3.2}
\end{gathered}
\]

This last finite table follows directly by taking interval unions in the
15-symbol active words obtained from (0.1) and (2.8).  It is also replayed
independently for every audited depth.  The four disjoint deck classes have
total size `8n+3+3+3+24=8n+33`, proving the claim. \(\square\)

Internal-deck equality is stronger than merely bounded internal damage, but
it does not imply arbitrary exterior crossing transparency.  Put

\[
\begin{aligned}
 \Pi_0&=K\cup\Phi\cup\{z,a_0,a_2,a_3\},&
 \Pi_1&=K\cup\Phi\cup\{z,a_1,a_2,a_3\},\\
 \Sigma_0&=K\cup\Phi\cup\{z,a_0,a_1,a_3\},&
 \Sigma_1&=\Pi_0.                                       \tag{3.3}
\end{aligned}
\]

### Proposition 3.2 (exact four-value exterior boundary)

Each phase has five distinct prefix OR values and five distinct suffix OR
values.  Their only differences are

\[
\begin{array}{c|cc}
 &T^0\setminus T^1&T^1\setminus T^0\\ \hline
 \text{prefix}&\Pi_0&\Pi_1\\
 \text{suffix}&\Sigma_0&\Sigma_1.
\end{array}                                               \tag{3.4}
\]

Thus the local exterior boundary signature has four typed occurrences
(three distinct
set values).  More precisely, a frozen left exterior OR `E_L` screens the
prefix discrepancy pointwise if and only if

\[
                            \{a_0,a_1\}\subseteq E_L,     \tag{3.5}
\]

and a frozen right exterior OR `E_R` screens the suffix discrepancy
pointwise if and only if

\[
                            \{a_1,a_2\}\subseteq E_R.     \tag{3.6}
\]

Without (3.5)--(3.6), every affected crossing interval is still described
exactly by adjoining its frozen exterior OR to the corresponding one of the
four values in (3.4); no arbitrary internal target needs to be exported.
However, as the frozen exterior suffix/prefix varies, these composites can
produce an unbounded number of distinct global targets.  Four local typed
signatures alone therefore do **not** prove arbitrary exterior upper
coverage; one needs the dominance guards (3.5)--(3.6) or a separate
boundary matching.

#### Proof

Taking cumulative unions in the two displayed tensor words gives (3.4).
The two prefix exceptions differ only by `a_0` versus `a_1`, proving (3.5).
The suffix exceptions differ only by `a_1` versus `a_2`, proving (3.6).
\(\square\)

## 4. Literal maximal erosion and common caps

Let `L=8d+23`.  For phase `epsilon` and source position
`0<=p<L+d`, define the maximal depth-`d` erosion letter

\[
 E_p^\epsilon=
 \bigcap_{\max(0,p-d)\le i\le\min(L-1,p)}T_i^\epsilon.    \tag{4.1}
\]

### Lemma 4.1 (nonempty exact inverse and returned boundary state)

Every `E_p^epsilon` is nonempty and

\[
              T_i^\epsilon=\bigcup_{p=i}^{i+d}E_p^\epsilon
              \qquad(0\le i<L).                         \tag{4.2}
\]

Moreover,

\[
 E_p^0=E_p^1
 \quad\text{for }0\le p\le d+1
 \quad\text{and for }L-2\le p\le L+d-1.                 \tag{4.3}
\]

Thus the complete first and last `d+2` source-address states return
literally.

There is also a phase-common central erosion bank

\[
 E_p^0=E_p^1
       \qquad(4d+9\le p\le5d+13),                        \tag{4.4}
\]

of exact length `d+5`.  It is centred on the common `B_0B_1` connector.

#### Proof

A set of at most `d+1=n-1` consecutive tensor owners meets at most one
screen.  Within one block, at most `n-1` different coatom omissions leave a
filler coordinate in their intersection.  Across a screen, the unique
active coordinate in the intersection of its two endpoint owners belongs
to every met block letter and to either screen type.  This proves
nonemptiness.

For one coordinate, maximal erosion followed by length-`d+1` union deletes
exactly strict internal positive runs shorter than `d+1`; clipped endpoint
runs survive through the partial intersections in (4.1).  Theorem 3.1 has
no such short internal run, proving (4.2).  Finally, the first `d+2=n`
owners are the common `B_2` block and the last `d+2` owners are the common
`B_3` block.  Formula (4.1) gives (4.3).

The common central owner interval starts with block `B_0` at
`3(n+1)` and ends with block `B_1` at `5n+3`.  An erosion window
`[p-d,p]` lies inside it precisely for

\[
                  3(n+1)+d\le p\le5n+3.
\]

Substituting `n=d+2` gives (4.4), including its length `d+5`.
\(\square\)

### Theorem 4.2 (exact prescribed common-cap criterion)

Let `P_p` be arbitrary nonempty Boolean caps on the `L+d` source positions
and put

\[
                         M_p^\epsilon=P_p\cap E_p^\epsilon. \tag{4.5}
\]

There are two nonempty source words `X^0,X^1`, both using this same cap
family, such that

\[
             X_p^\epsilon\subseteq P_p,\qquad
             D^dX^\epsilon=T^\epsilon,                    \tag{4.6}
\]

if and only if, for both phases,

\[
 M_p^\epsilon\ne\varnothing\quad\text{for all }p,
 \qquad
 T_i^\epsilon=\bigcup_{p=i}^{i+d}M_p^\epsilon
                    \quad\text{for all }i.                \tag{4.7}
\]

When feasible, `M^epsilon` is the componentwise maximal phase word.  In
particular the free choice

\[
                         Q_p=E_p^0\cup E_p^1              \tag{4.8}
\]

is one common cap family, and the two maximal words are exactly
`E^0,E^1`.  By (4.3), this common cap equals the common erosion letter on
the first and last `d+2` positions.

#### Proof

Any source letter at `p` which reconstructs phase `epsilon` must lie in
every target owner using `p`, hence in `E_p^epsilon`; the cap additionally
forces it into `P_p`.  Thus it lies in `M_p^epsilon`, proving necessity of
(4.7): indeed `X_p^epsilon subseteq M_p^epsilon subseteq E_p^epsilon`
gives

\[
 T^\epsilon=D^dX^\epsilon\subseteq D^dM^\epsilon
       \subseteq D^dE^\epsilon=T^\epsilon.
\]

Conversely the words `M^epsilon` directly satisfy (4.6) when
(4.7) holds.  For (4.8), intersection with `E_p^epsilon` returns
`E_p^epsilon` itself, and Lemma 4.1 completes the proof. \(\square\)

Direct erosion of the finite phase table also gives the exact inverse
mobility ledger

\[
                     |\{p:E_p^0\ne E_p^1\}|=4(d+4).       \tag{4.9}
\]

The four intervals are

\[
\begin{aligned}
 &[d+2,2d+5],&&[3d+5,4d+8],\\
 &[5d+14,6d+17],&&[7d+17,8d+20].                         \tag{4.10}
\end{aligned}
\]

For `d>=2` they are disjoint with positive gaps; for `d=1` the first two
and last two intervals are adjacent.  Their complement also proves the
central equality (4.4).  Formula (4.9) is why
this theorem must not be advertised as a four-source-star construction.

### Proposition 4.3 (eight-address lower bound for every exact inverse)

The `4d+16` in (4.9) is a statement about the maximal inverse.  There is
also an inverse-independent obstruction: **any** exact pair of nonempty
source words `X^0,X^1` satisfying `D^dX^epsilon=T^epsilon` differs at
least eight source addresses.  For `d>=2` the minimum is exactly eight;
for `d=1` it is exactly twelve.

For an owner-coordinate obligation `(i,x)` with
`x in T_i^0-T_i^1`, every phase-zero inverse must place `x` at some source
position in

\[
 \mathcal A(i,x)=\{p:i\le p\le i+d,\ x\in E_p^0\}.       \tag{4.11}
\]

Every phase-one source letter at every position in this set omits `x`,
because owner `i` omits `x` in phase one.  Thus each obligation forces a
phase-different source address in its admissible set.

For every `d>=2`, the following eight obligations have pairwise-disjoint
admissible intervals:

\[
\begin{array}{c|c|c}
x&i&\mathcal A(i,x)\\ \hline
a_2&d+2&[d+2,2d+2]\\
a_2&2d+3&[2d+3,2d+5]\\
a_0&2d+5&\{3d+5\}\\
a_0&3d+6&[3d+6,4d+6]\\
a_1&5d+14&[5d+14,6d+14]\\
a_1&6d+15&[6d+15,6d+17]\\
a_3&6d+17&\{7d+17\}\\
a_3&7d+18&[7d+18,8d+18].
\end{array}                                               \tag{4.12}
\]

This proves the lower bound eight.  It is attained.  Put

\[
\begin{split}
 D_8=\{&d+4,2d+5,3d+5,3d+8,\\
       &5d+16,6d+17,7d+17,7d+20\},                      \tag{4.13}
\end{split}
\]

let `R_p=E_p^0 cap E_p^1`, and define

\[
 X_p^\epsilon=
 \begin{cases}
 E_p^\epsilon,&p\in D_8,\\
 R_p,&p\notin D_8.
 \end{cases}                                             \tag{4.14}
\]

For completeness, the exact active-coordinate target traces are

\[
\begin{array}{c|c|c}
 &T^0&T^1\\ \hline
a_0&[2d+5,4d+11]\cup[7d+21,8d+22]
   &[3d+9,4d+11]\cup[6d+17,8d+22]\\
a_1&[3d+9,6d+17]&[2d+5,5d+13]\\
a_2&[0,2d+5]\cup[4d+11,5d+13]
   &[0,d+1]\cup[4d+11,6d+17]\\
a_3&[0,d+1]\cup[6d+17,8d+22]
   &[0,2d+5]\cup[7d+21,8d+22].
\end{array}                                               \tag{4.15}
\]

The core, `z`, and filler traces are phase-common.  Substituting (4.13)
into the eight active rows (4.15), with `R` elsewhere, covers each displayed
interval and introduces nothing outside it.  Hence coordinatewise dilation
gives `D^dX^epsilon=T^epsilon`; all letters are nonempty, and the two words
differ exactly on `D_8`.  This proves the attainment uniformly in `d`, not
only in the finite replay.

At `d=1`, interval scheduling on the finite 31-owner trace gives twelve
pairwise-disjoint obligation domains.  Equality is attained by (4.14) with

\[
 D_{12}=\{4,5,7,8,10,11,20,21,23,24,26,27\}.             \tag{4.16}
\]

The audit records the twelve disjoint domains and literal replay.  Hence the
positive tensor is not a three- or four-source-star realization even after
maximal erosion is replaced by an arbitrary exact antecedent.  For `d>=2`
it is, however, an exact **eight-address** phase macro inside the one common
cap (4.8).

## 5. Exact scope

The construction proves a positive local replacement for the varying-rank
owner obstruction of two separated asymmetric selectors:

\[
\begin{array}{c}
\text{four octagon edges + three common connectors}\\
\Downarrow\\
\text{two equicardinal resident Johnson paths, same owners and internal OR deck,}\\
\text{one free common cap, and a four-occurrence local exterior signature.}
\end{array}                                                \tag{5.1}
\]

Its owner support is `8d+23` and its maximal inverse support is `9d+23`.
Changing phase adds no cells: both terminal words have those same lengths.
The theorem does not prove:

* a direct realization by only three or four inserted source stars;
* compatibility with a prescribed parent cap beyond the iff test (4.7);
* external Johnson guards realizing (3.5)--(3.6);
* a global packet host, owner-disjoint bank, or connector supply; or
* any all-dimension `B(k)+O(1)` recurrence.

In particular, this tensor is distinct from the direct four-arm star lift:
the latter has four changing source occurrences but fails no-buffer
residence, whereas this resident tensor needs eight changing addresses in
every exact inverse for `d>=2` (the maximal inverse uses `4d+16`).

## 6. Replay

Run

```text
python3 scratch/audit_threadD_quaternary_octagon_coatom_path_commoncap_20260801.py --write
```

The dependency-free audit checks depths `1<=d<=12`, all owner/rank/Johnson
rows, the exact `8d+49` interval-deck count, the four boundary values,
residence and clipped signatures, maximal erosion, source reconstruction,
the common cap (4.8), and all 32 exterior active-label screens for
(3.5)--(3.6).  It reports

```text
PASS_THREADD_QUATERNARY_OCTAGON_COATOM_PATH_COMMONCAP
```

The finite audit verifies the displayed identities; the proofs above are
dimension-uniform and do not infer a global host from the sample range.
