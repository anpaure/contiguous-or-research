# Independent audit of the odd APH temporary-cart dichotomy

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_ODD_APH_TEMPORARY_CART_DICHOTOMY_20260806.md`  
**Audited SHA-256:**
`2dd6ce741910a23af7dd7a09aac47bb8d81bc13d47d4dd9c47df0ab97412e19e`  
**Method:** literal path, decoder, theorem-scope, and dependency audit; no
computation or search  
**Verdict:** **NO-GO.**  The resource dichotomy and the displayed endpoint
identities are correct, but the claimed occurrence-labelled APH construction
is not proved.  There are explicit intersections between paths belonging to
different sources, before any of the three global composition joins is used.
In addition, none of the three joins listed in Section 9 of the audited note
is supplied by the cited theorems.

This audit does **not** show that an odd APH construction is impossible.  It
shows that the proposed temporary-cart construction requires an early literal
branch/origin record and a protected-island bulk theorem before it may be
cited as APH.

## 1. Summary of the audit

The proof status of the individual rows is:

| Row | Status | Reason |
|---|---|---|
| Theorem 2.1, abstract word dichotomy | GO | The transition-matching and `BB` count are correct. |
| Paths (3.1)--(3.2), literal reachability | GO | Every displayed arrow is one adjacent unit transfer and all endpoints are correct. |
| Lemma 3.1, private-trail decoder | **NO-GO** | `H|M=0211` is also a strict state of the `B|H` swap; an explicit pair of sources meets there. |
| Lemma 4.1, two-atom assembly | **NO-GO** | It depends on Lemma 3.1 and does not install a physical atom-type/phase record. |
| Macros (6.3)--(6.12), endpoint algebra | GO as reachability identities | The block permutations and one-edge records have the stated endpoints. |
| Lemma 6.1, compound decoder | **NO-GO** | The lone-left-`B` branch meets the lone-right-`B` branch before the side record is written; the two orientations also meet at `HHHH` before `R_+`/`R_-` is written. |
| Teardown (7.1)--(7.6), endpoint algebra | GO conditionally | Reversal reaches the literal complemented source, provided a disjoint setup path and persistent phase record already exist. |
| Theorems 5.1, 7.1 and Corollary 8.1 | **NO-GO** | Their local decoder premises fail, and the three global scope joins remain unproved. |
| Claimed threshold (k\ge21) | **NO-GO for the fixed-collar application** | The count applies before reserving the two fixed collar blocks; after reserving them both the length and balance hypotheses change. |

## 2. The resource dichotomy itself is correct

The proof of Theorem 2.1 is valid as a statement about a linear word (w)
of length at least ten satisfying

\[
                         |\#A(w)-\#C(w)|\le1.
\]

If two transition edges of the reduced binary path do not share a vertex,
they are disjoint transition atoms.  If the transition-edge matching number
is at most one and both colours occur twice, the reduced path has exactly one
transition and hence has form (A^pC^q) or (C^pA^q), with (p,q\ge2).
The three gap bounds then give the advertised length-nine compound interval.
If one extreme multiplicity is at most one, the bound

\[
                 \sum_G\lfloor |G|/2\rfloor\le1
\]

does imply at most six `B` blocks and at most three extremes.  Thus a
length-ten counterexample cannot occur.

This proves only the abstract dichotomy.  Section 7 below explains why its
fixed-collar application does not inherit the same hypothesis.

## 3. Exact collision in the private-trail decoder

The four local paths displayed in (3.1)--(3.2) are literal.  However, their
state sets are not separated in the way required by Lemma 3.1.  In
particular,

\[
\begin{aligned}
 B|H &: 2002\to2011\to1111\to\boxed{0211}\to0220,\\
 M|H &: 1102\to1012\to0112\to0121\to\boxed{0211}=H|M.
\end{aligned}
\tag{3.1}
\]

Thus the endpoint `H|M` of the marked-gap swap is a strict state of the raw
`B|H` swap.  This is not merely a local overlap which an origin trail happens
to resolve.  It gives an exact global source collision.

Fix any (s\ge0), and append the same exterior word (Z) to the two equal
length, equal-charge sources

\[
             w_1=A B^s C B Z,
             \qquad
             w_2=A B^{s+1} C Z.
\tag{3.2}
\]

Bootstrap the displayed (A\cdots C) atom in each source.  The resulting
states are

\[
             H H M^s B Z,
             \qquad
             H H M^{s+1} Z.
\tag{3.3}
\]

Move the mobile head right.  In the first route, after the (s) private
marks have been crossed, take the first reverse edge of the raw-`B` path

\[
                          H|B=0220\to0211=H|M.
\]

The full state is then

\[
                         H M^s H M Z.
\tag{3.4}
\]

In the second route, cross only the first (s) private marks and stop at the
next macro checkpoint.  Its full state is the same word (3.4).  The two
sources in (3.2) are different, and one occurrence of (3.4) is a raw-sweep
strict state while the other is a private-trail checkpoint.

Consequently the stationary head and the visible length of the `M` trail do
not determine whether the last `M` is an old private mark or the first strict
state of a raw `B` crossing.  The phrase "excess over the recorded trail
length" in Lemma 3.1 assumes that the old trail length is independently
recorded; no such literal record is installed.

This disproves Lemma 3.1 as stated.  A valid repair must do at least one of:

1. write a literal phase/old-trail-length record before the mobile head
   leaves the atom;
2. replace the `B|H` and `M|H` paths by a globally disjoint, audited path
   family; or
3. carry an independently protected atom record which distinguishes (3.4).

An algorithmic branch name is not enough: the branch must be present in the
physical state.

## 4. The compound construction has two independent path collisions

The block endpoint identities (6.3)--(6.12) are algebraically correct, but
the records are written after information has already been erased.

### 4.1 The left/right lone-`B` branches meet before their side record

Consider the two valid `AACC` compound sources

\[
                    x=A B A C C,
             \qquad x'=A A C B C.
\tag{4.1}
\]

They respectively have

\[
 (u,v,w)=(1,0,0),
 \qquad
 (u,v,w)=(0,0,1).
\]

For (x), the first arrow of the special path (6.11) is

\[
                         A B A C C
                  \longrightarrow A B H H C.
\tag{4.2}
\]

For (x'), the standard middle bootstrap gives

\[
                         A A C B C
                  \longrightarrow A H H B C,
\]

and one completed rightward double-head swap through the `B` gives

\[
                         A H H B C
                  \longrightarrow A B H H C.
\tag{4.3}
\]

The states (4.2) and (4.3) are identical.  The records (6.10) and (6.12)
which were intended to remember the side of the lone `B` are written only
later, so they cannot separate this intersection.

### 4.2 The two orientations meet at `HHHH` before `R_+`/`R_-`

Take sources with the same exterior context and local intervals

\[
                              A A C C,
                  \qquad      C C A A.
\tag{4.4}
\]

The standard path and its reflected/complemented version both reach

\[
                                  H H H H
\tag{4.5}
\]

at (6.7).  The proposed orientation records

\[
                       R_+=H|M,
              \qquad   R_-=M|H
\]

are written by an edge **leaving** (4.5).  Hence (4.5) is already a common
internal vertex of two different source paths.  A record written after this
vertex cannot restore vertex-disjointness.

The sentence in Lemma 6.1 that the later record recovers the orientation
therefore does not prove the checkpoint at (4.5).  The orientation and the
lone-`B` side must be copied into a protected literal record before the
corresponding convergence, not afterward.

These two collisions disprove Lemma 6.1 and Theorem 7.1 as
occurrence-labelled path-bank statements.  They do not invalidate the
individual source-to-head and head-to-complement endpoint identities.

## 5. Composition join (i): protected zero-charge supports are not covered

The marked/LIFO theorem proves that, for the current cancellation pair,
every intervening block is in its allowed raw/tag alphabet.  Its load-bearing
invariant is that the interior consists of `B` blocks or previously written
tags.  It does not contain a theorem permitting the shuttle to jump over a
protected island containing `H`, `M`, `H|M`, or `M|H`.

Removing a zero-charge atom from the abstract (A/C) count preserves global
balance, but it does not make each physical component on the two sides of the
atom balanced.  For example, a remaining `A` to the left and a remaining
`C` to the right must be paired across the protected island.  The required
corridor then contains that island and violates the alphabet premise of the
marked rewrite.

Thus the instruction

> treat the two private origin trails as protected atom supports

is not an interface supplied by the marked/LIFO theorem.  Closing this join
requires one of the following additional results:

* a protected-island marked/LIFO theorem whose shuttle crosses each complete
  origin record with an occurrence decoder and restores it literally; or
* a selection theorem making every segment cut out by the protected supports
  separately charge-balanced, so no cancellation arc crosses a support.

Neither statement appears in the audited theorem or its cited dependencies.

## 6. Composition join (ii): cart transport across origin records is open

Lemma 6.1 of the visible-cart theorem allows the double head to cross words
over the macro and corridor alphabets.  `H` is deliberately outside those
alphabets.  The paragraph in Section 4 of the audited theorem observes that
three adjacent identical heads can be reinterpreted when an `HH` cart meets
an isolated `H`.  This is at most a macro convention; it does not establish
the required theorem for all origin records.

In particular:

1. the two-atom private decoder already fails at (3.4), before a cart crosses
   the record;
2. the compound records are `H|M` or `M|H`, not isolated heads;
3. crossing such a record moves the `M` and the indistinguishable head
   through the cart, so the allegedly stationary origin record is no longer
   at its old address; and
4. no literal phase state or decoder is supplied for the states in which the
   cart and origin head form a run of three or four `H` blocks.

Suppressing the duplicate `HHH` macro checkpoint does not prove that the
subsequent choice of which adjacent pair is the cart is occurrence-labelled
across different sources.  A separate sentinel-crossing theorem, covering
`H`, `H|M`, and `M|H` with the private origin address and phase in its literal
state, is required.

## 7. Composition join (iii): the fixed collar and temporary berth are not
## reserved by the dichotomy

The fixed-collar setup cited by the audited theorem starts with two named
literal collar blocks

\[
                              C(a)|C(b)
\]

and keeps them available until the protected setup writes the permanent
head.  Theorem 2.1, however, is applied to the entire suffix obtained only by
deleting the first connector.  It does not forbid either selected atom from
using one of the two fixed collar blocks.

If the fixed collar is removed before the resource theorem is applied, then
the proof's numerical hypotheses change:

* the available word has length (m-3), not (m-1); and
* deleting the first connector and two arbitrary collar blocks permits
  \(|\#A-\#C|\le3\), not the bound one in (1.2).

At the stated first value (m=11), (k=21), only eight blocks remain after
reserving the collar, so the length-ten theorem cannot be invoked.  Therefore
the claimed (k\ge21) APH scope is not established for the actual
fixed-collar geometry.

There are two further missing physical joins:

1. no indices are assigned to a two-block temporary berth which is disjoint
   from the fixed collar, `p_1`, both atom supports, and the fixed-collar work
   record; and
2. when the fixed-collar setup creates its own `HH`, the temporary `HH` and
   permanent `HH` coexist.  The cited visible-cart proof uses a unique
   maximal head run to locate its cart.  The audited theorem gives no literal
   phase/berth decoder for two separated runs or for one merged run of four.

Moreover Conditional Theorem 5.1 in the collar-first note ends with a head
at the fixed collar while keeping `p_1` fixed.  It does not, by itself, place
a "permanent connector-lattice double head at `p_1`" as asserted in step 3
of Section 5.  Transport from the fixed collar to the connector lattice and
the simultaneous retirement of the temporary cart need an explicit ordering
and decoder.

The intended schedule would indeed break the old logical cycle if all these
physical joins were proved: the temporary cart is sourced before the bulk,
the bulk creates the guardable checkpoint, and only then is the permanent
head written.  What is missing is not the high-level order but its literal
resource-disjoint realization.

## 8. Exact (k\)-scope and finite bases

For the unreserved (p_1)-punctured suffix, its length is (m-1), so the
abstract length-ten dichotomy starts at

\[
                         m\ge11,
                 \qquad  k=2m-1\ge21.
\]

That arithmetic is correct.  It is not the arithmetic of the protected
fixed-collar application, as Section 7 explains.

For an asymptotic same-parity (B(k)+O(1)) induction, finitely many excluded
dimensions may legitimately be absorbed into the constant once a valid
regenerative transition is proved; exact equality at each finite base is not
needed for that asymptotic statement.  This does **not** settle the exact
values at (k=17,19), and it does not repair the missing protected resource
theorem.  The audited note is correct to leave (k=17,19) outside its exact
scope, but its stronger statement that APH is closed for every (k\ge21)
does not follow.

## 9. Minimal proof-safe repair package

The current architecture can be salvaged only after the following are
proved in this order.

1. **Early atom record.**  Before moving a head away from an atom, record at
   least the atom type/orientation, the old private-gap length or an
   equivalent phase bit, and on the compound face the lone-`B` side.  The
   record must already be literal before the collision vertices (3.4),
   (4.2), and (4.5).
2. **Reserved-collar resource theorem.**  Prove a version of Theorem 2.1 on
   the suffix with `p_1` and the two named collar blocks unavailable.  Its
   hypotheses must allow the resulting imbalance up to three, and its
   threshold must be recomputed.
3. **Protected-island bulk theorem.**  Either make every exterior segment
   separately balanced or give literal shuttles across complete atom
   records.
4. **Sentinel/cart theorem.**  Give a source-disjoint decoder for an `HH`
   cart crossing `H`, `H|M`, and `M|H`, including all merged-head-run
   checkpoints.
5. **Two-head-bank schedule.**  Name disjoint temporary and permanent
   berths, prove their coexistence phase, transport the permanent head to the
   connector lattice, and retire the temporary atoms without invoking a
   theorem whose unique-head premise has been lost.

Only after these five rows are available do the already audited connector
beta and monotone post-beta terminal theorems compose.

## 10. Proof-safe conclusion

The correct conclusion at the audited SHA is

\[
 \boxed{
 \begin{array}{l}
 \text{abstract length-ten resource dichotomy: proved},\\
 \text{individual setup/teardown endpoint identities: proved},\\
 \text{occurrence-labelled temporary cart: not proved},\\
 \text{Anchored Pre-Head Bootstrap APH: open},\\
 \text{full odd package: still open at APH}.
 \end{array}}
\]

The explicit collision states above are exact corrections, not merely
requests for additional exposition.  Therefore Corollary 8.1 and the verdict
line claiming asymptotic APH closure must not be cited until the early-record
and composition repairs are supplied.
