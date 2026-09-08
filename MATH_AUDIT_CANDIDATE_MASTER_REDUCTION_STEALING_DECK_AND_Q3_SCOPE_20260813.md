# Audit of the proposed stealing-deck character theorem and master reduction

**Date:** 2026-08-13  
**Audited source:** /Users/amir.nuriyev/.codex/attachments/4db2edd8-d89f-48d3-9505-72e9701eee08/pasted-text.txt  
**Verdict:** **FAIL.** The fixed-core character in Theorem C(a) is
correct, but C(c) does not prove simultaneous cross-core elimination.
More importantly, the quoted results do not imply the master reduction:
the signed theorem omits compulsory rows, the Ferrers theorem is
capacity-only, and the four-socket host does not give a global bounded
component count.

## 1. Theorem C(a) passes

For a fixed core \(C\), every period-\(N\) cyclic \(q\)-window deck gives
each selected toggle point degree \(q\) and every unused point degree
zero. Therefore

\[
 \chi_x(v)=\sum_{\substack{H\supset C\\x\in H\setminus C}}v_H
 \pmod q
\]

annihilates every fixed-\(C\) column. The all-one demand on the fibre
has value \(\binom{M-1}{q-1}\), so

\[
 q\mid\binom{M-1}{q-1}
\]

is necessary for a decomposition confined to that fibre. This argument
is independent of the legal period.

## 2. First exact gap in C(c)

The actual projection of a stealing deck with the old core point \(w\)
placed in the toggle order is a **two-sided** cyclic staircase around
\(w\):

\[
 v_{w,\sigma}(x)=
 \begin{cases}
 q-\delta,&x\text{ is at circular distance }\delta\in[1,q-1]
             \text{ from }w\text{ on either side},\\
 0,&\text{otherwise},
 \end{cases}
 \pmod q .
\]

The proof of C(c) instead declares a one-sided vector

\[
 S=(q-1)e_{x_1}+\cdots+e_{x_{q-1}}
\]

to be a generator and obtains \(e_a-e_b\) by swapping one designated
point. No argument is given which realizes \(S\) itself by actual
stealing decks or holds the opposite staircase fixed while replacing
one point. This may be repairable when enough spare toggle points exist,
but it is not the displayed proof.

There is a more fundamental quantifier problem. An owner belongs to
many core fibres:

\[
 H\in\mathscr F_C\quad\Longleftrightarrow\quad C\subset H.
\]

A stealing deck introduced to correct the \(C\)-fibre therefore changes
the ledgers of every other \(c\)-core contained in one of its owners.
Consequently, even a proof that each isolated fibre character is generated
does not show that all fibre characters can be killed simultaneously.
The identity

\[
 M\binom{M-1}{q-1}=q\binom Mq
\]

only proves that the constant target vector has zero total coordinate in
one proposed quotient. It supplies neither a globally consistent
cross-core allocation nor a positive owner-disjoint selection.

Thus the safe conclusion of C is only:

> The displayed fixed-core character is not visibly invariant under
> arbitrary core migration, provided the actual stealing projections
> generate the needed global image.

That global image statement remains unproved.

## 3. “Q3 kills all Smith torsion” is out of scope

The quoted signed theorem proves exactly

\[
 \mathbb Z^{\binom{[k]}R}
 \oplus\mathbb Z^{\mathcal L_{\rm residual}}\oplus\{0\}
\]

after retaining only named owners, optional designated lower marks, and
whole-component trace boundary. It explicitly excludes compulsory
immediate-palette rows, phase/socket actions, nonoptional upper tickets,
and typed common-cap resources.

Therefore Q3 does **not** prove that the full protected packet matrix has
trivial Smith quotient. Moreover, reserving a bank or freezing protected
variables deletes columns, which can create torsion even when the
unprotected owner projection is saturated. The M2 table's sentence
“Q3 kills all Smith torsion” is false unless restricted to the projected
rows above.

Finite character correction per fibre would still give no positive
conclusion. A signed representation may reuse owners with opposite or
same signs, and its number of decks need not admit simultaneous
within-sign packing. The positive-semigroup gate is not weakened merely
by bounding the number of algebraic generators used for one fibre.

## 4. The Ferrers input is capacity-only

The exact arbitrary-boundary theorem supplies a matching of residual
lower targets into \(d\) labelled copies of their containing owners. It
explicitly does not prove that the targets assigned to one owner form a
nested suffix flag, agree with the owner's literal cyclic order, or avoid
uncontrolled repeated physical occurrences.

Hence the step in Theorem A

\[
 \text{“Q2 distributes the Ferrers flags onto selected rails' prefix
 slots with at most \(C_2\) misses”}
\]

does not follow from Q2. A scalar containment cut cannot install the
compulsory literal flag rows of PS\((k)\).

The same issue appears in Theorem B(vii): saying that the spray core is
“freely steerable” does not prove simultaneous nested-chain realization
with the fixed toggle prefixes, nor compatibility with the globally
selected rail factor.

## 5. The host theorem does not imply bounded global fusion defect

Q4 gives a spanning two-factor containing a prescribed protected bank.
It explicitly permits many other factor cycles. Re-pairing one
four-socket bank can merge only components which meet those four sockets.
Neither Q4 nor Theorem B constructs a connected graph of banks meeting
all global components.

Accordingly the claim

\[
 C_1\text{ is absolute “by Q4 + Theorem B's fusion action”}
\]

is unsupported. To make Proposition 4 applicable one still needs a
global occurrence-level merge graph which is connected up to components
containing \(O(1)\) owners, with all selected switches simultaneously
legal.

## 6. The new AP bank lacks the stated dual-residence proof

In Theorem B, every label of \(Y\) appears once in **each** of four visit
tracks, and every label of the common tuple \(U\) appears before each
visit. One occurrence indeed generates \(q\) consecutive positive owner
states. But BH1--BH4 impose no lower bound on the cyclic distance between
successive occurrences of the same physical label after tracks are
re-paired.

If two occurrences have separation \(g\), their owner intervals leave a
zero run of length \(g-q\) when \(g>q\), and merge when \(g\le q\).
This zero run may have length \(1,\ldots,q-1\). Thus the statement
“every non-core element's owner-membership runs have length exactly \(q\),
zero-gap” is false as a global trace statement. A valid dual-residence
theorem needs either private track labels or an explicit condition that
every inter-occurrence separation is \(q\) or at least \(2q\), including
all switched seams.

## 7. Exact master boundary

Even granting PS\((k)\) as written, Theorem A still needs three distinct
inputs not supplied by Q2--Q6:

1. literal nested Ferrers-flag alignment in the same selected rails;
2. a component-spanning, occurrence-safe switch graph with bounded
   residual component mass; and
3. joint preservation of compulsory upper and typed cap rows under those
   switches.

The proof therefore cannot reduce the whole problem to PS\((k)\) alone.
The first possible integral obstruction remains the full protected
occurrence matrix, not its owner/optional-mark projection.

