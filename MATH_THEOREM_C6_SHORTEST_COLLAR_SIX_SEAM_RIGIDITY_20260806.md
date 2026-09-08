# The shortest antipodal C6 collar has six irreducible upper seams

## Status

The orientation-reversal identity correctly cancels two immediate-upper
value terms between consecutive prepared C6 ports.  The current literal
antipodal collar, however, cannot reduce the loss inside one isolated port.
Its six omitted extreme cells are pairwise distinct, and none is recreated
by the same splice.  The reason is exact: distinctness of the three far
lower roots forces three private far labels on each side, while the Boolean
C6 changes the active pair in the incompatible direction.

Together with the invariant-core theorem, this gives a sharp scope
boundary.  A four-current global connector cannot be obtained merely by
relabeling the present shortest collar.  It needs either a different
root-distinguishing normal form, a longer protected tensor, or a
base-changing cross-core adapter.  No computation or search is used.

## 1. Literal extreme rows

Work at owner rank `q` and owner-window width `h>=3`.  Let `J` have size
`q-h`, and choose pairwise disjoint banks

\[
 A=\{a_0,a_1,a_2\},\quad
 P=\{\rho_1,\ldots,\rho_{h-2}\},\quad
 \Lambda=\{\lambda_1,\ldots,\lambda_{h-2}\},          \tag{1.1}
\]

together with six far labels `x_0,x_1,x_2,y_0,y_1,y_2`, all disjoint from
`J,A,P,Lambda` and from one another.  These are exactly the typed labels of
the explicit period-`2h` antipodal C6 collar.

At cut `t in Z/3Z`, the two far rank-`(q-1)` roots are

\[
       Q_t^R=J\cup P\cup\{x_t\},\qquad
       Q_t^L=J\cup\Lambda\cup\{y_t\}.                 \tag{1.2}
\]

The two old immediate-upper extremes are

\[
 \begin{aligned}
 E_t^R&=J\cup P\cup\{a_t,a_{t+1},x_t\},\\
 E_t^L&=J\cup\Lambda\cup\{a_t,a_{t+1},y_t\}.
 \end{aligned}                                         \tag{1.3}
\]

Under the cyclic splice `left(t)->right(t+1)`, the corresponding new
values are

\[
 \begin{aligned}
 N_t^R&=J\cup P\cup\{a_t,a_{t+2},x_{t+1}\},\\
 N_t^L&=J\cup\Lambda\cup\{a_t,a_{t+2},y_t\}.
 \end{aligned}                                         \tag{1.4}
\]

All sets in (1.3)--(1.4) have rank `q+1`.

## 2. Root distinctness forces the far-token separation

### Lemma 2.1 (the two private triples are not optional in this normal form)

Within the common-base singleton-marker collar, the three right far roots
in (1.2) are distinct if and only if the `x_t` are pairwise distinct.
Likewise the three left far roots are distinct if and only if the `y_t`
are pairwise distinct.

#### Proof

On each side the root has one fixed common part and one displayed far
label.  Equality of two right roots is therefore equivalent to equality of
their far labels; the left side is identical. \(\square\)

Thus replacing all `x_t` by one common token would indeed protect the
right extreme upper multiset, but it would repeat a rank-`(q-1)` root.
The analogous attempted repair on the left repeats a left root.  Such a
replacement is unavailable in an exact one-copy owner/root factor.

## 3. Exact six-seam rigidity

### Theorem 3.1 (no same-port upper cancellation)

For the literal collar above,

\[
 \{E_t^R,E_t^L:t\in\mathbb Z/3\mathbb Z\}
 \quad\hbox{and}\quad
 \{N_t^R,N_t^L:t\in\mathbb Z/3\mathbb Z\}             \tag{3.1}
\]

are disjoint six-element sets.  Hence one isolated shortest C6 splice has
exactly six negative and six positive extreme immediate-upper values in
its signed occurrence ledger.  None of the six old extremes is transported
inside the same port.

#### Proof

First compare two right-side values.  If `E_t^R=N_s^R`, uniqueness of the
far labels gives

\[
                         x_t=x_{s+1},
\]

and hence `t=s+1`.  The old active pair is then
`{a_(s+1),a_(s+2)}`, whereas the new active pair is
`{a_s,a_(s+2)}`.  They are unequal because the three active labels are
distinct.  Thus no old right value is new right value.

If `E_t^L=N_s^L`, uniqueness of the `y` labels gives `t=s`.  The remaining
active pairs are `{a_t,a_(t+1)}` and `{a_t,a_(t+2)}`, again unequal.  Thus
there is no left-side cancellation.

Finally a right-side value contains every member of `P` and no member of
`Lambda`, while a left-side value contains every member of `Lambda` and
no member of `P`; all active and far labels are disjoint from both banks.
Since `h>=3`, both banks are nonempty, so no cross-side equality is
possible.  The same private labels and bank distinction show separately
that the six old values are distinct and that the six new values are
distinct. \(\square\)

### Corollary 3.2 (scope of the four-current target)

No relabeling which stays inside the present common-base,
singleton-marker, root-simple antipodal collar can lower the isolated port
demand from six to four.  In particular:

1. making a far triple constant repairs one upper side only by destroying
   exact lower-root multiplicity;
2. permuting the three private far labels cannot create an old/new equality;
3. reversing the active orientation creates cancellation only against a
   *later* port, not inside the same port.

#### Proof

Items 1--2 are Lemma 2.1 and Theorem 3.1.  Item 3 is the exact
orientation-reversal identity, whose primed old row equals the preceding
new row but is not part of the same splice. \(\square\)

## 4. Combination with invariant-core rigidity

The reversal telescope reduces a serial path of `m` literally realizable
ports to at most `4m+2` uncancelled negative value terms.  But whole-collar
regeneration preserves the antipodal invariant core.  Indeed, in this
normal form the two typed extreme bases are

\[
                         J\cup P,\qquad J\cup\Lambda,
\]

whose intersection is exactly `J`.  Thus even equality of both typed
extreme values recovers the same core.

It follows that the two available facts have complementary scopes:

* **isolated port:** six is sharp in the current root-simple collar;
* **serial same-core path:** four per port is attainable in the signed
  value ledger by orientation reversal;
* **global owner shore:** the same-core path cannot connect different
  invariant-core fibres.

The exact next object must therefore be one of the following.

1. A **base-changing adapter** which transports or cancels the two typed
   extreme currents while replacing core `J` by `J'!=J`.  The adapter must
   leave the disjoint-`P/Lambda` normal form, because their intersection
   recovers `J`.
2. A **different four-seam port** whose far roots are distinguished without
   six private singleton far labels.
3. A **core-cluster bridge system**: telescope within each coherent core
   cluster, and use a separate zero-charge protected connector family
   between clusters.

This is a structural obstruction, not a scalar one.  The exact upper
surplus is large enough for four current terms per port; what is missing is
a literal connector which achieves that efficiency while changing core.
