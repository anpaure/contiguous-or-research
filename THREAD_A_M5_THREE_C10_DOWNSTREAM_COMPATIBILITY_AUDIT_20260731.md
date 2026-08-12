# Downstream-state audit of the synchronized `m=5` three-`C10` repair

Date: 2026-07-31  
Status: exact finite compatibility theorem and exact whole-path residence
obstruction; no all-`m` repair-packet theorem

## 0. Verdict

The synchronized three-`C10` packet is a genuine positive central Catalan
base.  The frozen forced-port decoration is leaf-peelable, not merely
palette-perfect: it produces an exact `42`-path Catalan linear matching on
`J(10,5)`, and the two standard labels retain their private **gap**
attachments.

It is not, however, an accepting instance of the full normalized recursive
state from items 2170--2179.  Three distinctions are decisive.

1. The two displayed private paths are gap-neighbourhood attachments.  They
   are not the occurrence-labelled physical endpoint sockets of the
   gain--Brauer law.
2. The repair changes the old component-tree geometry.  After the packet,
   either standard hexagon alone joins the two repaired components, while the
   second hexagon is a Hamilton-neutral transparent switch.  Thus the audit
   supplies two alternative private one-connector faces, not a two-label
   aligned component--gap basis.
3. Most strongly, the literal `42` paths contain `31` coordinate one-runs of
   length two bounded by zeroes strictly inside a path.  For `k=10`, where
   the flat-carrier depth is `d=2`, these runs survive every orientation and
   ordering of the intact paths and violate residence.  No endpoint socket
   matching can repair them.

Thus the correct conclusion is

> synchronized palette repair + private gap gluing succeeds at `m=5`, but
> even after a colour-injective, all-depth endpoint closure, an interior
> physical rethread remains necessary before residence and the common lower
> compiler can be imposed.

## 1. The exact central object

Let `C*` be the repaired Hamilton cycle in `ML(9)` and let `M*` be the
forced-port perfect matching in its augmented occurrence graph.  Write

\[
 C^*=(A_0,B_0,A_1,B_1,\ldots),
 \qquad |A_i|=4,\quad |B_i|=5,\quad
 A_i\subset B_i\supset A_{i+1}.
\]

Adjoin the tenth point `infinity`.  Every selected rank-4/rank-6 diamond
`(L,U)` has `U-L={a,b}` and lifts to the Johnson edge

\[
                 (L+a)(L+b)\in E(J(10,5)).          \tag{1.1}
\]

The selected diamonds consist of the selected `A`-turns, selected `B`-turns
and the forced residual cross matching.  The frozen matching has order
`210`, selects `84` occurrences on each rail, and includes all twelve ports
of the two standard hexagons.

### Theorem 1.1 (literal Catalan lift)

The lift `F*` of `M*` has

\[
 |V(F^*)|=\binom{10}{5}=252,\qquad
 |E(F^*)|=\binom{10}{4}=210.                         \tag{1.2}
\]

Every rank-4 intersection and every rank-6 union occurs exactly once.
Moreover, `F*` is a forest, hence has exactly

\[
                   252-210=42=\operatorname{Cat}_5  \tag{1.3}
\]

path components.  Its degree histogram is

\[
                         0^3,1^{78},2^{171},       \tag{1.4}
\]

and its path-order histogram is

\[
1^3 2^2 3^{11}4^8 5^2 6^1 7^4 8^3 9^2
11^1 12^1 13^2 16^1 29^1.                           \tag{1.5}
\]

#### Proof

The augmented matching is perfect on the `210` lower and `210` upper
resources, so (1.1) gives `210` distinct Johnson edges and both immediate
palettes exactly once.  Every rank-5 set appears once in the middle-levels
lift.  The independently reconstructed binary trace is on the forest side
of the exact one-cycle criterion.  Euler's identity then gives (1.3).
Literal degree and component traversal gives (1.4)--(1.5).  No inference
from turn-surjectivity is used.  \(\square\)

## 2. What is genuinely leaf-peelable and private

With the same forced matching, independently toggling the two standard
hexagons gives the following component cube:

\[
\begin{array}{c|c}
 (0,0)&120+132\\
 (1,0)&252\\
 (0,1)&252\\
 (1,1)&252.
\end{array}                                          \tag{2.1}
\]

The four gap-colour graphs have respectively `107,109,109,111` edges.
Direct leaf peeling removes every one of their `84` matched gap-colour
pairs, leaving no core.  Equivalently, every graph is a forest with a unique
perfect matching.  The binary trace is on its forest side in every
component of every state.

The full occurrence census around the two owner triples is exactly

\[
 [82]-g_{83,340}-[84]-g_{85,90}-[88],
 \qquad
 [50]-g_{51,308}-[52]-g_{53,58}-[56],                \tag{2.2}
\]

with no additional gap meeting either triple.  The two triples are
disjoint, and all thirty vertices used by the three `C10` circuits are
disjoint from the twelve standard ports.  This proves the private
gap-attachment claim.

There are two scope qualifications.

* In the `(0,0)` state, the `132`-vertex component has `22` zero-runs, all
  of length two, and no literal protected `0^4` guard.  Its trace is still a
  forest because an even marked run breaks the unique cycle face.  Future
  composition may therefore carry the exact trace automaton, but may not
  pretend that this component has a persistent literal `0^4` witness.
* Equation (2.1) shows that the repaired preparation no longer has the old
  three-component/two-tree-edge geometry.  To enter the private/aligned
  two-matroid face, freeze the three-`C10` packet and choose either one of
  the two standard hexagons as the sole component connector.  The audit does
  not prove that both labels form an aligned component--gap basis.

The stronger strict trace-run row of item 2176 fails outright.  Each of the
three Hamilton states has zero-run histogram `2^38 4^2` and also has odd
one-runs.  The two `(0,0)` components likewise contain length-two zero-runs
and odd one-runs.  This does not contradict binary forestness: the latter
only needs one nontransmitting run somewhere, while the strict row requires
every zero-run to have length at least four and every one-run to be even.

The original/repaired augmented occurrence graphs have common matching
order `197`.  Relative to the final forced matching, the symmetric
difference consists of thirteen vertex-disjoint augmenting paths, with
vertex-length histogram

\[
                         4^{11}6^1 16^1,             \tag{2.3}
\]

and four alternating 4-cycles.  This proves the bounded **unpaired
occurrence-linkage** row.  It does not identify a physical endpoint pairing,
a gain, or a lower-envelope compiler linkage.

## 3. Exact internal deeper-shadow ledger

Orient each path in (1.5) arbitrarily.  For a path
`P=(X_0,...,X_(s-1))`, define its internal width-`r` upper and lower
families by unions and intersections of consecutive `r` vertices.

### Lemma 3.1 (fragment protection)

Arbitrarily orienting and concatenating the forty-two paths preserves every
internal interval witness.  More generally, if a cyclic order is cut at
`s` adjacencies and its fragments are reordered or reversed, then at depth
`q` at most `sq` old `(q+1)`-windows and at most `sq` new windows cross the
old and new cuts.  Every target with a cut-avoiding witness survives.

#### Proof

Reversal preserves the union and intersection of a fixed interval.  Every
interval wholly inside a retained fragment therefore remains a consecutive
interval with the same value.  A fixed cut belongs to exactly `q` cyclic
windows of width `q+1`; summing over the cuts proves the bound.  \(\square\)

For `F*`, the exact internal missing masks are

\[
\begin{array}{c|c|c}
q&\text{upper rank }5+q&\text{lower rank }5-q\\ \hline
1&\varnothing&\varnothing\\
2&\{\mathtt{0ef},\mathtt{0fd}\}&\{\mathtt{281}\}\\
3&\{\mathtt{0ff}\}&\varnothing\\
4&\varnothing&\varnothing\\
5&\varnothing&\varnothing.
\end{array}                                          \tag{3.1}
\]

These are literal ten-bit masks.  Thus a socket closure has only four deep
targets to add; it cannot lose any target already certified internally.

## 4. Physical sockets and all-depth flag support

The endpoint graph of `F*` has `84` occurrence ports and `297` legal
cross-component Johnson socket pairs.  Port degrees range from `4` to `13`.
Exactly `234` unordered pairs of path components are adjacent, with socket
multiplicity histogram

\[
                         1^{177}2^{54}4^3.            \tag{4.1}
\]

A literal forty-two-socket perfect matching has been checked whose union
with `F*` is one Hamilton cycle.  Its connector lower colours are pairwise
distinct, and so are its connector upper colours.  Since the forest already
contains each immediate colour exactly once, the complete cyclic carrier
has the cap-two profile

\[
                             1^{168}2^{42}             \tag{4.2}
\]

on each shore.  Thus both connected degree-two topology and two-shore
connector injection pass at the final repaired state.

The same literal replay gives a stronger flag result.  The cyclic closure
covers every upper union and lower intersection at depths `q=1,...,5`.
Among its `252` possible edge cuts, exactly `46` give a linear order which
still covers the entire tower at every depth.  Exactly `39` of these cut a
connector rather than a protected forest edge, so they preserve all
forty-two path blocks intact.  In particular, the connector seams jointly
supply all four masks in (3.1).

This is not yet a recursively private gain--Brauer certificate.  The
displayed connector set uses lower colours `564=infinity+52` and
`594=infinity+82`, one from each private owner bank.  Scalar cap two has
been checked by (4.2), but transport of the same occurrence-labelled
pairing and resources through the three intermediate `C10` states and the
four standard-glue states is absent.  Moreover:

* final connected topology and two-shore connector injection: **proved**;
* final all-depth upper/lower flag support: **proved**, with `46`
  all-depth-support linear openings, `39` of them at connector edges;
* recursively private pairing/resource transport: **open**;
* gain--Brauer transition through the three intermediate `C10` states:
  **not represented by the frozen artifact**;
* nontrivial primitive voltage: **not tested** (the present quotient has
  `h=1`, where voltage is vacuous).

The gap paths (2.2) must not be called physical endpoint sockets without
this qualification.

## 5. Exact whole-path residence obstruction

For `k=10`, a depth-two erosion source requires every internal coordinate
one-run in the middle chronology to have length at least three.  This is the
coordinatewise necessary part of `D^2A=T`.

### Theorem 5.1 (no intact-path compiler)

No chronology obtained only by orienting and concatenating the forty-two
paths of `F*` satisfies depth-two residence.

#### Proof

Inside the path interiors, the positive coordinate-run histogram is

\[
 2^{31}3^{10}4^{24}5^3 6^9 7^1 8^4 10^2.           \tag{5.1}
\]

The thirty-one length-two runs are bounded by zeroes strictly inside their
paths and occur in eighteen distinct paths.  Their coordinate multiplicities
are

\[
                         (5,5,2,3,3,3,3,3,3,1).     \tag{5.2}
\]

Path reversal preserves such a bounded run, and path concatenation changes
only endpoint runs.  Hence every intact-path closure retains all thirty-one
violations of the run-at-least-three condition.  \(\square\)

The lower erosion-envelope SDR is therefore not merely unaudited on this
face: its prerequisite `D^2A=T` is impossible.  Any compiler-ready repair
must change path interiors.  The colour-injective all-depth endpoint closure
of Section 4 cannot fix this obstruction.

## 6. Correct theorem boundary

The synchronized three-`C10` packet proves all of the following at `m=5`:

1. both immediate palettes and the augmented alternating SDR;
2. a leaf-peelable gap forest with unique matching;
3. the two private gap tubes;
4. bounded common-core occurrence linkage;
5. an exact `42`-path Catalan linear matching;
6. a colour-injective connected physical socket closure; and
7. a complete upper/lower flag tower after any of `46` all-depth-support
   linear openings,
   including `39` connector openings.

It does not prove the aligned two-label component-tree face, the strict-run
state, recursively private pairing transport, gain transport, residence, or
the common lower compiler.  The smallest constructive continuation is therefore
an **interior rethread** which simultaneously removes the thirty-one
immutable run-two occurrences, retains the exact q1 diamond matching, and
retains one of the all-depth openings of Section 4.  Only
after that rethread, recursive socket transport, all-depth support and the
compiler must be re-audited jointly.

This is an exact finite separation theorem.  It neither refutes a different
`m=5` decoration nor proves a dimension-uniform repair packet.

## 7. Reproducibility

The lightweight audit is

```text
scratch/audit_thread_a_m5_three_c10_downstream_state_20260731.py
scratch/thread_a_m5_three_c10_downstream_state_20260731.audit.json
```

It reconstructs the displayed three switches and the forced-port matching
without repeating the large short-switch censuses.  It independently checks
the four-state leaf/trace cube, the literal `J(10,5)` lift, all internal
window masks, the endpoint graph, the displayed Hamilton closure, every
linear opening of that closure, and the immutable coordinate-run ledger.

Frozen lineage at this audit is:

```text
source three-C10 theorem      78c2079ad71641b96fc1e5002047f012f8f8fd787a73f4ae1d8bc6c916910881
source three-C10 JSON         f43e39674c4a027fe46ed2f9918e8c3dcc218865816decad4a8e1f4b8052c7e1
source endpoint JSON          1bc199e7758720b060cdf3ac1f2723ea1a38847e13de1b434f368ded42da2a94
this audit script             f97eaa7d8457f619e06fa91a501142a5b9fb0af0818fc0b31ae10ef318778041
this audit JSON               91201d7281bde581ef01a58778b6e8edbea8dcb7da37d185c76f1771b91b2a5e
JSON canonical payload        19752a1d1ec5d02ad5ab18479228a85d6128caa8b1bc51cc0226e509c8f31549
```
