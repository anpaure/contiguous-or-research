# Private-order one-occurrence generator and the FSW reduction

**Date:** 2026-08-06  
**Method:** product-permutohedron involutions and orbit double counting; no
computation or search  
**Status:** **PARTIAL STRUCTURAL LEMMA ONLY -- DO NOT CITE the analytic
conclusion.**  The private one-occurrence involution and its projected
Johnson generator are useful and remain candidates for a corrected proof.
However this note inherited the type-unsafe `(FSW)` formulation: the
resource-layer resolvent cannot be applied to the scalar `(K_Tf)(A)`.
Sections 3--6 therefore do not close the Bellman row.  They must be rebuilt
as a bilinear comparison between the stopped covariance operator and the
stopped root-removal generator.

## 1. Trackwise private orders

In one atomic macro there is one lower fresh path and `h in {2,3}` owner
fresh paths.  The paths share the insertion order, but their deletion data
are private:

* the lower path uses its private deletion bank;
* owner copy `c` uses its private queue-tail order `R_c`.

Choose the canonical atomic template with these coordinate banks pairwise
disjoint, and disjoint between the two halves of a balanced doublet.  This
uses only `O(d)` labels inside a ground set of order `Theta(d^2)` and is
compatible with the macroscopically separated headers.  Outside its own
track, the two labels in one private adjacent transposition occur together
or not at all.

Fix every endpoint set, the shared insertion order, every other private
order, all slots, and the port data.  In one chosen track, transpose two
adjacent deletion events in positions `q,q+1`.

### Lemma 1.1 (one literal occurrence changes)

For `1<=q<d-1`, this involution changes exactly the track occurrence in
role `q`.  Its old and new values are Johnson adjacent.  Every other lower,
owner, marked, and slot occurrence of the atomic doublet is unchanged.

#### Proof

For the lower track this is item 1 of the product-permutohedron square
calculus: all prefixes before `q` contain neither deletion and all prefixes
after `q` contain both.  The same theorem records that a deletion-order
transposition changes no FIFO owner set.  The owner track is the identical
fresh-path formula with its private queue-tail deletion order in place of
the lower deletion order; its bank occurs in no other track.  A deletion
transposition changes neither the shared insertion order, port, mark, nor
slot.

Moreover the mate is not merely an abstract reordered word.  Globally
transpose the two private coordinate labels.  Every resource outside the
chosen track contains both or neither and is fixed, while the unique
intermediate resource contains exactly one and changes.  Hence both mates
belong to the actual complete coordinate orbit defining `B_h`, have the
same multiplicity `h`, and have the same base weight.  \(\square\)

Call these involutions **private switches**.  If `C,C'` are their two
atomic candidates, then

\[
             |C\mathbin\triangle C'|=2
\tag{1.1}
\]

on the occurrence-labelled non-slot host: one old resource is replaced by
one Johnson neighbour.

## 2. The projected generator is the Johnson Laplacian

Fix one resource rank and one interior role.  Take the complete coordinate
orbit of the endpoint sets, all shared insertion orders, and all private
deletion orders.  Give every adjacent private switch its inherited base
weight.

### Theorem 2.1 (exact projected Laplacian)

There is a scalar `alpha_T>0` such that, for every function `f` on the
resource layer,

\[
 {1\over Z_T}\sum_{(C,C')}
       w(C,C')\bigl(f(x(C))-f(x(C'))\bigr)^2
 =\alpha_T\langle f,L_Tf\rangle.
\tag{2.1}
\]

Here `x(C),x(C')` are the unique changed occurrences and `L_T` is the
normalized Johnson Laplacian.  Rescaling the switch measure makes
`alpha_T=1`.

#### Proof

Every projected pair is a Johnson edge by Lemma 1.1.  The complete
coordinate orbit makes its weighted directed-edge count invariant under
`Sym(k)`.  That group is transitive on directed Johnson edges, so every
edge has the same count.  The resulting Dirichlet form is therefore a
positive scalar multiple of the Johnson Dirichlet form.  At least one
private switch exists, so the scalar is positive.  \(\square\)

Candidate-level connectivity is not needed.  Although each private switch
stays inside a fixed endpoint fibre, the union over the complete endpoint
orbit projects onto every Johnson edge with equal multiplicity.

Combining (2.1) with `R_TL_T=B_T` gives the exact pristine resolvent
cancellation on the actual vector, with no slow-sector or dimension loss.
More explicitly, the private-switch form represents `L_T`, not `B_T`:

\[
 \langle f,R_T(\alpha_TL_T)f\rangle
       =\alpha_T\langle f,B_Tf\rangle.
\tag{2.2}
\]

After dividing the generator measure by `alpha_T`, this is precisely the
pristine FIFO covariance payment.  The argument applies separately to the
lower layer, to every owner-side layer, and to each side of an owner-union
form; the union form then uses the sum of its two side generators and
`(u+v)^2<=2u^2+2v^2` exactly as in Lemma 5.5 of the joint-Lyapunov note.

## 3. Stopping creates no unhit changed occurrence

Let `C,C'` be a private-switch pair which are both available immediately
before accepting `G`.  Suppose `G` kills `C'` but not `C`.  Their common
resources cannot meet `G`, since then both candidates would be killed.
By (1.1), `G` must contain the unique new resource of `C'-C`.

Consequently

\[
 \boxed{D_T(C,C')=J_T(C,C';G),\qquad |D_T|=1.}
\tag{3.1}
\]

The unhit term `Z_U` in `(FSW)` is identically zero.  Hence every private
switch boundary is paid by the already established one-entry rooted term
`(ROc)`; `(FE3)` is needed only when another independently priced
collision/marked entry occurs in the same transition.

This is stronger than an `O(d)` multiplicity argument: the full-change
obstruction vanishes literally on the private generator.

## 4. Composite future coefficients

Let `A=(Q,E,F)` (or its rooted analogue) be a composite row in which one
atomic component `E` undergoes a private switch, replacing the old resource
`x` by its Johnson neighbour `y`.  Put

\[
                 (\epsilon_x,\epsilon_y)
      =({\bf1}_{\{x\in F\}},{\bf1}_{\{y\in F\}}).
\tag{4.1}
\]

There are four exact cases.

1. For `(epsilon_x,epsilon_y)=(0,0)`, the intersection size, union size,
   and every root not equal to `x` are unchanged.  The composite future
   coefficients are equal.
2. For `(epsilon_x,epsilon_y)=(1,1)`, the intersection and union sizes are
   again unchanged.  If `x in Q`, transport that occurrence-labelled root
   to `y`; otherwise keep `Q`.  The transported composite coefficients are
   equal.
3. For `(epsilon_x,epsilon_y)=(1,0)`, one common resource disappears and
   one union-only resource appears.  If `x in Q`, the rooted row ends at
   this boundary; otherwise its coefficient changes by exactly the two
   future factors prescribed by the common-resource loss and union gain.
4. `(epsilon_x,epsilon_y)=(0,1)` is the reverse transition.

Cases 3--4 carry one named first-entry resource.  Expanding their future
factor difference is exactly the rooted-overlap polynomial `(5.3)`--`(5.5)`
and hence `(ROc)`; there is no unspecified coefficient ratio.  If the
transition simultaneously changes a second component/root incidence, its
two named entries are a summand of `(FE3.3)` (or Proposition 7.1 for a
marked cluster).  Thus coefficient equality is exact off the already
priced one-entry face, and every failure of equality has the literal
`(ROc)`/`(FE3)` coefficient.

The stopped boundary is one-sided.  In cases 1--2 the two composite rows
have the same literal resources except for `x` versus `y` (with the same
occurrence root transported in case 2).  A selected edge which kills only
the mate must contain its mate-side resource.  Cases 3--4 are already
removed into the rooted first-entry ledger.  Therefore (3.1) applies to
every unpriced composite boundary.

## 5. Endpoint and marked roles

Adjacent deletion switches change roles `1,...,d-2`; they do not change the
two path endpoints.  The first two insertion/mark roles and the terminal
fan also form only a constant number of roles per track.  These are exactly
the anchored entry patterns isolated in the parent proof:

* penultimate/terminal owner fans use `(TF1)--(TF3)` in Section 5.5 of the
  rank-compensated note;
* fixed marked clusters of size two or three use Proposition 6.2 and the
  marked first-two-hit Proposition 7.1 of the joint-Lyapunov note;
* slot occurrences use Proposition 5.3 of the rank-compensated note;
* the remaining unmarked first/last lower and owner occurrences use the
  constant-role scalar estimate (5.1) below.

Therefore a complete proof of the raw stopped row follows if the parent
anchored ledger is interpreted occurrence-wise for these constant endpoint
roles, while Theorems 2.1 and (3.1) handle every interior role.

There is also a direct scalar proof for the unmarked endpoint part.  If a
template fragment contains at most `s_0=O(1)` endpoint occurrences, then

\[
       \left(\sum_{j=1}^{s_0}f_{x_j}\right)^2
       \le s_0\sum_{j=1}^{s_0}f_{x_j}^2.
\tag{5.1}
\]

After summing the composite weights, the right side is the first-incidence
root energy with only constant role multiplicity.  Its centered part is
absorbed by the already present root contraction; coefficient changes at a
common endpoint are one-entry `(ROc)` terms, and two common endpoints are
`(FE3)`.  Thus the degree-one/degree-two slow-path obstruction cannot occur
on the endpoint fragment: its word length is constant, not `Theta(d)`.

Thus every excluded role is mapped to a numbered existing row or to the
explicit constant-role inequality (5.1); there is no unnamed endpoint
family.

## 6. Conditional conclusion

Under that endpoint-ledger identification, the full-change residual
`(FSW)` vanishes on all interior roles and is already priced on the
constant exceptional role family.  The raw Johnson Bellman value is then
`O(M/d^4)`, and the existing stopped-transfer chain yields

\[
                 \mathbb E(B_0+B_1)=O(M/d^2).
\tag{6.1}
\]

The load-bearing audit questions are now finite and explicit:

1. verify that every owner track really has an independently swappable
   private deletion/queue order in the atomic doublet host;
2. verify the occurrence-weight normalization in (2.1) simultaneously for
   lower, owner-side, and owner-union forms;
3. check that every endpoint role is in the already proved anchored/fan
   ledger, rather than merely being a constant unpriced family.

No global coordinate-transposition FSW estimate is needed if these three
rows pass.
