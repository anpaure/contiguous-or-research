# Unsaturated one-copy hinges and the protected-completion gate

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotors  
**Status:** unconditional literal owner/payload construction.  It removes the
saturated-state owner repeat from every strict lower chain at central rank at
least three.  It does not prove state balance, residence, upper transparency,
or an all-`k` one-copy factor.

## 0. Outcome

The literal hinge rectangles previously used for empty and proper-depth
chains have a saturated tail state: its `d` letters already union to the
rank-`r` owner.  Any internal predecessor rank-`r` window is then the same
owner, violating one-copy use.

That defect belongs to the chosen letter order, not to the target chain.
For every strict nonempty chain

\[
 \varnothing\ne S_1\subsetneq\cdots\subsetneq S_\ell\subsetneq T,
 \qquad 1\leq\ell\leq d,qquad |T|=r\geq3,            \tag{0.1}
\]

this note constructs a literal depth-`d` trace which

* has owner exactly `T`;
* has the prescribed chain as its last `ell` suffix unions;
* has both its tail and head `d`-state unions strictly below `T`; and
* contains a one-sided Cartesian tail menu of size `2^(|S_1|-1)`.

Empty chains have a two-sided-unsaturated singleton trace as well.  Thus the
hidden owner-repeat obstruction can be removed locally.  The price is that
the resulting hinge has only a fixed head; proving a global predecessor
matching, completed residence/upper interface, and connected Euler rounding
remains the exact gate.

## 1. A choice lemma

### Lemma 1.1 (filler and missing guard)

Let

\[
 \varnothing\ne S_1\subseteq S\subsetneq T,
 \qquad |T|\geq3.                                     \tag{1.1}
\]

There are `x in T` and `y in S_1` such that

\[
                         x\ne y,qquad S\cup\{x\}\ne T.       \tag{1.2}
\]

#### Proof

If `|T-S|>=2`, choose `y in S_1` and `x in T-S`; one added point cannot fill
the complement.  If `|T-S|=1`, then `|S|>=2`.  When `|S_1|>=2`, choose
distinct `x,y in S_1`.  When `|S_1|=1`, choose `y` as its unique member and
choose `x in S-S_1`.  In both subcases `x in S`, so `S union {x}=S<T`.
\(\square\)

## 2. The unsaturated nonempty-chain hinge

Put `S_0=emptyset` and `U=T-S_ell`.  If `ell<d`, choose `x,y` from Lemma
1.1 with `S=S_ell`.  If `ell=d`, choose any `y in S_1`; no filler `x` is
needed.

For every

\[
                         A\subseteq S_1-\{y\},         \tag{2.1}
\]

define nonempty letters `B_0,...,B_d` by

\[
 \begin{aligned}
 B_0&=U\cup A,\\
 B_t&=\{x\} &&(1\leq t\leq d-\ell,\quad \ell<d),\\
 B_{d-q+1}&=S_q-S_{q-1} &&(1\leq q\leq\ell).
 \end{aligned}                                        \tag{2.2}
\]

The filler and chain-layer index ranges are disjoint and cover positions
`1,...,d`.

### Theorem 2.1 (literal unsaturated one-sided rectangle)

Every word (2.2) is a legal trace with the following exact properties.

1. Its complete union is `T`.
2. For `1<=q<=ell`, its last `q` letters have union `S_q`.
3. Its tail-state union is

   \[
    \bigcup_{t=0}^{d-1}B_t=
    \begin{cases}
      (T-S_1)\cup A\cup\{x\},&\ell<d,\\
      (T-S_1)\cup A,&\ell=d,
    \end{cases}                                       \tag{2.3}
   \]

   and is a proper subset of `T` because it omits `y`.
4. Its head-state union is

   \[
    \bigcup_{t=1}^{d}B_t=
    \begin{cases}
      S_\ell\cup\{x\},&\ell<d,\\
      S_\ell,&\ell=d,
    \end{cases}                                       \tag{2.4}
   \]

   and is a proper subset of `T`.
5. As `A` ranges through (2.1), the literal order-`d` tail tuples

   \[
                         (B_0,\ldots,B_{d-1})          \tag{2.5}
   \]

   are distinct and the literal head tuple `(B_1,...,B_d)` is fixed.  Hence
   these traces form a Cartesian rectangle

   \[
                         \mathcal A_{T,C,y}\times\{h_C\},
    \qquad |\mathcal A_{T,C,y}|=2^{|S_1|-1}.          \tag{2.6}
   \]

   This cardinality concerns literal tuples.  The coarser union masks in
   (2.3) need not be distinct when `x in S_1-{y}`.

#### Proof

Every difference `S_q-S_(q-1)` and `U=T-S_ell` is nonempty, so all letters
are nonempty.  The union of `U` and the chain differences is `T`, proving
item 1.  The last `q` positions contain exactly the first `q` chain
differences in increasing-union order, proving item 2.

The tail omits the last letter `B_d=S_1`.  Its remaining chain layers union
to `S_ell-S_1`; adjoining `U`, `A`, and the filler gives (2.3).  Since
`y notin A`, `x!=y`, and `y in S_1`, the tail omits `y`.  The head omits
`B_0=U union A`; its union is (2.4), which is proper by Lemma 1.1 when a
filler exists and by `S_ell<T` otherwise.  Finally only `B_0` depends on
`A`; the map `A -> B_0=U union A` is injective because `U` is disjoint from
`S_1`.  Thus the literal tail tuples are distinct while the literal head
tuple is fixed.  \(\square\)

### Corollary 2.2 (the owner repeat is no longer forced)

Neither endpoint state in Theorem 2.1 already unions to the rank-`r` owner.
Therefore the saturated-state lemma does not force either adjacent owner
window to repeat `T`.

This is only removal of a necessary obstruction.  A predecessor or successor
state with a different owner must still be present in the global table.

## 3. Empty payloads

### Theorem 3.1 (empty-chain unsaturated trace)

Let `|T|=r>=3`, choose distinct `u,v in T`, and put

\[
 B_0=T-\{v\},\qquad B_t=\{u\}\ (1\leq t<d),
 \qquad B_d=\{v\}.                                    \tag{3.1}
\]

Then the trace has owner `T`, has no declared suffix payload, and has

\[
 \bigcup_{t=0}^{d-1}B_t=T-\{v\},
 \qquad
 \bigcup_{t=1}^{d}B_t=
 \begin{cases}
   \{v\},&d=1,\\
   \{u,v\},&d\geq2,
 \end{cases}                                          \tag{3.2}
\]

both proper in `T`.  Thus it is a singleton completed rectangle at the
owner/payload projection and avoids the forced repeat.

#### Proof

All letters are nonempty, their full union is `T`, and (3.2) is immediate.
For `r>=3`, `{u,v}` is proper.  \(\square\)

### Proposition 3.2 (sharp rank-two exception)

For `r=2` and `d>=2`, no nonempty-letter trace with owner `T` can have both
adjacent `d`-state unions proper in `T`.  For `d=1`, the trace
`({u},{v})` does.

#### Proof

Write `T={u,v}`.  If the tail union is proper, every one of
`B_0,...,B_(d-1)` must equal the same singleton.  If the head union is
proper, every one of `B_1,...,B_d` must equal a singleton.  Since `d>=2`,
the two blocks overlap in a nonempty letter, so the singletons agree.  The
full trace then has proper union, contradiction.  The depth-one example is
immediate.  \(\square\)

## 4. Protected-interface and Euler consequences

### Proposition 4.1 (one-step two-sided completion obstruction)

In the order-`d` de Bruijn graph, an arc has the form

\[
 (B_0,\ldots,B_{d-1})\longrightarrow(B_1,\ldots,B_d). \tag{4.1}
\]

Let a nonempty arc relation contain a Cartesian endpoint product
`A x H`.  Then every tail in `A` has one common `(d-1)`-letter suffix and
every head in `H` has that same common prefix.  If, in addition, the packet
has a fixed depth-one suffix target `S_1`, then `B_d=S_1` on every arc and
`H` is a singleton.  Dually, a fixed depth-one prefix target forces `A` to
be a singleton.

#### Proof

Fix one tail `a in A`.  Since `(a,h)` is an arc for every `h in H`, the
first `d-1` letters of every `h` equal the last `d-1` letters of `a`.  Thus
all heads have one common prefix and can differ only in their last letter.
A depth-one suffix target is exactly that last letter, so fixing it makes
all heads equal.  The reversed argument proves the dual assertion.
\(\square\)

Consequently Theorem 2.1 is optimally one-sided among single-transition
literal hinges carrying a fixed `q=1` payload.  A nontrivial two-sided
completed hinge must be a multi-edge macro, must move the payload address,
or must be handled as a genuinely correlated non-Cartesian relation.

The unsaturated hinge is deliberately only an owner/payload theorem.  To use
it in the protected one-copy result
`MATH_THEOREM_A_PROTECTED_HINGE_INTERFACE_AND_EULER_FUSION_20260802.md`, one
must still do all of the following on one common table.

1. Choose the guards `y` and fillers `x` so that the resulting tail lists
   and fixed heads satisfy the shifted Hoffman cuts.
2. Carry literal clipped run-age states.  Repeating the filler `x` can create
   a short internal run unless the boundary histories extend it or a
   residence-clean macro replaces the raw trace.
3. Assign every protected upper target a context-invariant occurrence or
   prove an exterior boundary-signature theorem.  Equations (2.3)--(2.4)
   alone do not preserve arbitrary-width interval unions.
4. Reserve a distinct-role connected skeleton and recheck the residual cuts,
   or exhibit protected colour-neutral `q`-fusions.

The exact positive implication is now:

\[
 \boxed{
 \begin{array}{c}
 \text{integral chain table + protected completion of the unsaturated hinges}\\
 \text{+ shifted Hoffman spanning-skeleton cuts}\\
 \Longrightarrow\text{ one-copy protected Euler carrier with zero sidecar.}
\end{array}}                                         \tag{4.2}
\]

The first line of (4.1), not local owner legality, is the remaining
construction theorem.  The corrected stationary pull clock supplies only
averaged fractional marginals and does not prove it.

## 5. Scope for `B(k)+O(1)`

The construction eliminates a previously hidden obstruction in the current
hinge route: short target chains no longer have to sit at a unique global
boundary merely to avoid repeating their owner.  It does not bound the
number of Euler components, because all rectangles are one-sided and their
fixed heads may have a Hall-deficient predecessor graph.  Nor does it make
`O(1)` components an `O(1)` sidecar; exact overlap distance remains
load-bearing.

Consequently this theorem is genuine one-copy progress but not a proof of
`B(k)+O(1)` or exact `B(k)`.
