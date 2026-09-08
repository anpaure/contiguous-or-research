# A factor-level gap--Hall theorem and a terminal-ECO path obstruction

Date: 2026-07-31  
Status: exact all-dimension factor-decoration equivalence; exact solver-free
fixed-rotation terminal-bank path no-go at paper `n=6`; no all-dimension
decorated factor or contiguous-OR theorem

## 0. Verdict

There are two logically different central routes.

1.  The weakest Catalan-trace route does **not** require component merging.
    A decorated spanning Middle Levels `2`-factor already gives the perfect
    Boolean-diamond matching and the `Cat_m`-path lift.  For a fixed factor,
    its exact remaining decoration test is one occurrence-labelled gap--Hall
    matching, with a local binary-trace exclusion on each marked component.
2.  The stronger fixed-rotation terminal-ECO path-backbone route is false in
    general.  At paper parameter `n=6`, its component two-section has an
    articulation whose deletion leaves three nonempty components.  Hence it
    has no Hamilton path and admits no binary/ternary terminal-ECO path
    tiling.

Thus path-flow integrality remains correct **after** a component path is
exported, but the fixed-rotation terminal bank cannot always export such a
path.  This no-go does not obstruct the weakest decorated-`2`-factor target.

## 1. Exact factor-level gap--Hall formulation

Fix `m>=2`, put `Omega=[2m-1]`, and let `F` be a spanning `2`-factor of
`ML(2m-1)`.  On each factor component write

\[
 A_0,B_0,A_1,B_1,\ldots,A_{q-1},B_{q-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.                 \tag{1.1}
\]

At an `A`-occurrence and a `B`-occurrence define respectively

\[
 u_F(A_i)=B_{i-1}\cup B_i\in\binom\Omega{m+1},
 \qquad
 \ell_F(B_i)=A_i\cap A_{i+1}\in\binom\Omega{m-2}.    \tag{1.2}
\]

An **upper transversal** is a set `I` of `A`-occurrences containing exactly
one occurrence of every colour in `binom(Omega,m+1)`.  On every factor
component meeting `I`, cut the cyclic occurrence order at the members of
`I`.  The resulting open cyclic arcs are the **`I`-gaps**.  Components
disjoint from `I` contribute no gap.

Make the occurrence-labelled bipartite graph `Gamma_F(I)` as follows.

* Its left vertices are all `I`-gaps.
* Its right vertices are the colours in `binom(Omega,m-2)`.
* For every `B`-occurrence `b` lying in a gap `g`, add the labelled edge
  `(g,ell_F(b);b)`.

Parallel labels are retained because the chosen physical occurrence affects
the binary trace.

### Theorem 1.1 (componentwise gap--Hall equivalence)

The factor `F` has a componentwise Catalan decoration if and only if there
is an upper transversal `I` for which `Gamma_F(I)` has a perfect matching.
For fixed `I`, this is equivalent to the exact Hall family

\[
       |N_{\Gamma_F(I)}(X)|\ge |X|
       \qquad\text{for every set of gaps }X.           \tag{1.3}
\]

The chosen decoration is linear precisely when, on every component meeting
`I`, the occurrence-labelled perfect matching leaves at least one unmarked
occurrence and produces a binary mark word outside the cycle face

\[
 \text{all positive zero-runs have length }2,
 \qquad\text{all one-runs have odd length}.            \tag{1.4}
\]

Components disjoint from `I` are unmarked and may use either residual cross
phase.  Equivalently, if `1_C` denotes the all-one word on a component, the
forbidden trace family is

\[
 \mathcal B_{\rm cyc}(C)=\{1_C\}\cup
 \{\chi:\chi\text{ satisfies (1.4) and contains a zero}\}. \tag{1.5}
\]

#### Proof

Suppose first that a componentwise decoration is given and let `I` be its
selected `A`-occurrences.  Global upper-colour bijectivity makes `I` an upper
transversal.  Its cardinality is

\[
 |I|=\binom{2m-1}{m+1}=\binom{2m-1}{m-2},             \tag{1.6}
\]

the number both of `I`-gaps and of lower colours.  On a marked component,
selected shore types alternate.
Therefore every cyclic gap between consecutive selected `A`-occurrences
contains exactly one selected `B`-occurrence.  Match that gap to the lower
colour of this occurrence.  Global lower-colour bijectivity makes these
edges a perfect matching of `Gamma_F(I)`.

Conversely, let `M` be a perfect matching of `Gamma_F(I)` and select the
occurrence labelling each edge of `M`.  There is one selected `B`-occurrence
in every `I`-gap and every lower colour is used once.  Hence selected
occurrences alternate `A,B,A,B,...` on each marked component, while the two
turn-colour families are globally bijective.  This is exactly a
componentwise decoration.  Hall's theorem gives (1.3).  The trace statement
is the component-local binary-trace criterion, with the all-one trace
separately forbidden because it lifts to the two rail cycles.  A component
disjoint from `I` cannot contain a selected `B`: cyclic alternation would
force equally many positive `A`- and `B`-marks.  Such a component is
therefore wholly unmarked; it uses an alternating factor-edge phase and
contributes only disjoint cross edges.

For completeness, the trace law is all-dimensional.  The residual matching
makes every positive zero-run even.  A zero-run of length at least four cuts
both physical rails.  If every zero-run has length two, a rail closes around
the factor component exactly when every intervening one-run has odd length;
this is (1.4).  The all-zero word is the residual cross matching, while the
all-one word has no cross edge and gives the two rail cycles.  Hence
`B_cyc(C)` is the complete forbidden family.
\(\square\)

### Corollary 1.2 (weakest exact central target)

The central Catalan linear-matching problem is implied by

\[
 \boxed{\exists(F,I,M):
   F\text{ a spanning `2`-factor},\ I\text{ an upper transversal},\
   M\in\operatorname {PM}(\Gamma_F(I)),\
   \chi_C(I,M)\notin\mathcal B_{\rm cyc}(C)\
   \ \forall C\text{ meeting }I.}                    \tag{1.7}
\]

No component-spanning ECO tree, Hamilton voltage, fixed owner matching, or
occurrence router occurs in (1.7).  The factor-to-diamond theorem then gives
a perfect diamond matching whose physical lift is a spanning linear forest
with exactly `Cat_m` paths.

Moreover any two spanning `2`-factors are connected through `2`-factors by
an alternating-circuit packet: their red/blue symmetric difference has
equal red and blue degree at every vertex and decomposes into closed
alternating circuits.  Thus a post-glue or post-factor repair exists exactly
when some terminal factor satisfying (1.7) exists; it is not an additional
existential gate.

## 2. The fixed-rotation terminal bank

Let `[W]` denote the orbit of a Dyck word under the rooted plane-tree
rotation

\[
                 \rho(1a0b)=a1b0.                    \tag{2.1}
\]

For a Dyck word `D=1u0v` of semilength `n-1`, the three old component
classes of its fixed-rotation ECO atom are exactly

\[
 {cal C}(D)={[1u100v],\ [1u010v],\ [1v01u0]\}.       \tag{2.2}
\]

Indeed the first two lower ports already have a Dyck prefix before the
terminal zero.  Rotating the third lower port immediately after its extra
zero gives the prefix `1v01u0`.  This proves (2.2) without using the factor
enumerator.

The common physical/owner collision orientation is

\[
          1p\,10\,0v\longrightarrow1p\,0\,10v.       \tag{2.3}
\]

Consequently the collision-path terminals are precisely

\[
              {cal T}_n=\{D=1u0v:u\text{ does not end in `10`}\}. \tag{2.4}
\]

There is one such atom per collision-path component, so the whole terminal
bank is collision-independent.  The question addressed below is different:
does its **component** two-section have a Hamilton path which its binary and
ternary supports can tile?  The answer is no.

## 3. Exact `n=6` articulation

At paper parameter `n=6`, the plane-tree component classes, in the order
used below, are

\[
\begin{array}{c|l@{\qquad}c|l}
0&101010101010&7&101011101000\\
1&101010101100&8&101011110000\\
2&101010110100&9&101100101100\\
3&101010111000&10&101100111000\\
4&101011001100&11&101101110000\\
5&101011011000&12&101110011000\\
6&101011100100&13&101111100000.
\end{array}                                             \tag{3.1}
\]

Substituting the `42` Dyck words of semilength five into (2.2), imposing
(2.4), and discarding singleton supports leaves the following `28`
nontrivial atoms:

\[
\begin{array}{c|c@{\quad}c|c}
D&{cal C}(D)&D&{cal C}(D)\\ \hline
1111100000&8,13&1111010000&7,8\\
1111001000&6,11&1111000010&10,8,13\\
1110110000&5,10&1110101000&2,3\\
1110100010&5,7,8&1110011000&4,12\\
1110001100&11,10,13&1110001010&6,3,8\\
1101110000&3,11&1101101000&2,6\\
1101100010&9,5,10&1101011000&1,4\\
1011110000&13,8&1011101000&8,7\\
1011100100&11,6&1011100010&10,3\\
1011011000&10,5&1011010100&3,2\\
1011010010&5,2&1011001100&12,4\\
1011001010&4,1&1010111000&11,3\\
1010110100&6,2&1010110010&9,1\\
1010101100&4,1&1010101010&1,0.
\end{array}                                             \tag{3.2}
\]

Let `c=101010101100`, component `1`.  Deleting `c` from the two-section of
(3.2) leaves exactly the three connected sets

\[
 \{0\},\qquad \{4,12\},\qquad
 \{2,3,5,6,7,8,9,10,11,13\}.                         \tag{3.3}
\]

The only terminal atoms incident with `c` are

\[
\begin{array}{c|c}
1010101010&\{1,0\}\\
1010101100&\{4,1\}\\
1010110010&\{9,1\}\\
1011001010&\{4,1\}\\
1101011000&\{1,4\}.
\end{array}                                             \tag{3.4}
\]

Thus (3.3) is not an artefact of omitting a ternary bridge through `c`.
Table (3.2) also gives internal paths in each row of (3.3), so the
two-section itself is connected and `c` is an articulation with three
deletion components.

### Theorem 3.1 (terminal path-backbone no-go)

The fixed-rotation terminal ECO bank at paper `n=6` has no component
Hamilton path.  Consequently no selection of its binary and ternary atoms
tiles a component path, even before any downstream state or collision row
is imposed.

#### Proof

Deleting one vertex from a Hamilton path leaves at most two nonempty path
components.  Every path edge belongs to the ambient two-section, so each of
the three graph components in (3.3) would have to lie in one of those two
path components.  This is impossible.  A binary/ternary path tiling expands
each selected binary support to one path edge and each ternary support to
two adjacent path edges, and therefore would itself supply such a Hamilton
path.  Hence no tiling exists. \(\square\)

This refutes the all-`n` terminal/path-backbone conjecture by an explicit
branching obstruction.  It does **not** refute:

* connectivity of the terminal two-section for all `n`;
* a nonpath terminal incidence hypertree;
* a bank using another fixed-rotation phase or selected nonterminal atoms;
  or
* the decorated-`2`-factor target (1.7).

## 4. Exact hierarchy after the counterexample

The routes now have the following strict logical strength.

1. **Minimal central trace:** prove (1.7).  Components may remain disconnected
   and wholly unmarked components choose either residual phase.
2. **Post-glue Hamilton route:** first find a disjoint strict ECO incidence
   hypertree by any topology, then use alternating circuits to reach a
   decorated Hamilton cycle.  A terminal component path cannot be required
   uniformly because of Theorem 3.1.
3. **Repair-first private collar:** preserve one decoration and the exported
   owner/router state through every glue.  This is stronger than either
   central existence route, but it is the form capable of carrying recursive
   residence/shadow/compiler data.

Even (1.7) proves only Catalan Linear Matching.  Exact contiguous-OR equality
still requires strict residence, the full deeper-shadow tower, and the
integral compiler on one chronology.

## 5. Audit and dependencies

The solver-free audit

```text
python3 scratch/audit_catalan_terminal_eco_n6_path_cut_20260731.py
```

reconstructs (2.1)--(3.4), checks all `28` terminal supports, and emits

```text
scratch/catalan_terminal_eco_n6_path_cut_20260731.audit.json.
```

The factor-level implication uses
`MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
the post-glue equivalence uses
`MATH_THEOREM_CATALAN_POSTGLUE_REPAIR_AND_PERIOD3_SUPPORT_GATE_20260731.md`;
and the fixed-rotation support/collision laws use
`MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`.  The independent
`n=6` table agrees with the broader authenticated result in
`MATH_THEOREM_CATALAN_FIXED_ROTATION_ECO_PATH_BACKBONE_20260731.md`, which
also supplies positive nonterminal phase-selected path certificates through
`n=10`.
