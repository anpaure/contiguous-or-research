# The four-row Tamari associator has zero q1 current

## Status

The all-dimensional four-row Tamari associator preserves the two central
shore ledgers.  This note adds the missing adjacent-intersection audit and
proves that it also preserves the complete immediate-upper q1 palette.

Consequently, adjoining every coordinate conjugate or every currently
plantable four-row associator to the native MSW inverse-pair currents does
not enlarge their **static** rational or integer q1 span at all.  The span
deficiency of
`MATH_THEOREM_NATIVE_MSW_INVERSE_PAIR_SPAN_DEFICIENCY_20260806.md`
therefore survives unchanged.

The associator may still be useful dynamically: it can change which
inverse-pair slots exist while paying zero q1 current.  No present theorem
shows that its reachable host states expose all coordinate-conjugate
inverse pairs.  The exact remaining statement is a slot-transitivity
theorem, not another current identity.

No computation or search is used.

## 1. The missing base ledger

Use the port-restored negative and positive packets

\[
                 \mathcal P^-=(A^-,L^-,C^-,D^-),
 \qquad          \mathcal P^*=(A^*,L^*,C^*,D^*)
\tag{1.1}
\]

from the four-row Tamari associator.  Every named row is a rank-four
Johnson geodesic

\[
                           P_0,P_1,\ldots,P_4
\tag{1.2}
\]

on `[8]`.  For a packet `mathcal P`, define its adjacent-intersection
ledger

\[
 \mathcal I(\mathcal P)
 =\mathop{\dot\bigcup}_{P\in\mathcal P}
    \mathop{\dot\bigcup}_{t=0}^3\{P_t\cap P_{t+1}\}.
\tag{1.3}
\]

### Lemma 1.1 (exact intersection equality)

The three packet phases `mathcal P^-`, `mathcal P^+`, and
`mathcal P^*` have the same adjacent-intersection multiset.  It is

\[
\begin{aligned}
 \mathcal I_0=\{&124,125,126,127,128,137,146,147,148,\\
                 &168,347,467,478,678,468,468\}.
\end{aligned}
\tag{1.4}
\]

#### Proof

For the negative packet, the four row lists are

\[
\begin{array}{c|cccc}
A^-&126&146&467&347\\
L^-&125&128&168&678\\
C^-&127&124&148&468\\
D^-&137&147&478&468.
\end{array}
\tag{1.5}
\]

For the port-restored packet they are

\[
\begin{array}{c|cccc}
A^*&125&128&148&478\\
L^*&124&126&168&678\\
C^*&127&147&146&468\\
D^*&137&347&467&468.
\end{array}
\tag{1.6}
\]

Both tables enumerate (1.4), including the double occurrence of `468`.
The intermediate packet gives the same list:

\[
\begin{array}{c|cccc}
A^+&347&478&148&128\\
L^+&125&126&168&678\\
C^+&127&124&146&468\\
D^+&137&147&467&468.
\end{array}
\tag{1.7}
\]

This is the claimed literal multiset equality.  \(\square\)

Thus the base associator preserves not only its state and adjacent-union
ledgers, but both adjacent Boolean shadows.

## 2. Tensoring preserves the intersection ledger

For semilength `r>=4`, the all-dimensional tensor adjoins one common
`(r-4)`-set `S_0` to the five base states and then appends the same
complement geodesic

\[
                         S_0,S_1,\ldots,S_{r-4}
\tag{2.1}
\]

to the fixed terminal state of every named row.

### Theorem 2.1 (all-dimensional adjacent-intersection equality)

The two tensor phases have identical aggregate adjacent-intersection
multisets of rank `r-1`.

#### Proof

On the first four transitions,

\[
 (P_t+S_0)\cap(P_{t+1}+S_0)
                 =(P_t\cap P_{t+1})+S_0.
\tag{2.2}
\]

Lemma 1.1 therefore gives equality on the base segment.  The terminal base
state `P_4` is fixed row by row by the port-restored associator.  Hence the
junction intersection and every tail intersection are literally identical
in the two phases:

\[
 P_4+(S_0\cap S_1),qquad
 P_4+(S_j\cap S_{j+1}).
\tag{2.3}
\]

Adding the row ledgers proves the theorem.  \(\square\)

### Corollary 2.2 (zero immediate-upper current)

In the middle-levels lift on `2r+1` coordinates, the complete rank-`(r+2)`
immediate-upper current of the tensored associator is zero.

#### Proof

For a shortest wreath, complementation identifies the rank-`(r-1)`
adjacent-intersection values with the rank-`(r+2)` immediate-upper values.
Apply Theorem 2.1.  \(\square\)

The conclusion is occurrence-multiset equality, not merely equality of
coordinate marginals.

## 3. Static span after adding all associators

Fix one canonical MSW factor `F`.  Let

* `R(F)` be the set of q1 currents of all native inverse-pair moves
  available in `F`;
* `T(F)` be any family of physically plantable four-row associators in
  `F`, including arbitrary coordinate-conjugate copies whose negative
  packet actually occurs.

### Theorem 3.1 (static span is unchanged)

Over both the integers and the rationals,

\[
 \left\langle R(F)\cup\{\Delta_{q1}(A):A\in T(F)\}\right\rangle
                      =\langle R(F)\rangle.
\tag{3.1}
\]

The same identity holds if all prospective coordinate conjugates of the
four-row tensor are adjoined formally.

#### Proof

Corollary 2.2 gives `Delta_q1(A)=0` for every relabelled or planted
associator.  Adding zero vectors does not change a span.  \(\square\)

### Corollary 3.2 (the fixed-factor annihilator survives)

For every `m>=4`, the one-step native inverse-pair-plus-associator move set
still has non-coordinate q1 invariants.  Its extra annihilator dimension is
at least

\[
 (2m+1)left({C_m(m-2)\over2(m+2)}-1\right).
\tag{3.2}
\]

For the proved `1100/1010` inverse family, every target untouched by that
family remains untouched by all associator currents.

#### Proof

Combine Theorem 3.1 with the fixed-factor span theorem quoted in the
status.  \(\square\)

This answers the literal “adjoin the associator currents” question
negatively: the richer packet is a zero-current host reconfiguration, not a
new q1 lattice generator.

## 4. Prospective conjugates versus a physical orbit

There are three different statements which must not be conflated.

1. **Abstract orbit statement.**  Across arbitrary coordinate conjugates
   of the complete MSW factor, inverse-pair squares generate the full
   coordinate-balanced lattice.
2. **Static fixed-factor statement.**  In one factor, inverse pairs plus
   all currently available associators have the deficient span in
   Corollary 3.2.
3. **Dynamic statement.**  A zero-current associator may change the factor
   and expose an inverse pair that was absent before.  A long alternating
   sequence may therefore have a larger set of inverse currents than its
   time-zero atlas.

The current theorems prove statements 1 and 2.  They do not settle 3.

The four-row tensor theorem says that if its four negative rows are already
present, they may be replaced exactly.  It explicitly does not prove that
those rows occur in a prescribed factor.  At the base dimension there is a
concrete warning: the port-restored four-row packet contains seven Dyck
states but only four row ports, so it cannot be embedded in a complete
Dyck-port-transversal exact factor on the same support.  Tensoring preserves
the local packet identity but does not supply a global host selector.

## 5. Exact dynamic gate

Let `G_A(F)` be the graph of exact factors reachable from `F` using only
physically planted four-row associators.  Define the dynamic inverse span

\[
 \mathcal S_{\rm dyn}(F)
   =\left\langle
       \Delta_{q1}(P):
       P\text{ is an inverse pair available in some }
       F'\in G_A(F)
     \right\rangle.
\tag{5.1}
\]

Always

\[
       \langle R(F)\rangle
       \subseteq\mathcal S_{\rm dyn}(F)
       \subseteq\ker A.
\tag{5.2}
\]

The missing theorem is exactly

> **Associator slot-transitivity.**  For every square
> `square(Z;r,s|a,d)`, some associator-reachable exact factor contains an
> inverse pair with that q1 current, with a path which retains the named
> protected providers.

If slot-transitivity holds, then

\[
                         \mathcal S_{\rm dyn}(F)=\ker A
\tag{5.3}
\]

by the abstract square-generation theorem.  Without it, prospective
coordinate relabellings of the finite tensor do not constitute physical
moves of one factor.

Even (5.3) would be only a signed reachability theorem.  A proof of
immediate-upper coverdown would still require a positive, last-provider-safe
path and simultaneous control of deeper widths and topology.

