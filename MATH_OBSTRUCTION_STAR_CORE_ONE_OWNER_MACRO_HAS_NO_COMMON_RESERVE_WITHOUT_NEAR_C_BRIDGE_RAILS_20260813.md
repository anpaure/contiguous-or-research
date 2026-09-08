# The star-core one-owner macro has no common reserve without near-C bridge rails

**Date:** 2026-08-13  
**Status:** unconditional separating-character theorem for the specific
insertion/star catalogue.  It rules out every coupled-order telescoping
which uses only the original insertion core and the star cores.  It does
not obstruct the full mixed-core rail semigroup.

## 1. The two compulsory owner shores

Use the notation of
`MATH_THEOREM_PURE_RAIL_ONE_OWNER_SIGNED_MACRO_AND_CONFORMAL_ABSORBER_GATE_20260812.md`.
Thus

\[
 H=C\mathbin{\dot\cup}P,\qquad |C|=c,\quad |P|=q,\quad x\in P,
\tag{1.1}
\]

and the point-corrected signed macro is

\[
 Y_H=\Delta_x+K,qquad
 K=\sum_{p\in P\setminus\{x\}}
       \bigl(\Phi_x^{(p)}-\Phi_p\bigr).             \tag{1.2}
\]

Choose \(P\subseteq S\subseteq[k]\setminus C\), \(|S|=c+1\), as in its
Theorem 3.1.  Every rail in \(\Delta_x\) has core \(C\), and every rail in
\(\Phi_u\) has core \(S\setminus\{u\}\).

After cancelling the compulsory occurrence \(H\) from
\(e_H-Y_H\), put

\[
 \mathcal B^+=Y_H^-,\qquad
 \mathcal B^-=Y_H^+-e_H.                            \tag{1.3}
\]

These are the two equal-size simple owner matchings with the same point
degrees from the cited theorem.

Let \(\mathfrak R_{C,S}\) be the catalogue of **all** legal pure closed
rails, of arbitrary legal period and cyclic toggle order, whose core is
one of

\[
                         C,\qquad \{S\setminus\{u\}:u\in S\}.
\tag{1.4}
\]

Thus this catalogue permits every possible recoupling of the toggle
orders in the original insertion/star cores; it is much larger than the
particular columns used in `(1.2)`.

## 2. A compulsory-owner character

For \(t\notin C\), define on the named-owner lattice

\[
 \chi_{C,t}(v)
   =\sum_{A\in{[k]\choose R}:\ C\cup\{t\}\subseteq A}v_A
       \pmod q.                                     \tag{2.1}
\]

It counts, modulo \(q\), occurrences which simultaneously contain the
old insertion core \(C\) and the petal label \(t\).

### Lemma 2.1

Assume \(c>q\).  Every column of \(\mathfrak R_{C,S}\) is annihilated by
every character `(2.1)`.

#### Proof

In a rail with core \(C\), a label \(t\notin C\) is either unused or a
toggle.  It therefore occurs in respectively zero or exactly \(q\) of
the cyclic \(q\)-window owners.  Its character is zero modulo \(q\).

Now take a rail with core \(S\setminus\{u\}\).  Since \(C\cap S=\varnothing\),

\[
 |C\cup(S\setminus\{u\})|=2c>c+q=R.                \tag{2.2}
\]

No rank-\(R\) owner can contain both cores.  Hence none of this rail's
owners is counted in `(2.1)`. \(\square\)

### Theorem 2.2 (no star-core common reserve)

For every \(t\in P\),

\[
                         \chi_{C,t}(\mathcal B^+)=0,
 \qquad                 \chi_{C,t}(\mathcal B^-)=-1\pmod q. \tag{2.3}
\]

Consequently there is **no** nonnegative owner vector \(R_H\) for which
both

\[
                         \mathcal B^++R_H,qquad
                         \mathcal B^-+R_H              \tag{2.4}
\]

are nonnegative sums of pairwise owner-disjoint columns from
\(\mathfrak R_{C,S}\).  In fact, `(2.4)` is impossible even if
owner-disjointness is dropped.

#### Proof

Every complete rail occurring in either sign of \(Y_H\) is annihilated by
Lemma 2.1.  The positive insertion rail contains the designated owner
\(H\), and \(H\) contains \(C\cup\{t\}\) for every \(t\in P\).  Therefore

\[
 \chi_{C,t}(Y_H^-)=0,qquad
 \chi_{C,t}(Y_H^+-e_H)=-1\pmod q,
\]

which is `(2.3)`.

If `(2.4)` had rail decompositions, Lemma 2.1 would give

\[
 \chi_{C,t}(\mathcal B^+)+\chi_{C,t}(R_H)=0
 =\chi_{C,t}(\mathcal B^-)+\chi_{C,t}(R_H),
\]

contradicting `(2.3)`.  No positivity or simplicity property was used in
this last subtraction. \(\square\)

The obstruction is independent of every cyclic order, insertion cut, and
packing choice for the repeated centre potentials.  Thus coupled toggle
orders cannot telescope the star by themselves.

## 3. Exact escape condition

The theorem is local to the star-core catalogue, as it must be: the full
mixed-core signed rail lattice is the complete named-owner lattice.
Nevertheless `(2.1)` identifies the first kind of new column which any
positive escape must use.

Let a rail have core \(D\), \(|D|=c\), and put

\[
                         a=|C\setminus D|.           \tag{3.1}
\]

If one of its owners contains \(C\), then the toggle window must contain
all of \(C\setminus D\), so necessarily

\[
                         a\le q.                    \tag{3.2}
\]

The case \(a=0\) is \(D=C\), whose character is already zero.  Therefore
a column capable of breaking `(2.3)` must have a genuinely new **near-C
bridge core** satisfying

\[
                         \boxed{1\le|C\setminus D|\le q.}      \tag{3.3}
\]

The star cores have \(|C\setminus(S\setminus\{u\})|=c>q\), so none is
such a bridge.  A positive construction must introduce near-C bridge
cores, or an equivalent larger mixed-core compound trade; merely changing
the orders in \(\Delta_x\) and the \(\Phi_u\) cannot work.

### Proposition 3.1 (the distance-one bridge realizes the missing residue)

Let

\[
                         D=C-\{a\}+\{s\},           \tag{3.4}
\]

where \(a\in C\), and let a legal period-\(N\) rail with core \(D\) have
both \(a\) and \(t\) as toggle labels, with \(t\ne s\).  If their directed
cyclic separation is \(\delta\in\{1,\ldots,N-1\}\), then

\[
 \chi_{C,t}(f(D,T,\sigma))
 =\max(0,q-\delta)+\max(0,q-(N-\delta))\pmod q.     \tag{3.5}
\]

In particular, placing \(a,t\) adjacently gives

\[
                         \chi_{C,t}=q-1=-1\pmod q.  \tag{3.6}
\]

#### Proof

An owner of this rail contains \(C\) exactly when its toggle window
contains the one missing core label \(a\).  Since \(t\) is also a toggle,
it is counted in `(2.1)` exactly when the same cyclic \(q\)-window contains
both \(a,t\).  The number of such windows is `(3.5)`.  The two positive
terms cannot occur simultaneously for a legal period
\(N\ge2(q+1)>2q\).  Adjacency gives `(3.6)`. \(\square\)

Thus `(3.3)` is not merely qualitative: a distance-one bridge core has the
right scalar residue.  What remains is to cancel its other named owners in
a simple compound trade; Proposition 3.1 alone is not a common-reserve
construction.

## 4. Finite diagnostic (not used in the proof)

For the smallest illustrative case \(q=2,c=3,M=8\), take one common
toggle order and insertion gap in the centre/leaf potentials.  Exact H100
enumeration of all supported legal period-6/7/8 rails gives:

* \(\mathcal B^+\) is exactly the union of the three original negative
  rails;
* \(\mathcal B^-\) has no exact closed-rail cover on its support;
* \(\mathcal B^-+e_H\) is exactly the union of the three original positive
  rails; and
* \(\mathcal B^++e_H\) has no exact closed-rail cover on its support.

This is the finite shadow of `(2.3)`: the compulsory owner lies on opposite
sides of the two natural closed-rail decompositions.  The symbolic
character theorem, not this census, is the all-parameter result.
