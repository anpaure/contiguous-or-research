# Exact all-opening primary Benders and DM-shore interface

## 0. Result and boundary

This note gives the exact lazy interface between a SAT model of the current
resident combined factor master and the accepted flat-source/common-compiler
oracle.  It does not solve the resident master and does not assert
\(\nu(17)=B(17)\).

The main quantifier is existential over physical openings.  If \(x\) is a
determinant primary assignment and \(F(x)\) is its decoded connected physical
cycle, define

\[
 \mathcal R(F,\omega)=
 \begin{cases}
  1,&\text{opening \(\omega\) has an exact maximal source, complete}\cr
    &\text{nonwrapping upper deck, and feasible exact common cap;}\cr
  0,&\text{otherwise.}
 \end{cases}
\]

The factor has source/compiler recourse exactly when

\[
                 \bigvee_{\omega\in\Omega(F)}
                    \mathcal R(F,\omega)=1,             \tag{0.1}
\]

where \(\Omega(F)\) consists of both directions at every physical cut edge.
For the present \(k=17\) cycle, \(|\Omega(F)|=2W=48{,}620\).

The first executable bridge now:

1. authenticates the determinant primary model and all factor provenance;
2. enumerates all 48,620 directed openings;
3. emits exact rooted source-failure guards;
4. if no source opening exists, emits a bounded structural primary cut and
   two independently safe incumbent no-goods;
5. otherwise returns `NEED_DEEP_ORACLE` and emits no incumbent cut.

Upper, Hall/DM, common-cap, and verified-word outcomes have a complete exact
interface below.  The accepted source/compiler pipeline supplies the fixed-
opening subproblem.  A timeout, marginal-Hall result, partial proof, or
unverified UNSAT is never promoted to a factor cut.

## 1. Determinant variables in the live master

The current compact-Horn-v3 plus rank-11 master preserves the base factor
primaries verbatim:

\[
                        x_1,\ldots,x_{35713}.            \tag{1.1}
\]

There are 232 fixed quotient edges.  Exact residual facet choice forces
exactly 1,198 primary options, giving 1,430 quotient edges.  Developing each
through \(\mathbb Z_{17}\) gives

\[
 232\cdot17=3944\text{ fixed edges},\qquad
 1198\cdot17=20366\text{ selected option edges},        \tag{1.2}
\]

and 24,310 physical edges in total.

All counter, dart, Horn-history, and rank-11 summary/pair variables are
auxiliary.  They must not occur in an unguarded semantic factor cut.  The
physical factor is a deterministic function of (1.1), the frozen marker
witness, and the opening type.  The implementation independently checks all
35,713 option-map rows, including physical intersection/union, orbit
representatives, cap representative, and voltage.

## 2. Opening selectors and guarded logic-Benders cuts

One exact extended master uses a Boolean \(a_\omega\) for every directed
physical opening, with

\[
       \sum_{\omega}a_\omega=1,
       \qquad a_\omega\Longrightarrow x_{e(\omega)}=1,  \tag{2.1}
\]

where fixed cut edges need no primary implication.  Phase copies may later
be symmetry-compressed, but the proof-safe interface enumerates them all.
Both directions must be represented unless reversal compatibility with any
new typed endpoint state is separately proved.

### Theorem 2.1 (guarded failure cube)

Let \(G_\omega=\bigwedge_{\ell\in C_\omega}\ell\) be a conjunction of
primary literals, and suppose an independently checked subproblem proves

\[
 H\wedge a_\omega\wedge G_\omega
       \Longrightarrow \neg\mathcal R(F,\omega),        \tag{2.2}
\]

where \(H\) is the hard outer master.  Then

\[
  \neg a_\omega\ \vee\!
       \bigvee_{\ell\in C_\omega}\neg\ell              \tag{2.3}
\]

is a valid lazy clause.

#### Proof

Clause (2.3) is exactly the negation of the impossible conjunction in
(2.2). \(\square\)

A failure at one opening is **not** an unguarded factor cut.  The same factor
may use another opening.  Without selectors, only a structural obstruction
to every opening or a factor-complete incumbent no-good is generally safe.

## 3. Exact all-opening fallback

Let \(x^*\) be an incumbent whose every opening has a definitive failure
certificate.  The complete primary-assignment no-good is

\[
 \Delta(x,x^*)=
   \bigvee_{j:x_j^*=1}\neg x_j
   \ \vee\!
   \bigvee_{j:x_j^*=0}x_j.                              \tag{3.1}
\]

It excludes exactly \(x^*\), so it cannot exclude a different factor which
admits another opening.

### Theorem 3.1 (selected-only marker58 cut)

On the authenticated exact-facet marker58 factor face, let
\(S^*=\{j:x_j^*=1\}\).  Then the shorter clause

\[
                     \bigvee_{j\in S^*}\neg x_j         \tag{3.2}
\]

also excludes exactly the incumbent undirected factor.

#### Proof

Every feasible factor selects exactly 1,198 option variables.  If all 1,198
members of \(S^*\) remain selected, no additional option can be selected.
The 232 fixed edges and the deterministic \(\mathbb Z_{17}\) development
then give exactly the same physical factor. \(\square\)

If constant selected cardinality or deterministic development is not
machine-replayed for a changed master, (3.2) is unauthorized and the bridge
must fall back to (3.1).  If auxiliary variables can change the factor while
the primaries remain fixed, no primary-only incumbent cut is sound.

## 4. Bounded structural source cut

For every cyclic positive coordinate run

\[
                    R=0,1^\ell,0,qquad 1\le\ell\le d,
\]

let \(B(R)\) be its \(\ell+1\) bracket/path edges: the entering edge, the
\(\ell-1\) internal edges, and the leaving edge.

### Theorem 4.1 (all-opening bracket criterion)

A connected cycle has a flat depth-\(d\) opening if and only if

\[
                       \bigcap_R B(R)\ne\varnothing,    \tag{4.1}
\]

with the intersection over all short positive runs.  If there is no short
run, every cut passes.

#### Proof

The maximal-antecedent theorem says that a linear opening is exact precisely
when it has no internal positive run of length at most \(d\).  Cutting edge
\(e\) boundary-clips run \(R\) precisely when \(e\in B(R)\).  Thus one cut
repairs every short run precisely when it belongs to (4.1). \(\square\)

### Corollary 4.2 (bounded empty-intersection core)

If (4.1) is empty, there is a subfamily of at most \(d+2\) runs whose
bracket intersection is empty, using at most

\[
                         (d+1)(d+2)                     \tag{4.2}
\]

physical edges.

#### Proof

Choose one run \(R_0\).  For every \(e\in B(R_0)\), global emptiness supplies
a run \(R_e\) with \(e\notin B(R_e)\).  The family consisting of \(R_0\)
and these at most \(d+1\) witnesses has empty intersection.  Its union has
at most \((d+1)(d+2)\) edges. \(\square\)

### Theorem 4.3 (primary structural clause)

Assume one connected degree-two physical cycle and one global cut.  Let
\(\mathcal C\) be an empty-intersection core and let \(V(\mathcal C)\) be
the nonfixed primary activators of its physical edges.  Then

\[
                  \bigvee_{j\in V(\mathcal C)}\neg x_j \tag{4.3}
\]

is globally valid for the flat-source target.

#### Proof

If every activator in (4.3) remains selected, every nonfixed support edge
remains; the fixed supports are unconditional.  Degree two forces each
bracketed owner path to remain consecutive, possibly reversed, so every
short run persists with the same bracket set.  Their bracket intersection
is empty, contradicting Theorem 4.1. \(\square\)

If all support edges are fixed, (4.3) is the empty clause on this factor
face.  The theorem is not a multicomponent forest statement: independently
opening several components gives several cuts and invalidates its premise.

For \(d=3\), (4.2) gives at most five runs and twenty physical edges.

## 5. Upper-shadow separation

For a fixed opening, absence of an upper target is deterministic and is a
terminal opening failure.  It does not by itself yield a short clause on
currently absent primaries: a new consecutive path witness is a conjunction
of several selected edges.

The exact choices are:

1. use the guarded full-opening cube (2.3);
2. introduce exact accumulated-union path/DFA witness variables and their
   provider ALO; or
3. after every opening is definitively closed, use (3.1) or (3.2).

No clause saying merely “select one currently absent edge” is asserted.

## 6. Exact DM-shore strengthening

Fix an opening \(\omega\) and build the literal short-cell graph from the
maximal antecedent.  Let \(A\) be a deficient left shore, let
\(N=N(A)\), and put

\[
                          \delta=|A|-|N|>0.             \tag{6.1}
\]

For every occurrence-labelled cell \(C\notin N\), define an exact activation

\[
 q_{\omega,A,C} \Longleftrightarrow\!
   \bigvee_{S\in A}operatorname{Cand}_\omega(S,C),     \tag{6.2}
\]

where `Cand` is the full literal predicate

\[
 S\subseteq U_C,qquad M_C\subseteq S,qquad
 S\cap P_p\ne\varnothing\quad(p\in C).                 \tag{6.3}
\]

### Theorem 6.1 (guarded DM repair row)

Every Hall-feasible descendant using opening \(\omega\) satisfies

\[
  a_\omega\Longrightarrow
       \sum_{C\notin N}q_{\omega,A,C}\ge\delta.        \tag{6.4}
\]

#### Proof

The old cells in \(N\) contribute at most \(|N|\) distinct neighbors to
\(A\).  Hall feasibility needs at least \(|A|\) distinct neighbors.  Thus at
least \(\delta\) cells outside \(N\) must acquire an actual neighbor from
\(A\).  Losing old neighbors only strengthens the requirement. \(\square\)

Equation (6.4) is valid only with exact activations (6.2)--(6.3).  An
envelope-only, support-only, or scalar DM deficit is not a primary cut.
Without the activation extension, the safe row is the guarded factor cube
(2.3), or the all-opening fallback of Section 3.

## 7. Common-cap and terminal statuses

The exact fixed-opening common-cap CNF from the accepted pipeline is the
recourse subproblem after marginal Hall.  Its outcomes are classified as
follows.

| Status | Terminal for this opening? | May support global no-good? |
|---|---:|---:|
| `SOURCE_FAIL` | yes | only after every opening, or via Theorem 4.3 |
| `UPPER_FAIL` | yes | only after every opening or a guarded cube |
| `HALL_FAIL` | yes | only after every opening or exact (6.4) |
| `COMMONCAP_UNSAT_VERIFIED` | yes | only after proof/core verification |
| `COMMONCAP_UNKNOWN` | no | no |
| `PASS_WORD_DUAL_VERIFIED` | success | emit word; emit no cut |

An UNSAT result is usable only after the exact CNF, assumptions, and proof
are independently bound and verified.  A timeout, partial proof, or
unverified solver line is `COMMONCAP_UNKNOWN`.  If even one opening remains
unknown and no opening passes, no incumbent-excluding global clause is
authorized.

For SAT, the model is replayed clause-by-clause, decoded to a literal word,
checked against the exact \(D^3\) owner row, and then subjected to both
exhaustive \(2^{17}-1\) interval-OR scans before atomic emission.

## 8. Reversal and physical-opening scope

For the untyped flat compiler, reversing a linear opening sends

\[
 P'_p=P_{L-1-p},
\]

mirrors every short cell, preserves every accumulated-owner union, and maps
the common-cap CNF and a word to their reversals.  Thus the two directions
of one cut are isomorphic.  The bridge nevertheless exports both, with
swapped directed cut endpoints.  This prevents accidental use of the
reversal quotient after a future typed endpoint, collar, or phase state is
added.

## 9. Executable bridge

The implementation is

```text
scratch/build_ad_k17_opening_benders_primary_interface_20260802.cpp
```

with interface

```text
bridge MODE MAP.tsv MODEL [CNF|-] WITNESS.tsv BASE_COUNT OPEN_EDGE
       FACTOR.tsv PREFIX
```

`full-model` requires a complete assignment and replays every clause of the
given combined-master CNF.  `sparse-control` is explicitly restricted to the
frozen positive-primary calibration model and makes no full-CNF claim.

The bridge independently verifies:

- every option map row and its orbit/voltage semantics;
- the 232 fixed quotient rows reconstructed from the first 58 marker bases
  and opening type 3;
- all 1,198 selected primaries and their 20,366 developments;
- all 3,944 fixed physical edges;
- exact rank-8 facets, degree-two rank-9 owners, complete rank-10 caps, and
  one physical cycle;
- all 48,620 directed openings.

It exports the full primary assignment, selected-primary list, physical-edge
binding, all openings, one exact rooted source guard per source-failing
opening, the bounded source core, the selected-factor no-good, the full
assignment no-good, and a downstream status schema.  If any source opening
exists, none of the three incumbent clauses is emitted.

The numeric `edge_id` in a rooted row is incumbent-local and diagnostic.
The persistent host-master key is the exported directed physical endpoint
pair `cut_owner_a -> cut_owner_b` (equivalently its authenticated
orbit/phase address).  A rooted row becomes a clause only after a host
variable for that stable key is linked to the corresponding edge activator
and exactly one opening is selected.

The independent verifier

```text
scratch/verify_ad_k17_opening_benders_primary_interface_20260802.cpp
```

does not read the quotient map, witness, or model.  From the factor and
exported binding alone it reconstructs the cycle and short runs, replays all
48,620 opening rows and rooted guards, and checks the three clauses
literal-for-literal.

## 10. Exact controls

### 10.1 k15 positive

The accepted k15 flat-source/common-cap control is inherited as an explicit
pass-through calibration; this hardcoded k17 primary bridge is not run on a
k15 map.  The inherited control remains positive:

```text
exact Hall                    16383 / 16383
common-cap CNF/model          PASS
dual exhaustive coverage     32767 / 32767
```

It emits the independently verified universal word and no Benders cut.

### 10.2 final2397 negative

The authenticated inputs have hashes

```text
factor   eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb
model    9aa9c8137b4b90508aa255536a6f683bfa448b60de497b498f7119e432eb24ec
map      7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
witness  88fe38dc68ca3345318e142386a389fe7ea3eb56794ede1ed4e01494c7b88403
```

The bridge independently obtains 2,397 short positive runs, zero of 48,620
source-valid directed openings, and minimum residual count 2,395.  Its
inclusion-minimal two-run core is

```text
101166 - 101165 - 102157 - 109837 - 109838
128112 -  62577 -  62569 -  64553 -  64808
```

Both are coordinate-zero `0,111,0` paths.  Their eight physical bracket
edges are disjoint.  Two are fixed protected edges; the remaining six map
exactly to primaries

\[
             \{7604,10293,10514,13179,15783,15802\}.
\]

Therefore the exact structural clause is

```text
-7604 -10293 -10514 -13179 -15783 -15802 0
```

It is substantially stronger than the independently emitted 1,198-literal
selected-factor fallback and the 35,713-literal full-assignment fallback.
The independent verifier replays all 48,620 openings and all three clauses.

### 10.3 Frozen implementation package

The immutable local package is

```text
scratch/ad_k17_opening_benders_primary_interface_v4_20260802/
```

with manifest SHA-256

```text
feabd0d4b7e254a28815179ccce9661cc0662d9cf3a0cbe683a162c7ed01415d
```

The O3 build has empty warning logs.  Source/binary hashes are

```text
main source       63e43380a14c970249ee73890e3b620a6cf0af5dfd71247d8f6954a53059d4e7
main binary       a7502eee26df4289afef435559200c6fc26cfb478ec1d8392d1c68862b8b18bd
verifier source   3d25b015cb5f2a97ec0c6ceb9f1011478dc31b710f65ed5a45efc67e608ddbdd
verifier binary   616572d8b020b44dfe3b90b88dd02222c2e191aab72ed99e1c29cf047c2426b7
```

Principal and independent audit JSON hashes are

```text
5928b87d1f5d13ea494e5ef809848d44962c4f0577f94c5479070bb0250ec5ab
5401bbbba132892c178683d0c7eec4c532ce8078913c6f9c77c7818aa0c4538d
```

## 11. Precise remaining boundary

The determinant binding, all-opening quantifier, source structural cut, and
fallback factor cuts are closed.  For the first resident V2 SAT model,
positive residence should make every source cut pass, but the bridge will
still replay them.  The next run must then feed every surviving opening to
the accepted exact upper/Hall/common-cap oracle, use guarded DM rows only
with exact candidate activations, and retain `UNKNOWN` unless every opening
is terminally classified or one literal word passes dual verification.
