# Prefix/suffix OR transparency and the fixed-slot C6 signature gate

Date: 2026-07-31  
Lane: A, upper-shadow compression for buffered C6/ECO packets  
Status: exact linear/cyclic replacement theorem, exact signature filter, a
raw-C6 quadratic-supply obstruction, and one abstract signature-transparent
fixed-4 serialization proved; no physical all-\(m\) buffered packet follows

## 0. Verdict

Pointwise equality of all prefix unions and suffix unions is an exact
context-free certificate: an equal-length replacement at a fixed address
preserves every interval union which is not wholly internal to the replaced
slot, at every width.

Two qualifications are decisive.

1. A slot of length \(h=\Theta(d)\) has \(\Theta(d^2)\) internal intervals
   through all depths, not \(O(d)\).  Full boundary signature gives
   \(O(d)\) physical span and \(O(d)\) internal windows at each fixed depth.
   An \(O(d)\) all-depth ticket row still needs internal-deck compression or
   support-private local certification.
2. The raw fixed-anchor C6 menu is not quadratically compatible with one
   common full signature.  Relative to a fixed off-C6, signature safety fixes
   the insertion column \(c\), leaving only \(m\) of the \(m^2\) choices.
   More generally, a common anchored Johnson slot with
   \(m^2-O(md)\) signature-safe choices has length at least
   \(m-O(d)\).

There is a positive local algebraic identity: the fixed-4 incidence C6 has
two six-owner serializations with identical full signatures.  Each
serialization, however, has one internal Johnson-distance-two seam.  Thus
the resource identity admits the desired OR signature, but a literal
degree-two owner chronology still needs a buffer/connector for that one
antipodal seam.

## 1. Full boundary signature

For a word fragment \(X=(X_1,\ldots,X_h)\), define

\[
 P_j(X)=\bigcup_{i=1}^jX_i,\qquad
 S_j(X)=\bigcup_{i=j}^hX_i                                      \tag{1.1}
\]

and

\[
                         \Sigma_\vee(X)=
                         \bigl((P_j(X))_{j=1}^h,
                               (S_j(X))_{j=1}^h\bigr).            \tag{1.2}
\]

### Theorem 1.1 (linear all-width transparency)

Let

\[
                         W=LXS,\qquad W'=LYS,                     \tag{1.3}
\]

where \(X,Y\) occupy the same address and have the same length.  If

\[
                         \Sigma_\vee(X)=\Sigma_\vee(Y),           \tag{1.4}
\]

then every corresponding interval not wholly contained in the replaced
slot has exactly the same union in \(W\) and \(W'\).

#### Proof

An interval disjoint from the slot is unchanged.  An interval meeting only
the left boundary is an unchanged suffix of \(L\) united with \(P_j(X)\);
an interval meeting only the right boundary is \(S_j(X)\) united with an
unchanged prefix of \(S\).  An interval crossing both boundaries contains
the full slot, whose union is \(P_h(X)=P_h(Y)\).  These exhaust the linear
cases. \(\square\)

### Theorem 1.2 (cyclic all-width transparency)

Theorem 1.1 remains true for a fixed proper slot in a cyclic word, without
choosing the global opening.

#### Proof

The intersection of a cyclic interval with one proper cyclic slot is one of

\[
 \varnothing,\quad X,\quad\text{a prefix},\quad\text{a suffix},
 \quad\text{a prefix united with a suffix}.                       \tag{1.5}
\]

The first four cases use Theorem 1.1's identities.  In the last case,
equality of the relevant prefix and suffix unions gives equality of their
union. \(\square\)

Fixed placement and equal length are essential.  Moving the opening,
rerooting, or changing the address is a separate operation.

## 2. Exact coordinate and fixed-context forms

For a coordinate \(x\), let \(f_X(x)\) and \(\ell_X(x)\) be its first and
last occurrence positions in \(X\), with the usual absent-coordinate
conventions.

### Proposition 2.1 (first/last characterization)

\[
 \Sigma_\vee(X)=\Sigma_\vee(Y)
 \quad\Longleftrightarrow\quad
 f_X(x)=f_Y(x)\ \hbox{and}\ \ell_X(x)=\ell_Y(x)
 \quad\hbox{for every }x.                                        \tag{2.1}
\]

#### Proof

A coordinate belongs to \(P_j(X)\) exactly when \(f_X(x)\le j\), so all
prefix unions determine and are determined by all first occurrences.
Likewise \(x\in S_j(X)\) exactly when \(\ell_X(x)\ge j\). \(\square\)

Equivalently, put \(P_0=\varnothing\), \(S_{h+1}=\varnothing\), and

\[
 M_i=(P_i\setminus P_{i-1})\cup(S_i\setminus S_{i+1}),\qquad
 C_i=P_i\cap S_i.                                                 \tag{2.2}
\]

Then \(Y\) has the same signature as \(X\) exactly when

\[
                         M_i\subseteq Y_i\subseteq C_i            \tag{2.3}
\]

at every position, together with any separately required rank condition.

For one fixed exterior, full equality is sufficient but not necessary.
If \(\lambda\) is the cell immediately left of the slot and \(\rho\) the
cell immediately right, exact crossing transparency is equivalent to

\[
 P_j(X)\mathbin\triangle P_j(Y)\subseteq\lambda,\qquad
 S_j(X)\mathbin\triangle S_j(Y)\subseteq\rho                       \tag{2.4}
\]

for every \(j\), omitting a row when that exterior side is absent.
Necessity uses the shortest crossing interval \(\lambda X_1\cdots X_j\),
or \(X_j\cdots X_h\rho\); every longer exterior suffix/prefix contains the
same adjacent cell, proving sufficiency.

Thus (1.4) is the composition-safe context-free signature, while (2.4) is
the exact weaker signature for one frozen carrier.

## 3. The internal-window ledger

At depth \(q\), meaning interval length \(q+1\), a slot of length \(h\) has

\[
                         n_q(h)=\max\{h-q,0\}                     \tag{3.1}
\]

wholly internal windows.  Through depths \(1,\ldots,D\), their number is

\[
 \sum_{q=1}^D n_q(h)
   =rh-\frac{r(r+1)}2,\qquad r=\min\{D,h-1\}.                     \tag{3.2}
\]

For \(h=\Theta(d)\) and \(D\ge h-1\), this is \(\Theta(d^2)\).

The quadratic order is sharp even for constant-rank Johnson paths.  Take
\(|K|=r-2\), common endpoints \(K+a+b\), old interior cells
\(K+a+z_i\), and new interior cells \(K+b+z_i\), with the \(z_i\) distinct
and the endpoints/collars chosen so the first and last occurrences agree.
Every subinterval wholly in the \(h-2\) interior positions changes, giving
\((h-2)(h-1)/2\) changed internal intervals.

Therefore full boundary transparency justifies dependency **span**
\(D_m=O(h)\).  It justifies an \(O(dm^3)\) row-energy bound only if the
internal checks are support-private and already charged to the \(O(d)\)
physical support, or if their all-depth target state compresses to \(O(d)\)
additional tickets.

## 4. Exact signature-bad graph

For a parameterized equal-length replacement
\(X_{b,c}\leftrightarrow Y_{b,c}\), define

\[
 E(G_\Sigma)=
 \left\{(b,c):\exists x,\
 (f_{X_{b,c}}(x),\ell_{X_{b,c}}(x))
 \ne(f_{Y_{b,c}}(x),\ell_{Y_{b,c}}(x))\right\}.                  \tag{4.1}
\]

This is the exact context-free signature-failure graph.  A failed pair may
still pass the exterior-masked test (2.4), so \(G_\Sigma\) is a fail-closed
filter for one fixed context, not always the exact target-loss graph.

There is a useful unary specialization.  Suppose \(Y_{b,c}\) differs from
one fixed off-slot \(X\) only by deleting coordinate \(b\) at positions
\(I_b^-\) and adding coordinate \(c\) at positions \(I_c^+\).  Put

\[
 F_B=\{b:I_b^-\cap\{f_X(b),\ell_X(b)\}\ne\varnothing\},           \tag{4.2}
\]

\[
 F_C=\{c:I_c^+\not\subseteq[f_X(c),\ell_X(c)]\},                  \tag{4.3}
\]

where the interval is empty when \(c\) is absent from \(X\).  Then

\[
                         G_\Sigma=
 (F_B\times C)\cup(B\times F_C).                                  \tag{4.4}
\]

Indeed deleting an interior but nonextremal occurrence changes neither
first nor last occurrence, and adding inside the old first/last interval is
equally harmless; all other unary changes alter an extremum.  Consequently

\[
 |F_B|+|F_C|\le Kd
 \quad\Longrightarrow\quad
 |E(G_\Sigma)|\le Kmd.                                           \tag{4.5}
\]

This is the exact star-cover interface which a serialized buffered packet
would need to prove.

## 5. Raw anchored C6: only one safe insertion column

Fix \(C\subset U=C+a\), \(|C|=m\), choose \(b\in C\) and
\(c\notin U\), and consider the natural anchored C6 chronology

\[
 Z_{b,c}=(C,\ C+a,\ C-b+a,\ C-b+a+c,\ C-b+c,\ C+c).              \tag{5.1}
\]

Its prefix-union chain is

\[
                         C,\ U,\ U,\ U+c,\ U+c,\ U+c,             \tag{5.2}
\]

and, read from suffix length one upward, its suffix-union chain is

\[
                         C+c,\ C+c,\ U+c,\ U+c,\ U+c,\ U+c.       \tag{5.3}
\]

Both are independent of \(b\) and determine \(c\).

### Theorem 5.1 (fixed-slot C6 signature obstruction)

Relative to one fixed off-slot \(Z_{b_0,c_0}\), the signature-safe pairs are
exactly

\[
                         B\times\{c_0\}.                           \tag{5.4}
\]

Thus

\[
 G_\Sigma=K_{m,m-1},\qquad
 |E(G_\Sigma)|=m(m-1),\qquad
 \tau(G_\Sigma)=m-1.                                             \tag{5.5}
\]

#### Proof

Equations (5.2)--(5.3) show that changing \(b\) changes no signature entry.
The last cell \(C+c\), or the fourth prefix union \(U+c\), shows that equal
signatures force \(c=c_0\). \(\square\)

So the raw common-off-state C6 has \(m\), not
\(m^2-O(md)\), signature-safe choices when \(d=o(m)\).

### Theorem 5.2 (common-slot arrival lower bound)

Let \(X\) be one fixed off-slot starting at the source cell \(C\).  Suppose
each signature-safe candidate \(Y_{b,c}\) is a rank-preserving Johnson word
of length \(h\), starts at \(C\), and contains its selected
\(c\notin C\).  If at most \(Kmd\) of the \(m^2\) pairs are signature-bad,
then

\[
                              h\ge m-Kd+1.                         \tag{5.6}
\]

#### Proof

At most \(Kd\) complete \(c\)-columns can be bad, because each column has
\(m\) pairs.  Hence at least \(m-Kd\) columns contain a safe candidate.
Every safe candidate has the same total union as \(X\), so that common
union contains every corresponding \(c\).  A Johnson word beginning at
\(C\) introduces at most one coordinate outside \(C\) per transition.
Therefore \(h-1\ge m-Kd\). \(\square\)

For \(d=o(m)\), Theorem 5.2 rules out a fixed anchored \(O(d)\)-slot with
quadratic-minus-\(O(md)\) full-signature supply.  It does not rule out
candidate-dependent off-slots, the exterior-masked condition (2.4), a
non-Johnson/nonflat buffer, or a different atlas.

## 6. A signature-transparent fixed-4 serialization with one gap

Let \(H\) be a fixed core and let \(a,b,c,z\) be distinct outside it.  Put

\[
\begin{aligned}
 X^-={}&(H+ab,\ H+az,\ H+bc,\ H+bz,\ H+cz,\ H+ca),\\
 X^+={}&(H+ab,\ H+bz,\ H+cz,\ H+bc,\ H+az,\ H+ca).
\end{aligned}                                                     \tag{6.1}
\]

### Proposition 6.1 (abstract fixed-4 boundary transparency)

\[
                              \Sigma_\vee(X^-)=\Sigma_\vee(X^+).  \tag{6.2}
\]

Moreover the three pairs in positions \(12,34,56\) of \(X^-\) are one
matching phase of the fixed-4 incidence C6, and those of \(X^+\) are the
other phase.

#### Proof

The common prefix chain is

\[
 H+ab,\quad H+abz,\quad
 H+abcz,\quad H+abcz,\quad H+abcz,\quad H+abcz,                   \tag{6.3}
\]

and the common suffix chain, read from the end backward, is

\[
 H+ac,\quad H+acz,\quad
 H+abcz,\quad H+abcz,\quad H+abcz,\quad H+abcz.                   \tag{6.4}
\]

The old matching edges are

\[
 (H+ab,H+az),\quad(H+bc,H+bz),\quad(H+cz,H+ca),                   \tag{6.5}
\]

and the new ones are

\[
 (H+ab,H+bz),\quad(H+cz,H+bc),\quad(H+az,H+ca),                   \tag{6.6}
\]

which are precisely the two alternating C6 halves. \(\square\)

This is not yet a literal tight owner block.  In \(X^-\), the adjacency
\((H+az,H+bc)\) has Johnson distance two; in \(X^+\), the adjacency
\((H+bc,H+az)\) has Johnson distance two.  Every other internal adjacency
is a Johnson edge.  Thus a physical packet must buffer or export exactly
this antipodal seam while preserving (6.2), owner uniqueness, residence,
lower colours and common cap.

The identity proves that full boundary transparency is algebraically
compatible with an incidence C6.  It also isolates the smallest physical
chronology obstruction which the unordered resource theorem does not see.

## 7. ECO scope

The natural ECO ring

\[
 (H+a,\ H+a+b,\ H+b,\ H+b+c,\ H+c,\ H+c+a)                       \tag{7.1}
\]

has active first/last profiles

\[
 a:(1,6),\qquad b:(2,4),\qquad c:(4,6).                          \tag{7.2}
\]

Its reverse traversal changes these profiles, so the natural reversal is
not full-signature-transparent.

More generally, the existing ECO theorem supplies six ports and two
unordered matching phases.  After cutting a carrier, those ports delimit
global fragments whose lengths, orders and orientations depend on the
carrier.  Coherent turn-colour labels do not determine coordinate
first/last positions.  Hence no universal ECO bad-pair graph can be
computed from the six-port resource data alone; each proposed literal
serialization must pass (4.1), or the exact masked test (2.4), after its
opening and exterior are fixed.

## 8. Exact boundary for \(D=d\)

The replacement theorem removes every arbitrary-width **crossing** upper
row once a literal fixed-address full-signature packet is supplied.  To
deduce the protected row-energy hypothesis with \(D=d\), one still needs:

1. packet length \(h=O(d)\);
2. either \(O(d)\) total internal guard tickets, or support-private internal
   certification whose conflicts are already charged to the \(O(d)\)
   physical support;
3. residence, lower-palette, common-cap and topology tickets on the same
   serialization; and
4. a quadratic-minus-\(O(md)\) eligible list.

Theorems 5.1--5.2 show that Item 4 is false for the raw fixed-off C6
chronology when full context-free signature is demanded.  Proposition 6.1
shows a different fixed-4 serialization can meet the signature but leaves
one explicit antipodal seam.

Thus the weakest live positive construction is one of:

* a candidate-dependent off-slot whose fixed-4 serialization buffers that
  seam;
* an exterior-masked packet satisfying (2.4) on a prescribed carrier; or
* a nonflat connector which realizes Proposition 6.1 while retaining a
  quadratic eligible menu.

No current theorem supplies one of these together with the complete cap and
physical rows.  Full boundary signature is therefore a valid compression
principle, but the raw quadratic C6 menu does not yet instantiate it.

## 9. Scope audit

1. Signature equality preserves interval values and addresses, not merely
   the set of covered targets.
2. The cyclic theorem assumes one fixed proper slot; moving the opening is
   outside its scope.
3. The \(\Theta(d^2)\) internal count prevents the unsupported inference
   “\(O(d)\)-length slot implies \(O(d)\) all-depth windows.”
4. The raw-C6 no-go is for one common off-slot/signature.  It does not rule
   out candidate-dependent or context-masked packets.
5. Proposition 6.1 is an ordered-set identity.  Its one non-Johnson seam
   is not hidden or declared physical.
6. No equality theorem for \(\nu(k)\) or additive-constant upper bound is
   claimed.
