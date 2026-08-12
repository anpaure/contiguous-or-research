# APH audit: two head atoms exist, but only a stationary origin head breaks the collision

**Date:** 2026-08-06  
**Scope:** the Anchored Pre-Head Bootstrap lemma isolated in
`MATH_AUDIT_ODD_PACKAGE_DEPENDENCY_CLOSURE_20260806.md`  
**Method:** exact cyclic-word matching and literal capacity-two paths; no
computation or search  
**Verdict:** the raw resource is abundant: two disjoint zero-charge head
atoms exist in every sufficiently long balanced connector cycle.  A second
fixed \(H|H\), however, does **not** occurrence-label a mobile adaptive
\(H|H\); the old `ACB/BAC` collision embeds unchanged.  Leaving one member
of the mobile pair stationary at its own origin does break that collision,
and its single mobile head has explicit source-disjoint transport through the
raw alphabet \(\{A,B,C\}\).  The exact remaining APH row is extension past
the first previously written non-source block, or an injective persistent
origin marker installed before both heads leave.

## 1. Zero-charge atoms

Put

\[
                         A=00,\qquad B=20,\qquad C=22,
                         \qquad H=02,\qquad M=11.
\tag{1.1}
\]

A **transition atom** is a cyclic segment

\[
                         A B^s C\quad\hbox{or}\quad C B^s A.
\tag{1.2}
\]

The literal paths in the source-internal bootstrap turn it into \(H|H\)
plus a recorded \(M^s\) gap.  A **neutral atom** is an adjacent \(B|B\),
which has the literal path

\[
                         20|20\leadsto02|02.
\tag{1.3}
\]

Both atoms have zero signed connector charge and preserve total mass.

### Lemma 1.1 (two disjoint atoms)

Let \(w\) be a cyclic word over \(\{A,B,C\}\) with \(\#A=\#C\).  If
\(|w|\ge5\) and \(w\) is not one of the finite degenerate words supported on
fewer than four blocks, then \(w\) contains two block-disjoint zero-charge
atoms.

#### Proof

Let \(p=\#A=\#C\), and delete the \(B\)'s.

If \(p\ge2\), the reduced cyclic binary word has at least two transition
edges.  If it has exactly two, it is \(A^pC^p\) cyclically, and the two
transition edges are vertex-disjoint because \(p\ge2\).  If it has more
than two, its transition-edge subgraph on a cycle has a matching of size at
least two.  Reinsert the disjoint \(B\)-gaps.  The two matched transitions
give disjoint atoms of type (1.2).

If \(p=1\), the two extremes split the \(B\)'s into two cyclic gaps.  Since
\(|w|\ge5\), one gap contains at least two \(B\)'s.  Use the transition atom
through the other gap and a \(B|B\) atom inside the longer gap.

If \(p=0\), the word is all \(B\), and four of its blocks give two disjoint
neutral atoms.  \(\square\)

This is an unpunctured resource lemma.  If the active first connector is
forbidden, the selected atoms must additionally avoid that occurrence.
For a long suffix this follows after reserving one further local choice, but
the punctured statement is not needed for the no-go below and is not claimed
here.

## 2. A second fixed double head does not label the mobile origin

It is tempting to convert one atom to a permanently fixed \(H|H\), convert
the second atom to a mobile \(H|H\), and use the former as the origin label
of the latter.  This fails.

### Proposition 2.1 (embedded adaptive-berth collision)

Fix an identical literal \(H|H\) atom outside a three-block window.  In the
window take the two balanced sources

\[
                         ACB,\qquad BAC.
\tag{2.1}
\]

Their mobile bootstraps are

\[
                         HHB,\qquad BHH.
\tag{2.2}
\]

Move the first mobile double head one block toward a fixed collar on the
right.  It reaches \(BHH\), exactly the second source's mobile-bootstrap
checkpoint, while the remote fixed \(H|H\) is unchanged.  Thus the two full
states collide.

#### Proof

The local identities are the source-internal bootstrap and one literal
double-head block interchange.  Tensoring both routes with the same remote
fixed head and the same exterior word preserves equality at the collision.
The motion is toward the fixed right collar, so ordering the mobile atom by
distance from that collar does not exclude the example.  \(\square\)

Consequently two disjoint head atoms prove resource supply, not
occurrence-labelled mobility.  A marker must remember the **mobile** origin.

## 3. One stationary member does remember the mobile origin

Create one adaptive \(H|H\), but leave the member farther from the fixed
collar at its original physical coordinate.  Move only the nearer \(H\)
monotonically toward the collar.  At a macro checkpoint, the farther of the
two ordered \(H\)-positions is the stationary origin and the nearer is the
mobile head.

The following three paths move a mobile head left through one raw connector;
their reverses move it right:

\[
\begin{array}{rcl}
A|H:&0002\to0011\to0101\to0110\to0200&=H|A,\\
B|H:&2002\to2011\to1111\to0211\to0220&=H|B,\\
C|H:&2202\to2112\to1212\to1122\to0222&=H|C.
\end{array}
\tag{3.1}
\]

Every arrow is one adjacent unit transfer.  At every strict state, the
active four-coordinate word contains a value outside the raw source alphabet
\(\{A,B,C\}\).  In the middle line the possible active \(H\) is adjacent to
an active \(M\), so it is not confused with the isolated stationary origin
head.

### Theorem 3.1 (anchored single-head transport on a raw interval)

Suppose the interval between an adaptive head atom and the fixed collar is
still literal over \(\{A,B,C\}\).  Leave one \(H\) stationary at the atom,
and move the other monotonically through that interval using (3.1).  The
resulting paths are occurrence-labelled and pairwise source-disjoint.  They
preserve the active first selected row whenever the interval is disjoint
from \(p_1\).

#### Proof

At every macro checkpoint there are two ordered heads: the farther one is
the stationary origin and the nearer one is the mobile head.  The atom type
and orientation, retained in the finite setup record, recover the two source
blocks at that origin.  Reversing the completed block swaps recovers the raw
source interval and the number of completed crossings.

At a strict state the stationary head remains literal.  Outside its fixed
origin neighbourhood, the only non-source block or pair is the active strict
state listed in (3.1).  It therefore locates the active four-coordinate
window.  Its total mass chooses one of the three rows, and simplicity of that
row chooses the microstep.  Equality of two global states forces equality of
origin, direction, active address, row, and microstep, and then equality of
source.

If the whole interval lies after the active \(p_1\) support, every physical
edge is eligible for the existing shadow-clock lift and the selected row is
unchanged as an unordered row.  \(\square\)

The collision (2.1) is now separated.  In its first route the stationary
head remains at the first block of the old `AC`; in its second route it
remains at the second physical block.  The two literal states can no longer
be equal.

## 4. Why this still does not prove APH

Theorem 3.1 assumes that, away from the fixed origin atom, the crossed tape
is raw.  The first protected residual conversion writes \(M=11\), and the
bulk pair conversion writes \(01/21\) tags.  Those values can coincide with
the active strict markers in (3.1).  After one such write, the proof's
"unique non-source active window" sentence is no longer valid.

There are two proof-safe ways to finish APH:

1. **Persistent origin marker.**  Before reuniting or moving both heads,
   write a bounded injective marker at the mobile atom's physical origin and
   prove a marked-trail decoder through the enlarged tape alphabet.
2. **Anchored catalyst transducer.**  Give literal swap paths for the mobile
   single head through every state exported by the setup, together with a
   trail code whose boundary locates the active path even when the same
   non-source values occur elsewhere.

A second unmarked fixed \(H|H\) is not such a marker by Proposition 2.1.

## 5. Exact APH frontier

The remaining statement is now narrower than arbitrary fixed-head creation:

> Starting from the anchored single-head state of Theorem 3.1, perform the
> protected residual and \(G_1\) half-payments while the stationary origin
> head remains fixed, and either (i) create the source-independent fixed
> \(H|H\) cart, or (ii) export a persistent origin trail which makes the
> reunited adaptive \(H|H\) a valid moving cart.  Every strict state must
> decode the active address after previously written \(M\) and \(01/21\)
> values are present.

The mass and resource rows are not the obstruction: Lemma 1.1 supplies two
atoms and the zipper ledger balances all payments.  The sole missing content
is this enlarged-alphabet occurrence decoder.  Therefore APH, and hence the
full odd package, remains open at exactly that row.

