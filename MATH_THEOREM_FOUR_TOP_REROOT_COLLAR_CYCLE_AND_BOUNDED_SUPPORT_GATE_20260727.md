# A four-top re-root cycle changes boundary orbits with zero trace collar

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\tag{0.1}
\]

and assume \(H\ge3\) and \(m\ge6H+4\). There is an explicit physical
re-root move which joins different fixed-root boundary-swap components.

1. Four rank-\(M\) tops can be placed around a Johnson square of
   rank-\((M-1)\) seam facets. On every top, shift the rooted cyclic word
   forward by one position. The four new-minus-old signed trace vectors
   telescope exactly:

   \[
                         \boxed{\Delta_r=0\qquad(-H\le r\le H).}
   \tag{0.2}
   \]

   This includes the middle row \(r=0\), both protected signs, and the
   complete entrance collars. One path remains selected at every top.

2. The move changes the intrinsic boundary orbit

   \[
      (p_1,p_2,p_3,\ldots)\leftrightarrow
      (p_2,p_1,p_3,\ldots)
   \tag{0.3}
   \]

   into the different orbit based on \((p_2,p_3,p_4,\ldots)\). Thus the
   fixed-root \(K_2\)-component obstruction is not stable after literal
   re-root moves are admitted.

3. With two external companion tops, one may perform a collar-neutral
   hypersimplex rectangle before the re-root cycle and another after it.
   A chosen carrier top then realizes two distinct boundary rectangles
   in one coefficient-one chronology, while the total nonmiddle trace
   remains exactly zero.

4. A bounded carrier cannot recycle this indefinitely. If all re-root
   circuits involving a top \(U\) are supported on a fixed family
   \(\mathcal S\) of \(s\) tops, then before the rooted word wraps, \(U\)
   can expose at most

   \[
      |A_U(\mathcal S)|\le s-1
   \tag{0.4}
   \]

   distinct new boundary positions. Here \(A_U(\mathcal S)\) is the
   set of labels of \(U\) deleted on Johnson-adjacent intersections with
   other carrier tops. Therefore no constant-size catalyst supplies the
   required \(\Theta(m)\) independent rectangles per top. A dense bank
   needs carrier degree \(\Omega(m)\) or a move with more than bounded
   top support.

The four-top macro solves the local tail-change problem positively. It
does not yet construct the global \(\Theta(W)\)-rectangle schedule: the
remaining task is a high-degree decomposition of successive seam edges
into collar-compatible Johnson cycles, together with the prefix owner
capacity ledger.

## 1. Exact signed trace of one re-root

Let

\[
                         p=(p_1,\ldots,p_M)
\tag{1.1}
\]

be a rooted cyclic word on a rank-\(M\) top \(U\), with indices read
cyclically. At signed rank \(m+r\), use the actual promotion trace

\[
 \mathcal T_r(U,p)=
 \sum_{j=1}^{d}
 e_{\,U\setminus
 \{p_{j+r},p_{j+r+1},\ldots,p_{j+H-1}\}},
 \qquad -H\le r\le H.
\tag{1.2}
\]

For \(r=H\), the deleted interval is empty. This is the same shifted
promotion convention used in the common-core rectangle theorem; the
indices at most zero lie in the cyclic entrance prefix.

Every rooted cyclic word in (1.1) is a literal common-core option. Take
the unused \(H\)-prefix to be the positions \(1-H,\ldots,0\), take the
protected \(2H\)-core to be the preceding positions
\(1-3H,\ldots,-H\), and expose positions
\(1,\ldots,m-2H\). These three blocks have total length \(M\). After
re-rooting, make the same decomposition relative to the new origin.
Thus (1.3) is a genuine core-changing option move, not a formal shift of
an illegal linear word.

Let \(Sp\) be the one-step left re-root,

\[
                         (Sp)_k=p_{k+1}.
\tag{1.3}
\]

### Lemma 1.1 (two-seam formula)

For every \(-H\le r\le H\),

\[
 \boxed{
 \mathcal T_r(U,Sp)-\mathcal T_r(U,p)
 =e_{E_r(U,p)}-e_{A_r(U,p)},}
\tag{1.4}
\]

where

\[
 \begin{aligned}
 A_r(U,p)&=U\setminus
  \{p_{1+r},\ldots,p_H\},\\
 E_r(U,p)&=U\setminus
  \{p_{d+1+r},\ldots,p_{d+H}\}.
 \end{aligned}
\tag{1.5}
\]

At \(r=H\), both sets in (1.5) are \(U\).

#### Proof

The phase-\(j\) term of \(\mathcal T_r(U,Sp)\) is the phase-\((j+1)\)
term of \(\mathcal T_r(U,p)\). Summation over \(j=1,\ldots,d\)
therefore cancels phases \(2,\ldots,d\), leaving the new phase \(d+1\)
and removing phase \(1\). These are exactly (1.5). \(\square\)

Thus re-rooting has no bulk trace derivative. Its complete action is
carried by two nested seam flags.

## 2. A general collar-cycle lemma

Let

\[
                         B_0,B_1,\ldots,B_{k-1}
\tag{2.1}
\]

be a cyclic sequence of distinct \((M-1)\)-sets with

\[
                         |B_i\triangle B_{i+1}|=2.
\tag{2.2}
\]

Put indices modulo \(k\), and define

\[
 \begin{aligned}
 U_i&=B_i\cup B_{i+1},\\
 x_i&\in B_{i+1}\setminus B_i,\\
 y_i&\in B_i\setminus B_{i+1}.
 \end{aligned}
\tag{2.3}
\]

Thus \(|U_i|=M\), \(U_i=B_i\cup\{x_i\}=B_{i+1}\cup\{y_i\}\).

For every \(i\), choose an ordered collar

\[
                         C_i=(c_{i,1},\ldots,c_{i,2H-1})
                         \subset B_i
\tag{2.4}
\]

such that, inside \(U_i\), the four sets/labels

\[
                         C_i,\quad\{x_i\},\quad
                         C_{i+1},\quad\{y_i\}
\tag{2.5}
\]

are pairwise disjoint.

The two cyclic position intervals

\[
 [1-H,H],\qquad[d-H+1,d+H]\pmod M
\tag{2.6}
\]

are disjoint under \(m\ge6H+4\). Choose a cyclic word \(p_i\) on
\(U_i\) which places

\[
 \begin{aligned}
 (C_i,x_i)&\quad\text{in positions }1-H,\ldots,H,\\
 (C_{i+1},y_i)&\quad\text{in positions }d-H+1,\ldots,d+H,
 \end{aligned}
\tag{2.7}
\]

and fill all remaining positions arbitrarily.

### Theorem 2.1 (collar-cycle cancellation)

The simultaneous re-root move

\[
                         (U_i,p_i)\longmapsto(U_i,Sp_i)
                         \qquad(0\le i<k)
\tag{2.8}
\]

has zero aggregate derivative at every protected signed rank:

\[
                         \sum_{i=0}^{k-1}
 \bigl(\mathcal T_r(U_i,Sp_i)-\mathcal T_r(U_i,p_i)\bigr)=0.
\tag{2.9}
\]

#### Proof

Fix \(r\le H-1\), and put \(\ell=H-r\). By (2.7), the deleted
interval in \(A_r(U_i,p_i)\) consists of \(x_i\) together with the
last \(\ell-1\) labels of \(C_i\). Hence

\[
 A_r(U_i,p_i)=
 B_i\setminus\operatorname{suf}_{\ell-1}(C_i).
\tag{2.10}
\]

Similarly,

\[
 E_r(U_i,p_i)=
 B_{i+1}\setminus\operatorname{suf}_{\ell-1}(C_{i+1})
 =A_r(U_{i+1},p_{i+1}).
\tag{2.11}
\]

The endpoint terms in (1.4) telescope cyclically. At \(r=H\), every
one-top derivative is already zero. This proves (2.9). \(\square\)

Because the equality is separate for every signed rank and every seam
target, any common nested tag schedule on matching seams preserves it.
In particular the four rows below may use one common protected schedule.

## 3. The explicit four-top Johnson square

Let \(D\) have size \(M-3\), and choose distinct labels
\(a,b,c,e\notin D\). Define

\[
 \begin{aligned}
 B_0&=D\cup\{a,c\},&
 B_1&=D\cup\{b,c\},\\
 B_2&=D\cup\{b,e\},&
 B_3&=D\cup\{a,e\}.
 \end{aligned}
\tag{3.1}
\]

These four facets form a Johnson square. Their four carrier tops are

\[
 \begin{aligned}
 U_0&=D\cup\{a,b,c\},&
 U_1&=D\cup\{b,c,e\},\\
 U_2&=D\cup\{a,b,e\},&
 U_3&=D\cup\{a,c,e\}.
 \end{aligned}
\tag{3.2}
\]

Choose disjoint ordered \((2H-1)\)-sets \(C,C'\subset D\), and put

\[
                         C_0=C_2=C,\qquad C_1=C_3=C'.
\tag{3.3}
\]

The collar conditions (2.5) hold: adjacent collars are disjoint and all
four special labels lie outside \(D\). Therefore Theorem 2.1 gives an
explicit four-top, one-frame-per-top re-root move with (0.2).

All four common \((M-2)\)-cores change between adjacent seam
descriptions. The construction is consequently outside both the
fixed-root \(K_2\) theorem and the fixed-common-core catalyst parity
theorem.

## 4. Two independent rectangles on one carrier top

Every rooted word supports a literal boundary rectangle companion.

### Lemma 4.1 (arbitrary-word rectangle completion)

Let \(p=(p_1,\ldots,p_M)\) be any rooted word on \(U\). Put

\[
 \begin{aligned}
 a&=p_1,& b&=p_2,& x&=p_3,\\
 F&=(p_4,\ldots,p_H),&
 z&=p_{H+1},&z'&=p_{H+2},
 \end{aligned}
\tag{4.1}
\]

and let \(R\) be the remaining \(m-2\) labels, in their inherited
order. Choose \(y\notin U\), put \(U'=U-\{x\}+\{y\}\), and define

\[
                         p'=(b,a,y,F,z',z,R).
\tag{4.2}
\]

Then the simultaneous first-two swaps on \(p,p'\) form the exact
collar-neutral hypersimplex rectangle.

#### Proof

The displayed blocks have sizes

\[
 2+1+(H-3)+2+(m-2)=M.
\tag{4.3}
\]

Thus (4.1)--(4.2) are exactly the two words in the independently audited
two-top rectangle theorem. \(\square\)

### Proposition 4.2 (two-level rectangle chronology)

Choose one carrier top, say \(U_0\), in the four-top re-root cycle.
There is a coefficient-one chronology consisting of

1. one boundary rectangle ending at the source word \(p_0\);
2. the four-top re-root cycle \(p_i\mapsto Sp_i\); and
3. one boundary rectangle starting at \(Sp_0\),

such that all external companion tops are distinct. Its aggregate trace
derivative is zero at every nonmiddle signed rank, while the middle
derivative is the sum of two hypersimplex rectangles. On \(U_0\), the
two focal unit transfers use the distinct boundary pairs

\[
                         \{p_1,p_2\},\qquad\{p_2,p_3\}.
\tag{4.4}
\]

#### Proof

Apply Lemma 4.1 in reverse orientation to obtain the first rectangle,
so that its new focal state is \(p_0\). Apply Theorem 2.1. Apply Lemma
4.1 to \(Sp_0\) for the second rectangle. The complements of the six
carrier/companion tops have linear size, so the two companion tops can
be chosen distinct from the four carrier tops and from each other.

Each rectangle is exactly collar-neutral, and the re-root cycle is
exactly trace-neutral. Their chronological composition is therefore
zero at every nonmiddle signed rank. Equation (4.4) follows directly
from the one-step shift. \(\square\)

This is the first literal escape from the fixed-root one-net-swap ceiling:
one physical top performs two different rectangle directions without
ever carrying two simultaneous path options.

## 5. Bounded-support impossibility

The preceding macro cannot be iterated \(\Theta(m)\) times inside one
fixed finite carrier.

For a family \(\mathcal S\) of rank-\(M\) tops and \(U\in\mathcal S\),
define its outgoing seam alphabet

\[
 A_U(\mathcal S)=
 \{x\in U:\text{ for some }V\in\mathcal S,
 |U\cap V|=M-1\text{ and }U\setminus V=\{x\}\}.
\tag{5.1}
\]

Plainly

\[
                         |A_U(\mathcal S)|\le\deg_{\mathcal S}(U)
                         \le|\mathcal S|-1.
\tag{5.2}
\]

### Theorem 5.1 (seam-alphabet bound)

Let \(p\) be an injective cyclic word on \(U\). Suppose \(k\) distinct
successive forward re-roots

\[
                         S^tp\longmapsto S^{t+1}p,
                         \qquad 0\le t<k<M,
\tag{5.3}
\]

are each contained in an aggregate trace-neutral re-root circuit whose
top support is contained in one fixed family \(\mathcal S\). Then

\[
                         \boxed{k\le|A_U(\mathcal S)|\le|\mathcal S|-1.}
\tag{5.4}
\]

#### Proof

Inspect the signed rank \(r=H-1\). By Lemma 1.1, the removed seam target
at the \(t\)-th re-root is

\[
                         U\setminus\{p_{H+t}\}.
\tag{5.5}
\]

The trace coordinates are literal set identities. For its coefficient
to cancel in a trace-neutral circuit, some positive seam target on a top
\(V\in\mathcal S\) must equal (5.5). Equality of two rank-\((M-1)\)
sets implies

\[
 |U\cap V|=M-1,
 \qquad U\setminus V=\{p_{H+t}\}.
\tag{5.6}
\]

Thus \(p_{H+t}\in A_U(\mathcal S)\). The labels
\(p_H,p_{H+1},\ldots,p_{H+k-1}\) are distinct because \(p\) is
injective and \(k<M\). Hence \(k\le|A_U(\mathcal S)|\), and (5.2)
finishes the proof. \(\square\)

The theorem uses only the singleton seam \(r=H-1\). It is unaffected by
how the longer collars are tagged or paired. Backtracking re-roots may
be repeated indefinitely, but they revisit old boundary orbits and do
not create independent rectangle directions.

### Corollary 5.2 (no bounded catalyst for dense recycling)

A carrier supported on \(s=O(1)\) tops gives only \(O(1)\) independent
boundary rectangles per top. To obtain \(\Theta(m)\) distinct boundary
orbits at a typical top by one-step re-rooting, the carrier support graph
must have degree \(\Omega(m)\) there. In particular a fixed four-, six-,
or eight-top catalyst cannot close the dense rectangle gate.

## 6. Exact boundary

Proved:

1. the two-seam formula for the actual shifted promotion trace;
2. exact cancellation of all signed traces around every collar-compatible
   Johnson facet cycle;
3. an explicit four-top Johnson-square re-root macro;
4. a literal chronology giving two distinct hypersimplex rectangles on
   one carrier top with zero nonmiddle collateral; and
5. the seam-alphabet bound \(k\le|\mathcal S|-1\), ruling out bounded
   carrier support for \(\Theta(m)\) reuse.

Not proved:

1. a degree-\(\Theta(m)\) collar-cycle decomposition for successive
   re-root seams on almost all tops;
2. a synchronized rectangle/re-root chronology satisfying the owner
   capacity condition at every prefix;
3. an endpoint table with \(o(W)\) owner-repeat excess; or
4. coefficient one.

The local re-root/tail-change primitive exists. Its exact global cost is
not vertical trace damage but carrier expansion: every new boundary
position needs a new Johnson-adjacent seam neighbor.
