# Independent audit: complete Bellman positivity through grid size five

**Date:** 2026-08-04  
**Verdict:** **GO.**  The current theorem is a valid formal corollary of
the frozen branch theorems.  The first-crossing and endpoint
normalizations are now applied in the necessary order, the least-maximizer
partition is exhaustive, and the two final size-three exits are exactly
the independently audited `R` and `P` gates.

## 1. Exact binding

Primary theorem:

`MATH_THEOREM_FIVE_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md`

SHA-256:

`69d8d73e52342a74d11a8673811e0d41d15063a2d66d1fdbc504138b4ed76bed`

Every dependency row in the theorem was independently hashed against the
current workspace bytes:

| role | SHA-256 |
|---|---|
| complete `n<=4` theorem | `1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9` |
| five-slot Apéry normal forms | `2ba2be5a52e4761790f031fcc63955c8066fd032fc3afaa81de866b50abd9b9e` |
| complete size-two branch | `a678fc5a33c6457d9d640aa963d902fdb8c7ed932ade6a14fd320caf8d285e43` |
| least-critical endpoint normalization | `7d897ac0600f9331f821fb1ca3a5d47483c67caf412b009d172fe8b365580f7f` |
| complete size-five branch | `db22119a59eae766e51c9461111f207342280309a3144fe43d0caf214c704027` |
| size-four boundary split | `332debcb96ff54fa47d9c85e153d9a36c01460ccbf9552ee20a2e73baee90c5b` |
| size-four active face | `9cee07d666ae51411550cfad13b8cb8f0ac8006e8968c5983583353dacb10722` |
| size-four inert faces | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
| size-three endpoint split | `1e15d736592bce3103786fb965f62fe6f028436c0d35b763b195157a2cf3d0b6` |
| delayed-endpoint concavity | `b494371c790ed20f14e29bd4beba67b27aa30f7f5b1447e4ef8da4e74db8ea14` |
| complete short-singleton gate | `8f7e7caecfbf873d7992e34349e3d3c3cc7968ae8e8691615d193d4afa8ef992` |
| complete long-singleton gate | `19f8a5a23cca1963e1914da28f609a56c9247f89422ee407e8e3aaa696654927` |

The current short-singleton rebind is independently frozen by audit SHA

`c0427eb680265563ffb85448a0a538d89a63c6421d668a847d9d09f05e6e3760`,

and the long-singleton Taylor/tangent theorem is independently frozen by
audit SHA

`d2c148f0f7c32ffcfb95a412f831877db8b2b4c29aa3472598a13fecab58f538`.

For a second structural cross-check, the earlier exact two-gate reduction
and its independent audit have hashes

`b7763d92d857ce811de7a0b2a9cc8e3b283e2f141536be9c3d176c47388708a6`

and

`43cfe0ebc5311bf956b2346dd84025db77cea023c49ec3ee159274fe4b6c15b9`,

respectively.

## 2. Contrapositive normalization order

Assume a five-slot table has nonpositive functional.

1. First-crossing deletion cannot leave a prefix of size at most four:
   that prefix would have positive functional by the complete four-slot
   theorem, whereas deletion is monotone in the proof-safe direction.
   Thus the reduced table satisfies

   \[
   c_1,c_2,c_3,c_4<A\le c_5.
   \]

2. Endpoint saturation replaces `c_5` by `max(A,P_5)` without increasing
   the functional, while preserving the prefix and first crossing.
   Therefore a hypothetical nonpositive table yields a nonpositive
   **saturated** first-crossing table.

3. Only after this saturation do we select the least maximum-density size
   among `2,3,4,5`.  This order is necessary because saturation may change
   the maximizing size, and it is now explicit in the audited theorem.

These three steps prove exactly the contrapositive reduction needed by
the final theorem; no inference from positivity of a lower bound is
reversed.

## 3. Exhaustiveness of the efficiency partition

Internal superadditivity gives

\[
                         c_2\ge2c_1.
\]

Hence, if size one is maximum-density, size two is maximum-density as
well.  Some size in `{2,3,4,5}` is therefore a maximizer, and choosing the
least such size partitions every saturated table into exactly one of four
branches.

If the restricted rule selects size five, then sizes two, three, and four
are not maximizers.  Size one cannot be one either, since that would force
size two to be one.  Thus size five is also the global least maximizer,
which is precisely the hypothesis needed by least-critical endpoint
normalization.  There is no mismatch between the restricted branch rule
and the size-five theorem.

## 4. Closure of the four branches

### Size two

The complete wedge theorem applies to every table for which size two is a
maximal-efficiency generator.  Its exact normal form is a strictly
positive two-state lattice plus two nonnegative finite corrections.  This
branch is unconditional.

### Size five

Global least-maximality forces `c_5=A`.  The literal endpoint-period lower
bound, not an eventual Apéry approximation, gives the strict margin
`1/400`.  Therefore all finite availability effects are already priced.

### Size four

Monotone endpoint normalization gives exactly

\[
 T_*=\max\{A,P+x,y+z\},
\]

so the active-maximum decomposition has precisely the faces

\[
 T=A,qquad T=P+x,qquad T=y+z.
\]

The active theorem closes the first with margin `199/2310000`.  The
compact Gaussian theorem closes both inert composite faces and explicitly
states the resulting complete size-four corollary.  Thus no fourth face
or unpriced finite head survives.

### Size three

The endpoint-split theorem closes `c_5=A` with margin `69/10000`.  On the
strict inert endpoint it proves an exact two-face reduction:

* the `w=y` face reduces, after its boundary minimization, to

  \[
  \mathcal R(a,\beta)=\mathcal L_3(a+2\beta;a,a+\beta)
  \]

  on

  \[
  0\le a\le\beta,qquad2a+2\beta<A<2a+3\beta;
  \]

* the `w=2a` face has the proof-safe lower bound `H(p,a,b)`.  Strict
  concavity in `b` reduces its minimum to the already-positive threshold
  endpoint or

  \[
  \mathcal P(p,a)=\mathcal L_3(p;a,2a)
  \]

  on

  \[
  0<a<A/4,qquad\max\{3a,A-2a\}<p<A-a.
  \]

The current short-singleton theorem proves `R>0` on its whole honest
domain.  Its corrected audit binds exactly the current bytes and confirms
that no false reverse-monotonicity step remains.  The current
long-singleton theorem proves

\[
 {\partial\mathcal P\over\partial p}>0
\]

on its whole domain using the exact jointly convex `q=1,2` block and the
global tangent margin `79/1750`; its two lower-period boundaries are
positive.  The independent Taylor audit verifies all sixteen rational
`h,h'` boxes, including the signs of negative derivative factors.

Consequently both final size-three exits are strictly positive.  The
delayed-endpoint concavity theorem then closes the retained-pulse face.

## 5. Logical conclusion and scope

Every hypothetical nonpositive five-slot table produces a nonpositive
saturated table in exactly one of the four branches above, while every
branch theorem proves that table strictly positive.  This contradiction
proves all five-slot tables positive.  Combining with the frozen
four-slot theorem proves the statement for every grid size at most five.

**GO:** the first possible finite Bellman separator has grid size at least
six.  This finite theorem does not prove the all-grid Bellman inequality,
`nu(k)<=B(k)+O(1)`, or the existence of the remaining integral carrier and
common-cap objects.
