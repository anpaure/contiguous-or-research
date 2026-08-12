# K17 all-minimum endpoint/socket master

Date: 2026-08-01  
Status: exact finite theorem for the stated all-minimum-cut master and its
authenticated optional socket catalogue.  It is **not** a `k=17` word, a
Hamilton-path certificate, or a lower bound on `nu(17)`.

## 1. Frozen host

The host is the authenticated rank-nine SCD forest on `[17]`:

* 24,310 owners in 4,862 components;
* 19,448 old Johnson edges;
* 8,894 componentwise minimum residence-cut patterns;
* 12,672 possible physical pieces and 25,344 orientations;
* 1,419 cuts in every selected minimum-cut family.

The minimum-cut theorem and the colourwise support threshold `18 UNSAT / 19
SAT` are proved in
`MATH_THEOREM_K17_MINIMUM_RESIDENCE_CUT_COLORED_INTERVAL_STABBING_20260801.md`.
This note adds shared orientations, endpoint capacity, and authenticated
compact facet-socket columns.

## 2. Endpoint-degree master

For every selected oriented one-seam provider, charge one outgoing endpoint
to its left piece and one incoming endpoint to its right piece.  Every piece
has capacity at most one in each direction.  A rank-ten cut colour is either
served by one selected provider or placed in a terminal residual bank.  For
each colour, at most one provider is selected.

The exact no-socket threshold is

\[
   \boxed{28\text{ residuals is UNSAT},\qquad
          29\text{ residuals is SAT}.}
\]

The SAT witness was replayed clause by clause and against all selected
patterns, orientations, arcs, and omitted colours.  The UNSAT side has a
retained DRAT proof; its trimmed proof has SHA-256
`6a2081fd1aedb2726941c9c18b5b124aa2597f27b442068b792fcfde5d1cd6c1`.

This is a degree-cap theorem, not a path theorem: it does not require every
piece to have degree one, does not enforce connectivity, and does not choose
one common source chronology.

## 3. Optional compact sockets

The authoritative v5 bank contains thirty individually authenticated
length-three compact facet sockets.  A selected socket carries, in one
column:

1. its repaired rank-ten target;
2. its three rank-nine facet owners and their extraction positions;
3. the exact required component cut options;
4. its left and right guard states and segment orientations;
5. its extra cut colours and recursively closed child colours.

The master enforces:

* socket-to-pattern implications for every required component option;
* literal existence of both endpoint segments;
* endpoint orientation and in/out capacity;
* facet-owner nonoverlap;
* guard--guard, facet--facet, and guard--facet incompatibility;
* invalidation of every ordinary provider using an extracted segment;
* provider at-most-one over ordinary arcs and sockets together;
* recursive demand for every non-self child colour.

The v5 static bank was independently replayed with zero packing, exposure,
or child-closure conflicts.

### Theorem 3.1 (v5 optional-column threshold)

For the exact master above with the thirty v5 sockets available as optional
columns,

\[
   \boxed{24\text{ residuals is DRAT-UNSAT},\qquad
          25\text{ residuals is SAT}.}
\]

The SAT witness selects five sockets,

\[
             19449,\ 19709,\ 59815,\ 64225,\ 97508,
\]

uses fourteen socket-induced extra cuts, and leaves the exact residual set

\[
\begin{split}
\{&4059,12250,15070,20203,24371,28557,28926,31162,31988,
32286,36842,40870,41215,45903,48972,57583,60643,66555,\\
&69555,69605,71658,75693,85969,86735,89968\}.
\end{split}
\]

The model contains 793,254 variables and 2,347,555 clauses.  The literal
replayer reports exactly one cut pattern for each of the 4,862 components,
1,419 selected cut colours, 1,434 ordinary provider arcs, five socket
columns, and twenty-five omissions.

The UNSAT formula contains 788,960 variables and 2,338,968 clauses.  Kissat's
84 MiB binary proof was independently checked and trimmed; the 7.3 MiB core
proof was independently replayed again:

```text
c 43521 of 2338968 clauses in core
c 65625 of 66268 lemmas in core using 11935038 resolution steps
c 744 RAT lemmas in core
s VERIFIED
```

Thus the socket columns improve the exact scoped endpoint residual from 29
to 25, but do not close it.

## 4. CEGAR round two

Adding the child-closed compact socket rows generated for the residual-25
witness improves the exact scoped threshold to `22 UNSAT / 23 SAT`.  The
residual-23 witness selects eight sockets and has been replayed literally.
The UNSAT side was independently DRAT-verified; its trimmed proof has SHA-256
`213797f236f13544c15bcaf43b0e60e4d5ad964a3b62f8717ca2b3b8df5b198d`
and its second replay transcript has SHA-256
`098a8a508f0e7c02eb50dc7aa270821e5d47b793a561f90307fff7ed872b9a78`.
This round remains a column-generation diagnostic; the v5 theorem in Section
3 is the compact proof bundle retained in the repository.

## 5. Why this still does not produce a path

The socket selector is deliberately earlier than physical path and complete
upper-deck gates.  Exact materialization exposed two successive obstructions:

* the fixed v5 thirty-socket postbank has seven rank-ten colours with no raw
  oriented seam provider;
* a v7 extension closes raw rank-ten support, but still has 100 rank-ten and
  four rank-eleven colours with no residence-extendable provider.

Any interval crossing two pieces has an adjacent endpoint-owner seam.  Hence
a rank-ten internal hole with no residence-extendable seam provider cannot be
rescued by a longer interval in a resident global word.  A Hamilton-path CNF
on either frozen bank would therefore be theorem-redundant.

That last formulation is superseded by the authenticated v7 socket census.
Every one of the 100 rank-ten extendable-zero colours now has an explicit
compact L3 socket (individual extra-cut sum 213); 99 are child-clean and the
sole child 14309 has clean socket rows.  The live gate is therefore not
pairwise socket existence or another frozen-bank seam search.  It is one
prospective joint re-selection of the old and new sockets, component
options, guards, provider survivors and physical chronology.  In fact the
published L3/L4 rows are already unit-propagation UNSAT when appended to the
immutable v7 bank: 88 targets have both choices locally dead.  See
`MATH_THEOREM_HA_K17_V7_TYPED_SOCKET_CASCADE_AND_BUFFERED_COMPRESSION_20260801.md`
for the exact typed-child and buffered-junction interface.  The
noncanonical pivot-rich geodesic packet is proved and is not an open local
lemma, although its published collar range does not itself certify the
finite k=17 junction.

Only after this prospective selector eliminates every typed rank-ten child
is it meaningful to impose one orientation per final piece, exact in/out
degrees, one path, and the ranks 11--15 accumulated-union CEGAR.

## 6. Scope exclusions

The theorem does not assert:

* connectivity or a single path;
* a common depth-three source word;
* arbitrary-width upper coverage;
* lower-compiler feasibility;
* `nu(17)=24313`, or any improved numerical upper bound for `nu(17)`.

It proves an exact threshold only inside the encoded all-minimum-cut,
extendable-one-seam, endpoint-capacity, optional-v5-socket fibre.

## 7. Reproducible artifacts

* CNF generator:
  `scratch/build_k17_allmin_support_closure_cnf_20260801.cpp`, SHA-256
  `9d1fbffb4d9235214fc5cf901629570ce053517151cbce1bd154f6407dce0fa0`.
* Independent model replayer:
  `scratch/verify_k17_allmin_support_closure_model_20260801.cpp`, SHA-256
  `a8aef70e06d777615ed55b40b0be56312f40796191948da87a28616d33767654`.
* v5 socket bank:
  `scratch/k17_m9_endpoint_degree_combined30_socket_bank_v5_20260801.tsv`,
  SHA-256
  `14e444919ef4daf6aeee1639cbe1632299193cbd8a40838c0cb652d123018697`.
* Independent v5 bank audit:
  `scratch/k17_combined30_socket_bank_v5_independent_20260801.audit.json`,
  SHA-256
  `d77531b5ad73e3631b2df739febc725635ccd96656710c4de8df587d8cba6aa7`.
* Frozen proof/model bundle:
  `scratch/k17_socketv5_threshold_20260801/`.

All CNF generation and SAT/DRAT work was run on the H100 host's CPU.  No
heavy solver was run on the local workstation.
