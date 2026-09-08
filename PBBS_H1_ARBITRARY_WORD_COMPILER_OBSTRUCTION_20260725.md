# A true arbitrary-word obstruction to a universal depth-one compiler

Date: 2026-07-25

Method: exact mathematics only.

## 0. Outcome

There is no universal theorem saying that an arbitrary cyclic Johnson
owner block with (S) owners has a set-valued contiguous-OR replacement
of length (S+O(H)) covering all owners, lower intersections, and upper
unions through depth (H).

The failure already occurs for (H=1).  An explicit rank-two cyclic
Johnson walk with (S=2R) owners has the property that **every** nonzero
set-valued OR word covering its depth-one data has length at least

\[
 \boxed{
 S+\frac{S}{24}.
 }
 \tag{0.1}
\]

The proof allows completely arbitrary helper letters and completely
arbitrary witness intervals.  It is not restricted to Pareto-path or
intersection letters.

Adding a fixed core lifts the example to every rank (k\ge2).

Thus any coefficient-one seam theorem must use extra structure of the
actual PBBS clusters (for example, the critical residence-gap tiling); it
cannot be a black-box theorem for all Johnson blocks.

## 1. The cyclic chain of stars

Fix (R\ge4).  Let

\[
 b_0,\ldots,b_{R-1},p_0,\ldots,p_{R-1}
\]

be (2R) distinct coordinates, with subscripts modulo (R).  Put

\[
 X_t=\{b_t,b_{t+1}\},
 \qquad
 Y_t=\{b_t,p_t\}.
 \tag{1.1}
\]

Consider the cyclic rank-two Johnson walk

\[
 X_0,Y_1,X_1,Y_2,\ldots,X_{R-1},Y_0,X_0.
 \tag{1.2}
\]

It has

\[
 S=2R
 \tag{1.3}
\]

owner occurrences before returning to (X_0).  The two transitions
through (Y_t) have the common lower colour

\[
 B_t=X_{t-1}\cap Y_t=Y_t\cap X_t=\{b_t\}.
 \tag{1.4}
\]

Their upper colours are

\[
 U_t^-=X_{t-1}\cup Y_t
       =\{b_{t-1},b_t,p_t\},
 \tag{1.5}
\]

and

\[
 U_t^+=Y_t\cup X_t
       =\{b_t,p_t,b_{t+1}\}.
 \tag{1.6}
\]

Thus the required depth-one target family consists of

* the (R) singletons (B_t);
* the (2R) owners (X_t,Y_t); and
* the (2R) triples (U_t^-,U_t^+).

All displayed targets are distinct, apart from the intentional double
occurrence of each lower colour in (1.4).

## 2. Canonicalizing an arbitrary OR word

Let

\[
 A=(A_1,\ldots,A_L)
\]

be any nonzero set-valued word representing every target above.  Choose
one witness interval (J_T) for every target (T).

First delete every position which lies in no chosen witness.  This does
not disturb any chosen interval: an interval spanning that position would
have used it.  After deletion, the chosen intervals merely compress.

For every remaining position (j), replace (A_j) by

\[
 A'_j=\bigcap_{T:\,j\in J_T}T.
 \tag{2.1}
\]

This intersection is nonempty because the old nonempty letter (A_j)
was contained in every target whose witness used (j).  Also

\[
 A_j\subseteq A'_j\subseteq T
 \qquad(j\in J_T).
\]

Hence every chosen witness still has union exactly (T): it gains no
coordinate outside (T), and it retains every coordinate which its old
letters supplied.  We may therefore assume from the outset that the word
is canonical in the sense of (2.1).

### Lemma 2.1 (mandatory positions)

Every canonical word contains, at distinct positions,

\[
 \{b_t\}
 \quad\hbox{and}\quad
 Y_t=\{b_t,p_t\}
 \qquad(0\le t<R).
 \tag{2.2}
\]

Consequently

\[
 L=2R+e
 \tag{2.3}
\]

for some (e\ge0), after selecting one such mandatory position of each
type; call all other positions **extra**.

#### Proof

The witness for the singleton (B_t=\{b_t\}) contains a nonempty
letter.  Canonicality and the presence of (B_t) among the intersected
targets force that letter to be exactly \(\{b_t\}\).

The witness for (Y_t) contains a position supplying (p_t).  The only
required targets containing (p_t) are

\[
 Y_t, U_t^-, U_t^+,
\]

whose intersection is (Y_t).  Hence canonicality makes that letter
exactly (Y_t).

Letters selected for two different (Y)'s are distinct because their
private coordinates differ.  A selected (Y_t)-letter cannot equal a
selected singleton letter.  Thus all (2R) positions are distinct.
\(\square\)

Order the selected (2R) mandatory positions as they occur in the word.

## 3. Direct targets and their order constraints

Count only the following (3R) targets:

\[
 \mathcal T=
 \{X_t:0\le t<R\}
 \cup
 \{U_t^-,U_t^+:0\le t<R\}.
 \tag{3.1}
\]

Call (T\in\mathcal T) **direct** when its chosen witness contains no
extra position.  Otherwise call it **bad**.

### Lemma 3.1 (necessary mandatory-order conditions)

If (X_t) is direct, the mandatory singleton positions

\[
 \{b_t\},\ \{b_{t+1}\}
\]

are adjacent in the mandatory-position order.

If (U_t^+) is direct, the mandatory positions (Y_t) and
\(\{b_{t+1}\}\) have between them, in the mandatory-position order, at
most the position \(\{b_t\}\).  Equivalently, their hull contains only

\[
 Y_t,\ \{b_t\},\ \{b_{t+1}\}.
 \tag{3.2}
\]

The symmetric assertion holds for (U_t^-), with (b_{t-1}) in place
of (b_{t+1}).

#### Proof

A mandatory (Y_s)-letter contains (p_s), so it is not a subset of
any (X_t).  Among mandatory singleton letters, only
\(\{b_t\}\) and \(\{b_{t+1}\}\) are subsets of (X_t), and both are
needed to supply its two coordinates.  A direct witness can therefore
contain no mandatory position between them.

For (U_t^+), the only mandatory letter supplying (p_t) is (Y_t),
and the only mandatory letter other than (Y_t) which can supply
(b_{t+1}) without an unwanted private coordinate is
\(\{b_{t+1}\}\).  The only third mandatory letter which is a subset of
(U_t^+) is \(\{b_t\}\).  This proves (3.2).  The minus case is
identical. \(\square\)

### Lemma 3.2 (one local incompatibility)

If both (U_t^-) and (U_t^+) are direct, then at least one of

\[
 X_{t-1},\ X_t
\]

is bad.

#### Proof

Suppose instead that both (X_{t-1}) and (X_t) are direct.  Lemma 3.1
forces the three singleton positions

\[
 \{b_{t-1}\},\ \{b_t\},\ \{b_{t+1}\}
\]

to be consecutive in this order or its reverse, with \(\{b_t\}\) in
the middle.

The distinct mandatory position (Y_t) cannot be inserted between the
first two or the last two without destroying one of those adjacencies.
If it lies outside the three-position block, then its hull with one end
of the block contains the other forbidden end: the hull with
\(\{b_{t+1}\}\) contains \(\{b_{t-1}\}\), or symmetrically the hull
with \(\{b_{t-1}\}\) contains \(\{b_{t+1}\}\).  Lemma 3.1 then says
that at least one of (U_t^-,U_t^+) is not direct, a contradiction.
\(\square\)

Let

\[
 a=\#\{t:X_t\text{ is bad}\},
 \qquad
 b=\#\{(t,\pm):U_t^\pm\text{ is bad}\}.
\]

At least (R-b) values of (t) have both upper targets direct.  By
Lemma 3.2 each such (t) is incident with a bad (X).  A bad (X_s)
is incident with only the two indices (t=s,s+1).  Hence

\[
 R-b\le2a.
 \tag{3.3}
\]

In particular,

\[
 \boxed{a+b\ge R/2.}
 \tag{3.4}
\]

## 4. One extra position can explain at most six bad targets

Every bad target has an extra position in its chosen witness.  Assign it
one such position.

At a canonical position (j), choose any coordinate in the nonempty
letter (A'_j).  Every target whose chosen witness contains (j) must
contain that coordinate.  Within the counted family \(\mathcal T\),

* a private coordinate (p_t) belongs only to (U_t^-,U_t^+);
* a coordinate (b_t) belongs to
  \[
  X_{t-1},X_t,
  U_{t-1}^+,U_t^+,
  U_t^-,U_{t+1}^-,
  \]
  exactly six targets.

Therefore one extra position can be assigned by at most six bad targets.
Together with (3.4),

\[
 6e\ge a+b\ge R/2,
\]

and hence

\[
 \boxed{
 L=2R+e\ge2R+\frac{R}{12}.
 }
 \tag{4.1}
\]

Since (S=2R), this is exactly (0.1).

## 5. Fixed-core lift and linear truncation

For any (k\ge2), take a fixed set (G) of size (k-2) disjoint from
all (b_t,p_t), and replace every owner (Z) above by (G\cup Z).
This is a cyclic rank-(k) Johnson walk with the corresponding
fixed-core lower and upper targets.

If a word represents the lifted targets, project every letter to the
active coordinates \(\{b_t,p_t\}\) and delete the resulting zero
letters.  Every witness remains a contiguous interval after zero-letter
deletion and has the required projected union.  The projected word is a
nonzero word for the rank-two family, so (4.1) applies.  Thus the same
lower bound holds at every rank.

Deleting (O(1)) owners and targets at one cut turns the cyclic walk into
a linear block and changes the counting inequalities by only (O(1)).
Hence linear truncations also require

\[
 L\ge \left(1+\frac1{24}\right)S-O(1).
 \tag{5.1}
\]

## 6. Exact boundary for the geometry programme

This example has only depth-one demands.  Its obstruction is the
alternation between

* a star owner (Y_t), whose two upper triples want (Y_t) locally
  adjacent to both neighbouring (b)-directions; and
* the boundary owners (X_{t-1},X_t), which want the three singleton
  lower colours in their own consecutive order.

The two local orders cannot all be direct.  Canonicalization makes every
failure consume a genuinely extra word position, and bounded coordinate
incidence turns the local failures into the linear bound (4.1).

Therefore neither diagonal Pareto sampling nor an unrestricted
facet/pin substitution can prove a universal (S+O(H)) Johnson-block
compiler.  A coefficient-one PBBS argument must exploit a property which
excludes this chain-of-stars pattern on almost all of the physical mass.
