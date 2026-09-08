# Fail-closed maximal flat-source/compiler pipeline

## 0. Result and exact scope

This note closes the *verification pipeline* needed after a future connected,
residence-capable middle factor is found.  It does not prove that such a
factor exists.

Fix integers

\[
  1\le d<r<k,\qquad W=\binom{k}{r},\qquad L=W+d.
\]

For a chosen directed linear opening

\[
  T=(T_0,T_1,\ldots,T_{W-1})
\]

of a simple Johnson cycle on all rank-\(r\) owners, the pipeline does the
following, in this order.

1. It constructs and directly verifies the unique pointwise-maximal flat
   \(D^d\)-antecedent.
2. It verifies the complete nonwrapping accumulated-owner upper deck.
3. It enumerates the exact literal incidences between every strict-lower
   target and every source interval of length at most \(d\).
4. It computes a maximum matching, a canonical Hall shore, and the full
   Dulmage--Mendelsohn decomposition of that incidence graph.
5. Only after marginal Hall succeeds, it emits an exact common-cap CNF.
6. A SAT model is accepted only after every variable and every DIMACS clause
   is replayed.  The decoded word must induce exactly the chosen owner order.
7. A word is written atomically only after two exhaustive, independently
   organized interval-OR scans both cover all \(2^k-1\) nonempty masks.

The implementation is factor-parameterized for \(k\le20\).  Its factor mode
intentionally requires one connected, simple, exact-lower-facet,
rank-\((r+1)\)-cap-complete degree-two factor.  It is not a multicomponent
chronology compiler.  One passing opening proves a linear flat antecedent;
it does **not** by itself prove cyclic residence.  Protected-bank provenance,
nonflat sources, and UNSAT proof checking remain outside this theorem.

## 1. The maximal antecedent theorem

For \(0\le p<L\), define

\[
 P_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i.       \tag{1.1}
\]

Here and below, an empty index range never occurs.

### Theorem 1.1 (maximal flat antecedent)

There is a word \(A=(A_0,\ldots,A_{L-1})\) of nonempty masks satisfying

\[
  D^dA=T,
  \qquad (D^dA)_i=\bigcup_{p=i}^{i+d}A_p,               \tag{1.2}
\]

if and only if

\[
  P_p\ne\varnothing\quad(0\le p<L),                    \tag{1.3}
\]

and

\[
  \bigcup_{p=i}^{i+d}P_p=T_i\quad(0\le i<W).            \tag{1.4}
\]

When these conditions hold, \(P=(P_p)_p\) is itself a valid antecedent and
is the unique pointwise-largest one: every other antecedent satisfies
\(A_p\subseteq P_p\) for every \(p\).

#### Proof

If (1.2) holds and \(p\in[i,i+d]\), then \(A_p\subseteq T_i\).  Intersecting
over all owner windows containing \(p\) gives \(A_p\subseteq P_p\).  Thus
nonempty \(A_p\) implies (1.3), and

\[
 T_i=\bigcup_{p=i}^{i+d}A_p
     \subseteq\bigcup_{p=i}^{i+d}P_p
     \subseteq T_i,
\]

which proves (1.4).  Conversely, (1.3)--(1.4) say exactly that \(P\) is a
nonempty word with \(D^dP=T\).  The first argument proves maximality. \(\square\)

### Corollary 1.2 (run/opening criterion)

For a linear Johnson owner path and \(d<r\), all \(P_p\) are automatically
nonempty.  Condition (1.4) holds exactly when every *internal* positive run
of every coordinate in the owner trace has length at least \(d+1\).

For a cyclic trace, a positive run of length \(\ell\le d\) is repaired by a
linear opening exactly when the cut lies in one of its \(\ell+1\) bracket
edges.  Hence the exact status of every directed physical opening can be
computed by the bracket-incidence count.  Direct construction of (1.1) for
the selected cut is used as an independent assertion of the run theorem.

#### Proof

For coordinate \(x\), \(x\in P_p\) precisely when every owner in the clipped
backward window at \(p\) contains \(x\).  An internal positive run supplies a
carrier position for all its owner rows exactly when its length is at least
\(d+1\).  Prefix and suffix runs use the clipped windows.  On a cycle, a cut
turns a run into boundary runs precisely when it meets a bracket edge.
The exact size of an adjacent intersection is not needed here.  For
nonemptiness it suffices that every clipped window has at most \(d+1\le r\)
owners along a Johnson path, whose successive deletions cannot remove all
\(r\) initial elements. \(\square\)

The final sentence uses only \(d<r\): along \(t\le d\) Johnson steps at most
\(t\) elements of the first owner can disappear, so an intersection of
\(t+1\) consecutive owners has size at least \(r-t>0\).

## 2. Exact separation of short and long cells

### Theorem 2.1 (accumulated-union identity)

Let \(A\) be any antecedent with \(D^dA=T\).  For every source interval
\([a,b]\) of length at least \(d+1\),

\[
  \bigcup_{p=a}^{b}A_p
    =\bigcup_{i=a}^{b-d}T_i.                             \tag{2.1}
\]

Every interval of length at most \(d\) is contained in at least one owner
window \([i,i+d]\).  Consequently:

- a strict-lower target, of rank less than \(r\), can occur only in a source
  interval of length at most \(d\);
- all middle targets are the length-\((d+1)\) owner windows;
- all strict-upper targets are present exactly when they occur in the
  nonwrapping consecutive-union deck of \(T\).

#### Proof

Taking the union of (1.2) for \(i=a,\ldots,b-d\) gives exactly the source
positions \(a,\ldots,b\), proving (2.1).  A short interval lies in an owner
window, so its OR is a subset of a rank-\(r\) owner.  Conversely every long
interval contains an owner window and hence has rank at least \(r\). \(\square\)

This theorem is why the upper audit must be opening-specific and
nonwrapping.  Cyclic upper completeness alone is not enough for a linear
word.

## 3. Exact literal short-cell incidence

Assume Theorem 1.1 passes.  Let \(C=[a,a+\ell-1]\), where
\(1\le\ell\le d\), and define

\[
 U_C=\bigcup_{p\in C}P_p.                               \tag{3.1}
\]

For every owner bit \(x\in T_i\), let its maximal carrier set be

\[
 H_{i,x}=\{p\in[i,i+d]:x\in P_p\}.                      \tag{3.2}
\]

This is a nonempty interval.  Define the bits forced into cell \(C\) by

\[
 M_C=\{x:\text{ for some }i,\ x\in T_i\text{ and }H_{i,x}\subseteq C\}.
                                                                    \tag{3.3}
\]

### Theorem 3.1 (one-cell realizability)

For a nonempty strict-lower target \(S\), there exists an antecedent which
agrees with \(P\) outside \(C\), still induces \(T\), and has OR exactly
\(S\) on \(C\), if and only if

\[
  S\subseteq U_C,\qquad M_C\subseteq S,\qquad
  S\cap P_p\ne\varnothing\quad(p\in C).                 \tag{3.4}
\]

#### Proof

Necessity is literal.  Every letter inside \(C\) is a nonempty subset of
\(P_p\) and of the cell OR \(S\), giving the first and third conditions.
If all possible carriers of an owner bit lie in \(C\), preserving that bit
forces it into \(S\), giving the second.

For sufficiency, set \(A_p=P_p\cap S\) inside \(C\) and \(A_p=P_p\)
outside.  The third condition makes every letter nonempty.  The first makes
the cell union equal \(S\).  For each owner bit, either a carrier remains
outside \(C\), or all carriers lie inside and (3.3)--(3.4) retain it.  Thus
\(D^dA=T\). \(\square\)

The exact incidence graph has every nonempty rank-less-than-\(r\) mask on
the left and every occurrence-labelled short cell on the right.  Its right
side has exactly

\[
  \sum_{\ell=1}^{d}(L-\ell+1)
   =dL-\binom d2                                           \tag{3.5}
\]

vertices.  An edge is present if and only if (3.4) holds.  This is the
literal graph; the former envelope-only relaxation is not used.

## 4. Hall, DM, and the simultaneous common-cap gate

A left-perfect matching in the graph of Section 3 is necessary, because two
different target values cannot be assigned to one literal cell.  The
pipeline computes:

- a maximum matching by Hopcroft--Karp;
- the canonical alternating-reachable deficient Hall shore;
- plus, minus, and balanced core regions;
- the matched-edge-contracted alternating SCC decomposition.

This Hall/DM result is only the exact *one-cell projection*.  Overlapping
cells still share source letters, so perfect Hall is not sufficient.

For simultaneous feasibility introduce \(x_{p,b}\) for every
\(b\in P_p\), and one provider variable \(y_{S,C}\) for every exact edge.
The CNF contains exactly these clause families:

1. \(\bigvee_{b\in P_p}x_{p,b}\) for every source position \(p\);
2. \(\bigvee_{p=i}^{i+d}x_{p,b}\) for every \(b\in T_i\);
3. \(\bigvee_Cy_{S,C}\) for every strict-lower target \(S\);
4. \(y_{S,C}\Rightarrow\neg x_{p,b}\) for \(p\in C\) and
   \(b\in P_p\setminus S\);
5. \(y_{S,C}\Rightarrow\bigvee_{p\in C}x_{p,b}\) for
   \(b\in S\setminus M_C\).

Bits in \(M_C\) are supplied by the global owner-restoration clauses because
all their carriers lie in \(C\).  An explicit at-most-one constraint on a
cell is unnecessary: if two distinct targets selected the same cell, these
clauses would force that cell's OR to equal two different masks.

### Theorem 4.1 (CNF exactness)

The common-cap CNF is satisfiable if and only if there is one nonempty word
\(A\), with \(A_p\subseteq P_p\) and \(D^dA=T\), in which every strict-lower
target occurs in an occurrence-labelled short cell.

#### Proof

Given a model, let \(A_p=\{b:x_{p,b}=1\}\).  Clauses 1--2 give nonemptiness
and the exact owner row.  For a selected provider, clauses 4--5 and the
forced-bit argument above make its OR exactly \(S\).  Conversely, select one
actual witnessing cell for every target in a valid word.  Its letters and
witnesses satisfy all five families. \(\square\)

## 5. Universal-word and emission theorem

### Theorem 5.1 (fail-closed completion)

Suppose a chosen opening passes Theorem 1.1, its accumulated-owner deck
contains every strict-upper target, and its common-cap CNF has a model that
passes literal clause replay.  Then the decoded word covers every nonempty
mask.

#### Proof

The CNF supplies all strict-lower targets.  Its \(D^d\) row supplies every
rank-\(r\) target exactly once because \(T\) is the complete middle layer.
Theorem 2.1 transports the complete accumulated-owner deck to source
intervals and supplies all strict-upper targets. \(\square\)

The implementation does not rely on this implication when emitting a word.
It additionally performs both of the following exhaustive checks over all
nonempty masks:

- a direct scan over every interval start and end;
- a dynamic scan of all distinct OR-frontier states ending at each position.

The two coverage bitsets must agree mask-for-mask and both must contain all
\(2^k-1\) nonempty masks.  The decoded word must also be nonempty,
envelope-contained, and have derivative exactly \(T\).  Only then is it
written through a no-overwrite temporary file and atomic rename.

This atomicity is per word file, not a transaction over every diagnostic
TSV/JSON sidecar.  An interrupted post-emission diagnostic write can leave a
mathematically verified but provenance-incomplete orphan word.  Promotion
therefore additionally requires the frozen package manifest and independent
word-verifier PASS; this caveat cannot create an invalid emitted word.

## 6. Frozen implementation contract

The main implementation is

`scratch/build_ad_exact_source_compiler_pipeline_20260802.cpp`.

Its strict interfaces are:

```text
factor K R D FACTOR PREFIX [CUT=-1] [REVERSE=0] [EMIT_CNF=0]
       [MODEL=-] [OUTPUT_WORD=PREFIX.verified.word]

word   K R D WORD PREFIX [EMIT_CNF=0]
       [OUTPUT_WORD=PREFIX.verified.word]
```

Factor TSV rows are

```text
color_mask  owner_a  owner_b  cap_mask  protected
```

with literal tab separators.  The loader rejects wrong ranks, wrong declared
intersection/union, parallel edges, repeated/missing facets, owner degree
different from two, a missing rank-\((r+1)\) cap, and more than one physical
component.  It canonically starts at the least owner and chooses its lesser
neighbor first.  Both orientations and all \(W\) cuts are then scanned.

If no opening passes, no cell graph, CNF, or word is emitted.  If a model is
provided, the same run must first regenerate the CNF; the model must contain
an authenticated SAT line, assign every CNF variable consistently, and
satisfy every regenerated clause.  Hall success without a model receives
the deliberately nonterminal status `PASS_MARGINAL_HALL_COMMON_CAP_OPEN`.

The independent final verifier is

`scratch/verify_ad_exact_source_compiler_word_20260802.cpp`.  It excludes the
factor parser, graph, matching, DM, CNF, and solver logic.  From a word and
frozen owner TSV it independently checks the exact middle layer, maximal
antecedent, \(D^d\) replay, and both exhaustive interval-OR scans.

## 7. Frozen controls

The immutable package is

`scratch/ad_k17_exact_source_compiler_pipeline_v2_20260802/`.

Its `SHA256SUMS` file has SHA-256

`e537bd5990cfe495bf3073efb8cb104c11407b7d4a5494a48875a6b59f62d72d`.

The O3 build used GCC 13.3.0 with `-std=c++20 -O3 -Wall -Wextra
-pedantic`; both warning logs are empty.  Main source and binary hashes are

```text
7f404855d3abb50a07e7fe13d1d9daf92fca00f878ca33913db1b7958e8945ba  source
112f65ad64c711ee1259a17393e6051b7743a275de423c1b9c8b6cf10af18e0d  binary
```

The independent verifier source and binary hashes are

```text
3420cc56fcfaf1dca87dc96f9329955f0c749a29e60a2e364a531716db19ea1f  source
e8997a553b8c567677fae1bdb27a6e02041bb27199228bac67338755c80016ed  binary
```

### 7.1 Positive control: authenticated exact k15 word

Input `answers/k15.word`, SHA-256
`f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b`,
passes with:

```text
owners                         6435
source length                  6438
maximal-envelope ranks         5^6432, 6^2, 7^2, 8^2
strict-lower targets           16383
short cells                    19311
exact candidate incidences     137238
zero candidates                0
maximum matching               16383
common-cap variables/clauses   169440 / 621905
dual exhaustive coverage       32767 / 32767 in each scan
```

The full generated assignment satisfies every CNF clause and decodes back
to the capped word.  The emitted maximal-cap word has SHA-256
`017f05fa1b4a642688c246064d303d70d267683aca21befafd78bf1decd8dea3`.
It need not equal the historical input word; the independent verifier gives
`PASS_INDEPENDENT_EXHAUSTIVE_WORD_REPLAY`.  Principal and independent audit
JSON hashes are respectively

```text
cb1f5a6cedebdb52cbefdd103e164e9ee3c385054b97c8f45ad8f5486a1ab248
9af3c323b4a53334425a1a7bea4fe111beafdeaa72c81cc01af7e89e38f2bf8c
```

### 7.2 Negative control: authenticated final2397 k17 factor

The factor SHA-256 is
`eba52226952cda38d74e98fc7463f54640b0b59736ff88fc2949c8f0c02de1eb`.
All \(2W=48{,}620\) directed openings were scanned.  Exactly zero pass; the
minimum remaining internal short-run count is 2,395.  The status is
`NO_EXACT_OPENING`, and the package contains no incidence graph, CNF, model,
or output word for this control.  Its principal audit JSON has SHA-256

`5a85c84a9b87642e40bd534de46ef37b177b12f7d32ed345a3bbbe81bd89de20`.

This is a fail-closed negative control, not a statement about nonflat
compilers or a different residence-clean factor.

## 8. Independent audit boundary

Independent adversarial audits checked the opening/run calculation,
maximal-source equivalence, interval identity, mandatory-carrier predicate,
Hall shore and DM arithmetic, CNF exactness, complete model/clause replay,
decoded owner replay, both exhaustive scans, and atomic no-overwrite output.
No blocking error was found.

The live gate is therefore cleanly separated.  A future V2 factor must first
pass a chosen physical opening, then the nonwrapping upper deck, exact
short-cell Hall/DM, and the common-cap model.  Nothing in this pipeline
asserts that residence, protected marker semantics, or higher shadows are
preserved by the search that produced that factor; those are authenticated
input conditions or separately replayed gates.
