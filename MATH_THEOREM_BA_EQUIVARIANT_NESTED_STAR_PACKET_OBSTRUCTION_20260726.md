# Exact obstruction to a three-orbit equivariant nested-star packet

Date: 2026-07-26

Method: coordinate dynamics and directed-window reconstruction.  No
computation or finite search is used.

## 1. Statement

Let

\[
 n=2m+1,
 \qquad
 C=BA,
 \qquad
 L=m(m+1),
\]

and let a permutation state be written as a word
\(\pi=(x_1,\ldots,x_n)\).  Thus

\[
 C(x_1,\ldots,x_n)
   =(x_3,x_4,\ldots,x_{n-1},x_1,x_n,x_2).
\tag{1.1}
\]

Put

\[
 J=\{m+2,m+3,\ldots,2m\}.
\tag{1.2}
\]

This is the ordered common-suffix interval in the canonical nested-star
atom of Proposition 2.8 of
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`.

### Theorem 1.1 (synchronized equivariant packet obstruction)

For every \(m\ge3\), there are no three permutation states
\(\pi_1,\pi_2,\pi_3\), from distinct \(C\)-orbits or otherwise, such
that

\[
       (C^t\pi_1,C^t\pi_2,C^t\pi_3)
\]

is a canonical nested-star source triple for every
\(t\in\mathbb Z_L\).

In fact, if two states \(\pi,\pi'\) satisfy

\[
 (C^t\pi)|_J=(C^t\pi')|_J
       \qquad\text{for every }t\in\mathbb Z_L,
\tag{1.3}
\]

then \(\pi=\pi'\).

Thus the proposed packet consisting of three full \(BA\)-orbits with
equal-phase triples is exactly impossible.  The obstruction occurs
before the owner rows or the endpoint orientation are imposed.

For odd \(m\) there is a stronger statement which also rules out an
arbitrary rematching of phases.

### Theorem 1.2 (arbitrary phase-rematching obstruction)

Let \(m=2r+1\ge5\).  Let \(O_1,O_2,O_3\) be three \(C\)-orbits of
permutation states.  It is impossible to partition

\[
                      O_1\sqcup O_2\sqcup O_3
\]

into \(L\) canonical nested-star source triples, each containing one
state from each \(O_i\), unless

\[
                         O_1=O_2=O_3.
\]

In particular no such partition exists for three distinct orbits.
This remains true if the orientation and the three endpoint labels of
the star are allowed to vary independently from triple to triple.

Theorem 1.2 independently verifies and slightly reframes Proposition
4.5 of
`MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md`.

## 2. Exact coordinate criterion for one canonical atom

We first isolate exactly what must be preserved by an equivariant
packet.

### Lemma 2.1 (necessary and sufficient coordinate criterion)

Let \(\pi_1,\pi_2,\pi_3\) be permutation states on \([n]\).  They are
the three sources of a canonical nested-star atom if and only if, after
cyclically indexing the states and choosing distinct labels \(a,b,c\),
the following hold.

1. Their ordered restrictions to \(J\) agree:
   \[
         \pi_1|_J=\pi_2|_J=\pi_3|_J=\mathbf K.
   \tag{2.1}
   \]

2. Their ordered endpoint pairs are
   \[
   (\pi_1(1),\pi_1(n))=(a,b),\quad
   (\pi_2(1),\pi_2(n))=(b,c),\quad
   (\pi_3(1),\pi_3(n))=(c,a).
   \tag{2.2}
   \]

3. At the last position of the middle block,
   \[
       \pi_1(m+1)\ne c,\qquad
       \pi_2(m+1)\ne a,\qquad
       \pi_3(m+1)\ne b.
   \tag{2.3}
   \]

The reverse cyclic orientation is included by interchanging \(b,c\).

#### Proof

Necessity is immediate from the normal form

\[
 (a,P_{ab},\mathbf K,b),\qquad
 (b,P_{bc},\mathbf K,c),\qquad
 (c,P_{ca},\mathbf K,a),
\tag{2.4}
\]

where the three \(P\)-blocks end in the common set \(R\).

Conversely, let \(K\) be the label set of \(\mathbf K\), and set

\[
 R=[n]\setminus(K\cup\{a,b,c\}).
\]

The endpoint labels do not belong to \(K\), because each occurs outside
\(J\) in one of the permutation states.  Hence \(|R|=m-1\).  Since
every \(\pi_i\) is a permutation, its positions \(2,\ldots,m+1\)
contain respectively

\[
 R\cup\{c\},\qquad R\cup\{a\},\qquad R\cup\{b\}.
\]

Condition (2.3) says precisely that the final entry of each of these
three blocks lies in \(R\).  Thus (2.4) is the canonical normal form of
Proposition 2.8. \(\square\)

Only condition (2.1) is needed for both obstructions below.

## 3. Synchronized phases expose the whole state

Write (1.1) as

\[
                    (C\pi)(j)=\pi(\sigma(j)),
\]

where \(\sigma\) has the two position cycles

\[
 P=(1,3,5,\ldots,2m-1),
 \qquad
 Q=(2,4,6,\ldots,2m,n).
\tag{3.1}
\]

Their lengths are \(m\) and \(m+1\), respectively.

### Lemma 3.1 (suffix observability)

For \(m\ge3\),

\[
                  \bigcup_{t\in\mathbb Z_L}\sigma^t(J)=[n].
\tag{3.2}
\]

#### Proof

The interval \(J\) has length \(m-1\ge2\), so it contains two
consecutive positions and therefore meets both cycles in (3.1).
The translates of any one position under \(\sigma\) cover its whole
cycle.  Translating the two nonempty intersections \(J\cap P\) and
\(J\cap Q\) consequently covers \(P\cup Q=[n]\). \(\square\)

#### Proof of Theorem 1.1

If (1.3) holds, then for every \(j\in J\) and every \(t\),

\[
 \pi(\sigma^t(j))=(C^t\pi)(j)
                  =(C^t\pi')(j)=\pi'(\sigma^t(j)).
\]

Lemma 3.1 implies equality at every coordinate, so \(\pi=\pi'\).

If three equal-phase translates formed a canonical atom at every phase,
Lemma 2.1 would give (1.3) for each pair of base states.  All three base
states would therefore be equal.  This contradicts (2.2), which uses
three distinct endpoint labels. \(\square\)

The same proof permits fixed phase offsets: replacing \(\pi_i\) by
\(C^{s_i}\pi_i\) shows that three orbitwise affine alignments
\(C^{t+s_i}\pi_i\) cannot work either, unless the aligned states are
identical.

## 4. Arbitrary phase matchings retain a directed-window invariant

For a state \(\pi\), define its ordered suffix deck

\[
 \mathcal D(\pi)=
 \bigl\{(C^t\pi)|_J:t\in\mathbb Z_L\bigr\},
\tag{4.1}
\]

with multiplicity.  Suppose \(m=2r+1\).  The intersections
\(J\cap P\) and \(J\cap Q\) are each a directed interval of length
\(r\) in the corresponding cycle (3.1).

Read the labels of \(\pi\) around those two position cycles as cyclic
sequences

\[
 A=(a_0,\ldots,a_{m-1}),qquad
 B=(b_0,\ldots,b_m).
\tag{4.2}
\]

Since \(\gcd(m,m+1)=1\), the powers \(t\in\mathbb Z_L\) realize every
pair of shifts \((u,v)\in\mathbb Z_m\times\mathbb Z_{m+1}\).  Hence

\[
 \mathcal D(\pi)=
 \left\{
   \operatorname{interleave}
   \bigl(A[u,u+r),B[v,v+r)\bigr):
   (u,v)\in\mathbb Z_m\times\mathbb Z_{m+1}
 \right\}.
\tag{4.3}
\]

### Lemma 4.1 (deck rigidity)

If \(r\ge2\) and
\(\mathcal D(\pi)=\mathcal D(\pi')\) as multisets, then \(\pi'\) is
a power of \(C\) applied to \(\pi\).

#### Proof

Project each word of (4.3) onto the positions inherited from \(P\).
The resulting multiset is the deck of all directed length-\(r\)
windows of \(A\), each repeated \(m+1\) times.  The analogous projection
onto the \(Q\)-positions gives the length-\(r\) window deck of \(B\),
each repeated \(m\) times.

For a cyclic sequence of distinct labels, its directed window deck of
length at least two determines its directed cyclic order: the unique
window whose first entry is a given label records that label's unique
successor in its second entry.  Thus equal suffix decks force the two
\(P\)-cycle sequences to differ only by a rotation, and likewise for
the two \(Q\)-cycle sequences.

Any prescribed pair of rotations modulo \(m\) and modulo \(m+1\) is,
by the Chinese remainder theorem, induced by one power of \(C\).
Therefore \(\pi'\in\langle C\rangle\pi\). \(\square\)

#### Proof of Theorem 1.2

In every canonical nested-star triple, the three ordered suffixes are
equal by Lemma 2.1.  A partition using every state once therefore
induces, between any two participating orbits, a bijection preserving
the ordered suffix word.  Their suffix decks are equal as multisets.
Lemma 4.1 then says the two orbits coincide.  Applying this to both
other orbit pairs yields \(O_1=O_2=O_3\). \(\square\)

## 5. Exact boundary of the obstruction

This theorem rules out the smallest explicit way to intersect the
owner matching with exact circulation:

* three full \(BA\)-orbits cannot be bundled into an equivariant atom
  packet;
* allowing arbitrary phase bijections among those three orbits does
  not help for odd \(m\ge5\);
* fixed phase offsets, reflections, or independent rotations of the two
  position cycles do not help, because the full ordered suffix deck
  remembers both directed cyclic orders.

It does **not** obstruct an orbit-level factor using a growing family of
orbits in which each orbit meets many different orbit triples.  Nor does
it obstruct a protected-height atom that shares only a truncated suffix
flag rather than the full \((m-1)\)-letter ordered suffix.  Those are the
minimum surviving forms of the matching-circulation intersection.

