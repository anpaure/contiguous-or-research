# Independent audit of protected plateau transport

> **Supersession notice (2026-07-31).**  This audit's approval of the
> length-only component-parity law is withdrawn.  The explicit `m=2`
> two-rail C8 in
> `MATH_THEOREM_R_CATALAN_TWO_RAIL_PORT_MATCHING_AND_C8_CONNECTIVITY_OBSTRUCTION_20260731.md`
> maps two cycles to two cycles and refutes that law.  Statements about fixed
> protected-face circulation and the literal PBBS interface remain valid;
> all claims that every C6 preserves parity or every C8 flips it are
> superseded by the exact occurrence-port pairing criterion.

Date: 2026-07-31.

Scope: hand mathematics only. This audit covers the three new Lane-R notes
on protected circulation, hexagon parity, and the PBBS fragment-braid
interface. No finite search, SAT run, or web source was used.

## 1. Valid unconditional results

### 1.1 Fixed-guard circuit connectivity

Let \(I\) be the middle consecutive-level incidence graph, let \(P\) be a
fixed incidence support, and let

\[
 {\cal F}(P)=\{F\subseteq E(I):d_F\equiv2,\ P\subseteq F\}.
\]

For \(F_0,F_1\in{\cal F}(P)\), red and blue degrees in
\(F_0\triangle F_1\) agree at every vertex. Pairing opposite-colour
half-edges gives alternating circuits disjoint from \(P\). Toggling them
one at a time remains in \({\cal F}(P)\). Thus every literal interval
witness whose complete incidence support lies in \(P\) survives at every
stage. This proof and all quantifiers are valid.

The hereditary residence claim is also valid in its deliberately strong
form: for every coordinate \(x\) and every \(x\)-owner \(V\), the guarded
\(x\)-component through \(V\) must itself contain at least \(h\) owners.
Any completion containing the guard then has an \(x\)-run containing that
component. Endpoint-DFA safety without such a hereditary guard is a
different, order-dependent condition.

### 1.2 Exact forced-witness circulation

For a current factor \(F\), protected support
\(P'=P\cup(Q\cap F)\), and mandatory new incidences \(A=Q\setminus F\),
orient addable incidences from the lower to the upper shore and removable
incidences from the upper to the lower shore. Give every arc capacity one
and give arcs in \(A\) lower bound one. Hoffman's circulation theorem gives
the exact criterion

\[
 |A\cap\delta^+(S)|\le |\delta^-(S)|
 \qquad(S\subseteq V(I)).                              \tag{1.1}
\]

The orientation is correct: the usual inequality
\(\ell(\delta^-(S))\le u(\delta^+(S))\), applied to the complement of
\(S\), is (1.1). Integral capacities give a binary circulation. Toggling
its arcs preserves every degree, never removes \(P'\), and installs every
edge of \(Q\). Conversely, the symmetric difference with any factor
containing \(P\cup Q\) is such a circulation. Necessity, sufficiency, and
integrality therefore pass.

The duplex make-before-break corollary is valid: first reach a common factor
containing old and new witness supports while freezing the old support;
then freeze the new support and release the old. It is a factor-shadow
transport theorem. It does not itself provide component connectivity,
chronology, residence-DFA acceptance, an opening, or common-\(Q\)
compilation.

### 1.3 Residual guarded Hall condition

For a paired guard \(K\), residual demands
\(b_C=2-d_K(C)\), \(b_V=2-d_K(V)\), and residual graph \(H=I\setminus K\),
the exact b-matching condition is

\[
 b_{\cal C}(A)\le b_{\cal V}(B)+e_H(A,{\cal V}\setminus B)
 \quad(A\subseteq{\cal C},\ B\subseteq{\cal V}),      \tag{1.2}
\]

together with equal total demand and \(d_K\le2\). This is exactly the
source--lower--upper--sink min-cut inequality, and unit incidence
capacities make the completion integral. Marginal endpoint Hall does not
imply (1.2).

### 1.4 Component-parity law

If a simple alternating circuit has length \(2\ell\), delete its
\(\ell\) old factor edges. The remaining affected paths pair the circuit
vertices by a matching \(P\); the old and new shores are matchings \(R,B\),
and \(R\cup B\) is one \(2\ell\)-cycle. The three-matching sign identity
gives

\[
 c(F\triangle C)-c(F)\equiv\ell-1\pmod2.              \tag{1.3}
\]

Hence legal incidence hexagons (\(\ell=3\)) preserve component parity.
The proof passes. The fixed-opening corollary also passes after adjoining
the same dummy closing edge at every stage.

### 1.5 Explicit \(I(5,2)\) checks

The displayed Hamilton factor \(H\) and two-cycle factor \(E\) each use all
ten rank-two and all ten rank-three vertices exactly once. Directly taking
the union of the two adjacent rank-three owners at every rank-two row gives
each of the five rank-four targets exactly twice in both factors. Their
symmetric difference is exactly the displayed alternating \(C_{12}\), so
the toggle changes component count from one to two, as (1.3) predicts.
This proves that the legal-C6 move graph is disconnected even inside the
immediate-upper-complete fibre.

The separate protected \(C_8\) example also passes. The fixed support
saturates every vertex outside the chordless eight-cycle and leaves residual
demand one at its eight vertices. The protected face consequently consists
of the two shores of that \(C_8\), with no protected C6 move.

### 1.6 Common-exterior neutral hexagons

Under the explicit assumption that the opposite hexagon half is absent,
the other selected owner in each of the three rows has an exterior label
outside the core and all three petals. The old and new immediate-upper
triples have petal-pair signatures \(ab,bc,ca\). Multiset equality forces
the three exterior labels to agree, and a common label plainly suffices.
Thus the common-exterior classification is exact.

Fixed-span protection is valid. Residence after a switch is exact only
after composing the coordinate DFA in the actual orientation of every
fragment and, for a cycle, across its closing seam. The corrected theorem
assumes a reversal-closed forbidden language (as for \(01^t0\)); otherwise
each reversed fragment must be separately checked internally.

## 2. Corrected implication scopes

The following corrections were required and have been incorporated in the
theorem notes.

1. “Exact zero-defect criterion” means an exact balanced-factor shadow
   endpoint. It does not include topology, a linear chronology, boundary
   residence, or the common-cap compiler.
2. A static loose tree of neutral C6 switches must have disjoint extended
   supports: the six cycle incidences and the three exterior-owner
   incidences. Disjoint six-cycles alone can share a lower row, allowing an
   earlier toggle to destroy a later switch's common exterior. Sequential
   DFA acceptance remains mandatory.
3. A parity absorber is defined by the exact net condition
   \(c(F')=c(F)-1\), not merely by an informal claim that two components are
   merged.
4. Guard-intersection connectivity is an absorber architecture. It
   preserves a common predicate only when every guard in the chain certifies
   that predicate. A full converse additionally needs catalogue coverage,
   protected connectivity inside every catalogue fibre, protected
   intersections, and transition refinement. Net-protected compound
   circuits can cross between guards having no common factor.
5. The factor-to-braid dictionary uses cuts \(M\setminus N\) and seams
   \(N\setminus M\). The final endpoint is a decorated path-cover with
   colour rows, protected spans, composed DFA state, and no subtours; it is
   not merely a static endpoint matching.
6. Any conclusion \(\nu(k)=B(k)\) remains conditional on an independently
   proved exact common-cap/compiler theorem, coverage of the entire required
   target universe, a legal opening, and complete literal replay.

## 3. Exact proved/open boundary

The strongest unconditional result is:

> Within one fixed literal protected face, compound alternating circuits
> give plateau-monotone zero-shadow-defect transport. For a fixed proposed
> replacement witness bank, (1.1) is necessary and sufficient for a duplex
> protected factor handoff.

The strongest C6 result is conditional:

> After one protected parity-changing absorber when needed, a sequentially
> legal bank of common-exterior neutral hexagons on distinct current
> components, with fixed-span witness protection and exact DFA replay,
> Hamiltonizes the carrier with zero shadow/residence defect.

This cannot be made unconditional: C6 toggles preserve component parity,
and the \(I(5,2)\) examples disprove both unprotected and protected
hexagon-only connectivity.

For PBBS, the remaining all-dimensional carrier lemma is to select sparse
literal witnesses and/or duplex guards satisfying every Hoffman cut while
leaving a colour-exact, product-DFA-accepted connected fragment completion.
For a C6-based fusion architecture, an even-component PBBS factor also
requires a protected even-half-length parity absorber. Even after that
carrier lemma, simultaneous common-cap compilation remains separate.

No unconditional all-\(k\) equality theorem is claimed.
