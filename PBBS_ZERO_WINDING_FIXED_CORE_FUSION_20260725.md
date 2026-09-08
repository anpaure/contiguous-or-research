# A linear literal fusion word for a genuine PBBS zero-winding sector

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

A genuine zero-winding PBBS return of gap \(2s+1\) has the exact owner
structure proved in
\`PBBS_ZERO_WINDING_OWNER_WREATH_STRUCTURE_20260725.md\`.  After choosing
one step-two parity and complementing if necessary, an open nonwrapping
sector consists of owners

\[
 Y_j=K\cup I_j,
 \qquad 0\le j\le s,
\]

where

* \(K\ne\varnothing\) is fixed;
* \(\Gamma=(\gamma_0,\ldots,\gamma_{2s})\) is an ordered active set; and
* \(I_j=\{\gamma_j,\ldots,\gamma_{j+s}\}\) is the ordinary
  \((s+1)\)-interval starting at \(j\).

The following word has length exactly \(2s+1\):

\[
 \boxed{
  \{\gamma_0\},\ldots,\{\gamma_{s-1}\},
  K\cup\{\gamma_s\},
  \{\gamma_{s+1}\},\ldots,\{\gamma_{2s}\}.}
 \tag{0.1}
\]

It represents every intersection and every union of consecutive owners
from \(Y_0,\ldots,Y_s\), through the full available depth \(s\).  Thus one
genuine zero-winding sector has an \(O(s)\), not \(O(s^2)\), literal fusion
gadget.  The construction uses the exact fixed-core/window geometry and
does not follow from the false implication \(d(D)=1\Rightarrow\) return.

This is not by itself a coefficient-one proof: the word has roughly twice
as many entries as the selected parity has owners, and a deck-level sharing
or overlap ledger is still needed.  It does, however, remove the quadratic
per-seam repair loss on every actual zero-winding sector.

## 1. Abstract fixed-core window lemma

Let \(s\ge1\), let \(K\) be a nonempty set disjoint from

\[
 \Gamma=\{\gamma_0,\ldots,\gamma_{2s}\},
\]

and put

\[
 I_j=\{\gamma_j,\gamma_{j+1},\ldots,\gamma_{j+s}\},
 \qquad
 Y_j=K\cup I_j,
 \qquad 0\le j\le s.
 \tag{1.1}
\]

No cyclic wrap occurs in (1.1).

### Theorem 1.1 (central-marker fusion)

The word (0.1) represents, for every \(0\le q\le s\) and every
\(0\le j\le s-q\), both

\[
 \bigcap_{t=0}^{q}Y_{j+t}
 \quad\hbox{and}\quad
 \bigcup_{t=0}^{q}Y_{j+t}.
 \tag{1.2}
\]

Every word entry is nonempty.

### Proof

The active intervals in (1.1) slide one step at a time, so

\[
 \bigcap_{t=0}^{q}Y_{j+t}
 =K\cup
   \{\gamma_{j+q},\ldots,\gamma_{j+s}\},
 \tag{1.3}
\]

and

\[
 \bigcup_{t=0}^{q}Y_{j+t}
 =K\cup
   \{\gamma_j,\ldots,\gamma_{j+s+q}\}.
 \tag{1.4}
\]

Both active intervals contain \(\gamma_s\).  Indeed, for (1.3),

\[
 j+q\le s,
 \qquad
 j+s\ge s,
\]

while for (1.4),

\[
 j\le s,
 \qquad
 j+s+q\ge s.
\]

In the word (0.1), the union of the consecutive entries from the
\(\gamma_a\)-entry through the \(\gamma_b\)-entry is therefore exactly

\[
 K\cup\{\gamma_a,\ldots,\gamma_b\}
\]

whenever \(a\le s\le b\).  Taking

\[
 (a,b)=(j+q,j+s)
\]

gives (1.3), and taking

\[
 (a,b)=(j,j+s+q)
\]

gives (1.4).  All singleton entries are nonempty, and the central entry is
nonempty because it contains \(\gamma_s\) (as well as \(K\)).
\(\square\)

## 2. Application to a genuine zero-winding PBBS return

Assume a genuine zero-winding return of gap \(2s+1<N=2r+1\).  The exact
owner-wreath theorem supplies active labels

\[
 \Gamma_0=(b_0,\ldots,b_{s-1},a_0,\ldots,a_s)
\]

and fixed cores \(K,K'\), each of size \(r-s>0\).  On the even parity,

\[
 A_{2j}=K\cup V_j,
 \qquad 0\le j\le s,
\]

where the \(V_j\)'s are consecutive \(s\)-windows in \(\Gamma_0\).
On the complement-projected parity,

\[
 X_j=[N]\setminus A_{2j}
 =K'\cup(\Gamma_0\setminus V_j).
 \tag{2.1}
\]

Rotate the active order by \(s\):

\[
 \gamma_i=(\Gamma_0)_{i+s}\qquad(i\bmod 2s+1).
 \tag{2.2}
\]

Then, for \(0\le j\le s\), the active complement in (2.1) is the
ordinary \((s+1)\)-interval

\[
 \Gamma_0\setminus V_j
 =\{\gamma_j,\ldots,\gamma_{j+s}\}.
 \tag{2.3}
\]

Thus Theorem 1.1 applies with core \(K'\).  It gives a literal word of
length \(2s+1\) covering every correct consecutive lower intersection and
upper union supported wholly by this open projected sector, at every depth
\(q\le s\).

At depth one, (1.3) also recovers the intervening odd PBBS states:

\[
 X_j\cap X_{j+1}=A_{2j+1}.
 \tag{2.4}
\]

Hence the gadget is compatible with the exact middle/first-shadow owner
dictionary; it is not merely an abstract active-coordinate factorization.

## 3. Exact scope

The theorem proves a local \(2s+1\)-entry fusion for one parity of one
**actual** zero-winding sector.  Three issues remain before it can enter a
coefficient-one global ledger.

1. The endpoint owner after the returned edge is the wrapped window and is
   not included in (2.3); it needs one adjacent packet or an endpoint
   collar.
2. Overlapping zero-winding sectors cannot be charged independently.  They
   must be selected or fused so that replacing their owner entries does not
   duplicate the main \(W\)-entry budget.
3. Positive-winding and non-zero-winding short residences are not covered
   by this fixed-core theorem.

The gain is nevertheless exact: the former literal repair ledger charged
\(\Theta(s^2)\) targets per cut, whereas every target generated inside a
genuine zero-winding sector is represented by the single linear word
(0.1).

