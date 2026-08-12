# The full `H_4` orbit of the `D_4` pair-transfer factor

Date: 2026-07-26

This note characterizes the complete relabelling orbit of the factor
`G` in `MATH_THEOREM_D4_PAIR23_PORT_FACTOR_20260726.md`.  It also records
the exact scope of the port-substitution theorem: the orbit gives genuine
integral packet states, but it does not give four target labels at every
individual Dyck root, and port legality does not by itself settle the
crossing-collar capacity problem.

The asymptotically decisive qualification is that the standard dense
first-size-four **fringe** bank is strict inside the serviced child and is
therefore endpoint-inert.  The orbit supplies a strong local menu, not yet
an active bounded-packet partition of the complete early-scale occurrence
family.

## 1. The eight conjugate factors

Put

\[
 s_1=(2\ 3),\qquad s_2=(4\ 5),\qquad s_3=(6\ 7),
 \qquad H_4=\langle s_1,s_2,s_3\rangle\cong C_2^3.
 \tag{1.1}
\]

Every element of `H_4` fixes `1,8,9` and preserves the Catalan root
family `D_4`.  If `h=s_1^e_1s_2^e_2s_3^e_3`, define `G^h=hG`.  Reanchor
the relabelled row at the original root.  Since every `h` is an
involution, its oriented word is

\[
                    q_{G^h}(P)=h\bigl(q_G(hP)\bigr),
 \qquad
                    b_1^{G^h}(P)=h\bigl(b_1^G(hP)\bigr).
 \tag{1.2}
\]

### Theorem 1.1

The eight factors `G^h` are pairwise distinct integral
`D_4`-port-transversal exact factors.  In the root order

\[
1234,1235,1236,1237,1245,1246,1247,
1256,1257,1345,1346,1347,1356,1357,                 \tag{1.3}
\]

their first-insertion target maps are as follows.

\[
\begin{array}{c|cccccccccccccc}
(e_1e_2e_3)
&1234&1235&1236&1237&1245&1246&1247
&1256&1257&1345&1346&1347&1356&1357\\ \hline
000&8&8&7&8&3&3&3&7&3&6&8&8&2&4\\
001&8&8&8&6&3&3&3&3&6&7&8&8&4&2\\
010&8&8&7&8&3&7&3&3&3&6&2&5&8&8\\
011&8&8&8&6&3&3&6&3&3&7&5&2&8&8\\
100&8&8&7&8&6&8&8&3&4&2&2&2&7&2\\
101&8&8&8&6&7&8&8&4&3&2&2&2&2&6\\
110&8&8&7&8&6&3&5&8&8&2&7&2&2&2\\
111&8&8&8&6&7&5&3&8&8&2&2&6&2&2
\end{array}                                                   \tag{1.4}
\]

#### Proof

Relabelling preserves both exact ownership ledgers.  Formula (1.2) shows
that the row of `G^h` rooted at `P` has endpoints `P` and `[8]\P`, so it
also preserves every prescribed port.  The eight rows of (1.4) are
distinct, and therefore the eight factors are distinct.  The entries are
obtained directly from (1.2) and the fourteen words in equation (6.3) of
the source theorem.  \(\square\)

There is a second quick distinction.  The aggregate target histogram of
`G` is

\[
                   e_2+4e_3+e_4+e_6+2e_7+5e_8.       \tag{1.5}
\]

Every one of the three swapped coordinate pairs has unequal two entries.
Thus its `H_4` orbit already has eight distinct aggregate labelled
histograms.

## 2. Exact rootwise multiplicities

For a root `P` and label `x`, put

\[
             m_P(x)=|\{h\in H_4:b_1^{G^h}(P)=x\}|.   \tag{2.1}
\]

The complete table is

\[
\begin{array}{c|l|c}
P&\{x^{m_P(x)}:m_P(x)>0\}&|\operatorname {supp}m_P|\\ \hline
1234&8^8&1\\
1235&8^8&1\\
1236&7^4,8^4&2\\
1237&6^4,8^4&2\\
1245&3^4,6^2,7^2&3\\
1246&3^4,5,7,8^2&4\\
1247&3^4,5,6,8^2&4\\
1256&3^4,4,7,8^2&4\\
1257&3^4,4,6,8^2&4\\
1345&2^4,6^2,7^2&3\\
1346&2^4,5,7,8^2&4\\
1347&2^4,5,6,8^2&4\\
1356&2^4,4,7,8^2&4\\
1357&2^4,4,6,8^2&4
\end{array}                                                   \tag{2.2}
\]

Consequently the new orbit has four labels at eight roots, three labels
at two roots, two labels at two roots, and one label at two roots.  It is
therefore an eight-state **packet** library, but not a four-state library
at every occurrence.

If the single canonical factor `G_0` is adjoined to the eight conjugates,
the multiplicity table becomes

\[
\begin{array}{c|l}
1234&8^9\\
1235&8^9\\
1236&7^4,8^5\\
1237&6^5,8^4\\
1245&3^4,6^2,7^2,8\\
1246&3^4,5,7,8^3\\
1247&3^4,5,6^2,8^2\\
1256&3^4,4^2,7,8^2\\
1257&3^4,4^2,6,8^2\\
1345&2^5,6^2,7^2\\
1346&2^5,5,7,8^2\\
1347&2^5,5,6,8^2\\
1356&2^5,4,7,8^2\\
1357&2^5,4,6,8^2.
\end{array}                                                   \tag{2.3}
\]

This raises the number of four-label roots from eight to nine, but leaves
two frozen roots, two binary roots, and the three-label root `1345`.

### Corollary 2.1 (coarse transfer is state-independent)

Every `G^h` has pair totals

\[
                         (5,5,1,3)                    \tag{2.4}
\]

on `E_0={1,8}, E_1={2,3}, E_2={4,5}, E_3={6,7}`.
Thus choosing among the eight labelled states never changes the coarse
`E_2 -> E_3` unit transfer.

#### Proof

`H_4` fixes every `E_i` setwise.  \(\square\)

## 3. Aggregate first-boundary capacity

Summing (2.2) over the roots gives the exact orbit ledger

\[
 \sum_{h\in H_4}\sum_{P\in D_4}e_{b_1^{G^h}(P)}
 =20e_2+20e_3+4e_4+4e_5+12e_6+12e_7+40e_8.          \tag{3.1}
\]

Thus the uniform conjugate average has largest target multiplicity five
per fourteen-row packet.  In fact every single conjugate already has
largest first-insertion multiplicity five.

Suppose an occurrence family is the disjoint union of `N` complete
fourteen-row packets, plus `R` exceptional occurrences, and every complete
packet sees the same aligned first-insertion profile.  Under arbitrary
choices of conjugates, every physical target receives at most

\[
                             5N+R
          ={5\over14}(14N+R)+{9R\over14}.             \tag{3.2}
\]

Hence, if `R=o(p)` and its total regular mass `d=14N+R` obeys

\[
                            d\le\left({64\over25}-o(1)\right)p,
                                                                  \tag{3.3}
\]

then the first-boundary contribution is at most

\[
               \left({5\over14}{64\over25}+o(1)\right)p
                         =\left({32\over35}+o(1)\right)p<p.       \tag{3.4}
\]

This is a real `14/5=2.8` effective-capacity bound, strictly larger than
`64/25=2.56`.  It applies to the occurrence mass on which this boundary
profile is visible.  It must not be applied blindly to the complete

\[
                       M_s=C_s+2C_{s-1}+C_{s-2}        \tag{3.5}
\]

two-boundary atlas: the two collars and the background have different
boundary visibility.

## 4. The complete cyclic carrier census

For `1<=ell<=8`, `j in Z_9`, and `h in H_4`, put

\[
 \nu_{\ell,j}^h(S)
 =|\{P\in D_4:I_{\ell,j}(q_{G^h}(P))=S\}|.           \tag{4.1}
\]

Conjugacy gives

\[
                  \nu_{\ell,j}^h(S)=
                  \nu_{\ell,j}^1(h^{-1}S).           \tag{4.2}
\]

Thus every conjugate has the same largest collision multiplicity.  The
complete table

\[
 m_{\ell,j}=\max_S\nu_{\ell,j}^h(S)                  \tag{4.3}
\]

is independent of `h` and equals

\[
\begin{array}{c|rrrrrrrrr}
\ell\backslash j&0&1&2&3&4&5&6&7&8\\ \hline
1&5&4&5&5&5&3&4&5&14\\
2&2&2&2&5&2&2&2&5&5\\
3&1&1&2&2&1&1&2&2&2\\
4&1&1&1&1&1&1&1&1&1\\
5&1&1&1&1&1&1&1&1&1\\
6&2&2&2&1&1&2&2&1&1\\
7&5&5&2&2&2&5&2&2&2\\
8&14&5&4&5&5&5&3&4&5.
\end{array}                                                   \tag{4.4}
\]

The only constant local profiles are `(ell,j)=(1,8)`, whose target is
`{9}`, and `(8,0)`, whose target is `[8]`.  Every other carrier profile
has collision multiplicity at most five in a complete packet.

For completeness, let

\[
 A_{\ell,j}=\max_S\sum_{h\in H_4}\nu_{\ell,j}^h(S).  \tag{4.5}
\]

The exact uniform-orbit numerators are

\[
\begin{array}{c|rrrrrrrrr}
\ell\backslash j&0&1&2&3&4&5&6&7&8\\ \hline
1&40&20&20&40&40&20&28&40&112\\
2&16&8&16&40&12&16&16&40&40\\
3&8&8&16&16&8&8&16&16&16\\
4&8&8&8&8&8&8&8&8&8\\
5&8&8&8&8&8&8&8&8&8\\
6&16&16&16&8&8&16&16&8&8\\
7&40&40&16&8&16&40&12&16&16\\
8&112&40&20&20&40&40&20&28&40.
\end{array}                                                   \tag{4.6}
\]

In particular the same `5/14` bound holds simultaneously for every
nonconstant carrier profile when the eight conjugates are used uniformly.
The factor histogram is independent of the `H_4` choice only at

\[
 (1,8),(4,0),(4,4),(5,4),(5,8),(8,0).                \tag{4.7}
\]

The middle four profiles in (4.7) are already simple ledgers: respectively
the roots, their complements, the complements with `9`, and the roots
with `9`.  The first and last profiles are the two constant collars and
cannot be split by this library.

Equations (4.4)--(4.7) are a finite carrier-resolved certificate.  Their
use in an ambient factor requires that the fourteen rows of each packet
have one common cyclic local profile `(ell,j)` and one common exterior
set, or, more generally, that the physical push-forward be injective on
the local target ledger.  A window meeting overlapping local atoms must
be evaluated as a joint profile rather than by adding the two tables.

## 5. What an independent opposite bit would give

Suppose a second boundary carries a legal binary choice, uses a disjoint
coordinate pair, is visible on the same occurrences, and its ownership
component is independent of the `H_4` packet choice.  If intersection
with the second coordinate pair recovers its bit, every first-boundary
target splits into two distinct cells.  A balanced product library then
has largest regular cell at most

\[
                              {5d\over28}+o(p).        \tag{5.1}
\]

For a bulk fibre with `d=C_s<4p`, this is below `5p/7`.

Rootwise, however, the numbers of distinct product cells are

\[
        2,2,4,4,6,8,8,8,8,6,8,8,8,8                 \tag{5.2}
\]

in the order (1.3).  Therefore:

* the eight conjugates are eight genuine global packet states;
* eight local cells occur at eight of the fourteen roots;
* a uniform eight-cell statement on the complete occurrence family is
  false for this orbit;
* adjoining the canonical factor raises the eight-cell roots only from
  eight to nine.

Most importantly, (5.1) applies only where **both** choices are visible.
In the natural two-boundary atlas, the bulk sees both choices, the two
one-sided collars see only one each, and the double collar sees neither.
The complete cap condition is therefore a carrier-resolved sum of the
bulk, collar, background, and unaffected loads.  Nominally having eight
states does not replace that ledger.

## 6. Exact ownership and the `a_1,b_4` seam

There are two different assertions which must not be conflated.

### Proposition 6.1 (closed-slab ownership is legal)

Let a local row be the full closed path

\[
               X_0=P,X_1,X_2,X_3,X_4=[8]\setminus P, \tag{6.1}
\]

including all four internal adjacent-union cells
`Y_t=X_t union X_(t+1)`.  Attach unchanged outer row pieces only at
`X_0` and `X_4`.  Replacing the canonical packet by any `G^h` preserves
exact ambient middle ownership.

#### Proof

The two outer incident edges have the same endpoint state before and
after the replacement, so their rowwise union colours are unchanged.
The entry and exit exchanges which may change `a_1` or `b_4` lie inside
the closed slab.  Their states are included in the complete `X` ledger,
and their adjacent-union colours are included in the complete `Y` ledger.
Both ledgers are exact for every `G^h`.  Hence the total state and edge
ownership discrepancies vanish.  This is precisely the corrected
Section-17 port-substitution theorem.  \(\square\)

Thus changing `a_1` or `b_4` does **not** break the exact middle-factor
join in the closed port interface.

### Proposition 6.2 (what the port theorem does not preserve)

The port theorem does not preserve the oriented cyclic seam

\[
                              b_4,9,a_1,               \tag{6.2}
\]

nor any lower-rank window crossing that seam.  It also does not justify a
substitution which

1. truncates one of the internal boundary edges;
2. attaches an outer row at a half-edge or at an oriented coordinate
   rather than at `X_0` or `X_4`;
3. overlaps or nests another modified slab without a joint ledger; or
4. requires preservation of a later necklace/phase partition.

For these uses the required boundary datum is the full positional tensor

\[
 D_A=\sum_{P\in D_4}
   \left(e_{\{q_i^{G^h}(P):i\in A\}}
        -e_{\{q_i^{G_0}(P):i\in A\}}\right),          \tag{6.3}
\]

together with the literal exterior push-forward.  Equivalently, for a
nested exact replacement one must exhibit the complete outer `X/Y`
ledgers, not only the inner ports.

This is the definitive seam distinction: ports settle exact ownership of
a closed slab; the carrier tensor settles the crossing shadows and every
larger non-closed interface.

## 7. Conclusion

The `H_4` orbit is a real eight-state exact library.  It preserves the
coarse pair transfer, and every nonconstant one-hole carrier profile has
complete-packet multiplicity at most five.  This supplies an effective
`14/5` local capacity and, conditionally on a commuting disjoint opposite
bit, a `28/5` bulk capacity.

It does **not** prove a complete eight-cell parent atlas: six roots have
fewer than four first-boundary labels, two local carrier profiles are
constant, and the one-sided collars/background require their own physical
capacity ledger.  Those are now exact, finite constraints rather than an
ambiguity about factor legality.

## 8. Deployment obstruction: the dense fringe bank is boundary-inert

There is a further asymptotic qualification.  The stable first-size-four
fringe decomposition does produce fourteen-row packets on all but an
exponentially small fraction of large Dyck fillings.  Those packets are
not, however, boundary packets for the serviced size-`s` child.

### Proposition 8.1 (strict-fringe erasure)

Let a complete size-four packet lie strictly inside a serviced child
window `W`.  Every choice among the factors `G^h` has the same two
exported endpoints of `W` and the same target for the full endpoint
window.

#### Proof

The local closed slab contains its complementary ports `Q` and
`J_4\setminus Q`.  Since `W` contains the whole slab, the local
contribution to the intersection defining the target of `W` is contained
in

\[
                         Q\cap(J_4\setminus Q)=\varnothing.       \tag{8.1}
\]

The exported endpoints of `W` lie outside the strict descendant slab and
are unchanged.  \(\square\)

In the natural no-interior-return family

\[
 \mathcal B_s\simeq
 \mathcal D_s\ \dot\cup\ \mathcal D_{s-1}\ \dot\cup\
 \mathcal D_{s-1}\ \dot\cup\ \mathcal D_{s-2},       \tag{8.2}
\]

all four central filling sizes exceed four once `s>=7`.  Every standard
first-size-four fringe packet is then strict, so its `H_4` state changes
neither Boolean endpoint bit.  The dense fringe partition therefore has
**zero** boundary-active packets on `B_s`; it cannot be fed into the
two-partition contingency theorem with a small exceptional set.  The
finite whole-central exceptions occur only at `s=4,5,6`.

Consequently Sections 3--5 are conditional local capacity theorems.  To
use them asymptotically one still needs a new construction which partitions
all but `o(M_s)` serviced occurrences into bounded **parent-aligned**
packets, or a growing parent-scale port-factor library.  The present dense
fringe bank does not provide that deployment.
