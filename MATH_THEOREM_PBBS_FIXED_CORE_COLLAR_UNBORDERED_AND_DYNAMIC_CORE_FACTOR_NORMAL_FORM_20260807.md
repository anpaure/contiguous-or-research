# Fixed-core lag-two collars are unbordered; dynamic cores remove the abstract owner obstruction

**Date:** 2026-08-07  
**Status:** unconditional sharp fixed-core overlap obstruction and
unconditional abstract dynamic-core factor theorem.  A fixed core supports
isolated clean \(B+2\) collars but not a positive-density overlapping
collar bank.  After allowing adjacent core changes, every Johnson owner
path has a core/queue lift; the remaining obstruction is the literal,
decorated realization of that lift.

## 1. Parameters and the exact fixed-core collar

Put

\[
 n=2m+1,\qquad L=d+2,\qquad a=m-L=m-d-2.
\tag{1.1}
\]

Use the fixed-core collar of
`MATH_THEOREM_PBBS_LAG2_FIXED_CORE_RAIL_COLLAR_20260807.md`.
Thus

\[
 G=Q\mathbin{\dot\cup}C_0\mathbin{\dot\cup}\{a_0\},
 \qquad |G|=a,qquad |C_0|=d-1,
\tag{1.2}
\]

and the exceptional toggle substring is

\[
 b^-,u,a_1,\ldots,a_{d-1},z,b,v.
\tag{1.3}
\]

For \(d\ge3\), after deleting the designated toggle from each source
letter, the successive **core fragments** in the exceptional substring
are

\[
 \boxed{
 C_0,\quad \varnothing,\quad
 H,\ldots,H,\quad C_0,\quad\varnothing,\quad\varnothing,}
 \qquad H:=G\setminus C_0,
\tag{1.4}
\]

where \(H\) occurs \(d-1\) times.  The word (1.4) has length

\[
 d+4=L+2.
\tag{1.5}
\]

The endpoint enrichment \(C_0+b^-\) is included in (1.4).  For \(d=2\)
the outgoing seam additionally enriches the final \(v\)-letter; that
finite special case is separated below.

## 2. Sharp fixed-core overlap obstruction

For all sufficiently large parameters,

\[
 |H|=a-d+1=m-2d-1>d-1=|C_0|>0.
\tag{2.1}
\]

Thus the three fragment types \(C_0,H,\varnothing\) have distinct ranks.

### Theorem 2.1 (unbordered collar word)

Let two clean lag-two collars use the same fixed core \(G\), possibly with
different choices of \(C_0\subset G\).  If their exceptional source
substrings overlap and the literal prescriptions agree at every shared
position, then the two starts are equal.

Equivalently, distinct fixed-core collars have disjoint exceptional
supports, and their start positions differ by at least

\[
 \boxed{L+2=d+4.}
\tag{2.2}
\]

#### Proof

Let the later collar start \(r\) positions after the first, with
\(0<r<L+2\).  At the first shared position, the later collar prescribes
its initial rank-\((d-1)\) fragment \(C_0'\).  By (2.1), the first
collar can have an equal fragment only at one of its two \(C_0\)-positions,
namely positions \(0\) and \(L-1=d+1\).  Since \(r>0\), necessarily

\[
 r=L-1,qquad C_0'=C_0.
\]

The overlap then has length three.  The old suffix is

\[
 C_0,\varnothing,\varnothing,
\]

whereas the new prefix is

\[
 C_0,\varnothing,H.
\]

Since \(H\ne\varnothing\), the third shared source letter is
inconsistent.  No nonzero overlap is possible. \(\square\)

### Corollary 2.2 (no positive-density fixed-core packet bank)

In a source interval of length \(N\), one fixed core supports at most

\[
 \boxed{\left\lfloor\frac{N}{L+2}\right\rfloor+O(1)}
\tag{2.3}
\]

clean collar occurrences.  Their density is \(O(1/d)\), tending to zero.
In particular no periodic set such as a positive-density subset of
\(6\mathbb Z\) works for all large \(d\).

For \(d=2\), the enriched fragment word is

\[
 C_0,\varnothing,H,C_0,\varnothing,H,
\]

and has period three.  This finite exception does not affect the
all-dimensional asymptotic obstruction.

For \(d\ge3\), one may optionally enrich the final \(v\)-letter by the
core fragment \(H\).  The resulting fragment word is

\[
 C_0,\varnothing,H^{d-1},C_0,\varnothing,H.
\]

Its only nonzero border has length three, so the only possible overlap
shift is \(L-1=d+1\) (and requires the same \(C_0\)).  Its collar density
is still \(O(1/d)\).  Thus the no-positive-density conclusion is
independent of choosing the minimal or uniformly enriched outgoing seam.

### Corollary 2.3 (the actual boundary bank is not position-limited)

The triangular Ferrers bank has

\[
 h\le\binom{d+1}{2}=O(d^2).
\]

Disjoint collars occupy \(O(d^3)\) source positions, while
\(W=\binom{2m+1}{m}\) is exponential in \(m\).  Hence (2.2) does not
obstruct the actual boundary bank by scalar position count.  It does
rule out a positive-density all-owner construction using one fixed core.

## 3. Which tasks one fixed core can carry

Let \(M\) be the bottom of a clean promotion flag, \(|M|=a\).  In the
collar normal form,

\[
 G=Q+C_0+a_0,
 \qquad
 M=Q+a_0+A_1,
 \qquad |C_0|=|A_1|=d-1.
\tag{3.1}
\]

### Proposition 3.1 (sphere criterion)

A fixed core \(G\) supports the flag bottom \(M\) if and only if

\[
 \boxed{\operatorname{dist}_{J(n,a)}(G,M)=d-1.}
\tag{3.2}
\]

For the full flag \((M,M+u)\), one must additionally have \(u\notin G\),
because \(u\) is a toggle label of the collar.

For a compatible pair, the number of possible distinguished common
labels \(a_0\) is

\[
 |G\cap M|=a-d+1.
\tag{3.3}
\]

#### Proof

The displayed collar has

\[
 G-M=C_0,qquad M-G=A_1,
\]

so (3.2) is necessary.  Conversely, when (3.2) holds, choose
\(a_0\in G\cap M\), put

\[
 Q=(G\cap M)-a_0,quad C_0=G-M,quad A_1=M-G,
\]

and recover (3.1). \(\square\)

Thus one fixed core has

\[
 \binom a{d-1}\binom{n-a}{d-1}
\tag{3.4}
\]

compatible flag bottoms.  This is a large menu, but it is not universal.
If two required bottoms have Johnson distance greater than \(2(d-1)\),
the triangle inequality shows that no common fixed core can carry both.

## 4. The full fixed-core owner factor and its lattice obstruction

The complement of one rank-\(a\) core has size

\[
 R_0=n-a=m+d+3.
\tag{4.1}
\]

For a cyclic order \(\sigma\) of those \(R_0\) toggles, the fixed-core
carousel owners are

\[
 G\cup\{\sigma(i),\sigma(i+1),\ldots,\sigma(i+L-1)\},
 \qquad i\in\mathbb Z_{R_0}.
\tag{4.2}
\]

They form a simple Johnson cycle of size \(R_0\).  The carousel orbit on
the rank-\(m\) owner shore is regular and has normalized maximum
pair-codegree \(\Theta(m^{-2})\), but a perfect owner partition using
only full fixed-core cycles necessarily satisfies

\[
 \boxed{R_0\mid W.}
\tag{4.3}
\]

This divisibility generally fails.  Therefore even without promotion
collars, full fixed-core cycles are not a uniform all-parameter owner
factor.  Open rail paths of varying lengths, or core-changing splices,
are necessary.

## 5. Every abstract owner path has a dynamic-core lift

The fixed-core obstruction is not an abstract core-connectivity
obstruction.

### Theorem 5.1 (dynamic-core tracking)

Let

\[
 T_0,T_1,\ldots,T_s
\]

be any rank-\(m\) Johnson path.  There are rank-\(a\) cores

\[
 G_i\subset T_i
\]

such that every consecutive pair \(G_i,G_{i+1}\) is equal or Johnson
adjacent.

#### Proof

Choose any \(G_0\subset T_0\) of rank \(a\).  Write

\[
 T_{i+1}=T_i-x_i+y_i.
\]

If \(x_i\notin G_i\), put \(G_{i+1}=G_i\).  Then
\(G_i\subset T_i\cap T_{i+1}\).

If \(x_i\in G_i\), the intersection

\[
 I_i=T_i\cap T_{i+1}
\]

has rank \(m-1\), while \(G_i\cap I_i\) has rank \(a-1\).  Hence

\[
 |I_i\setminus G_i|=m-a=d+2=L>0.
\]

Choose \(w_i\in I_i\setminus G_i\) and put

\[
 G_{i+1}=G_i-x_i+w_i.
\]

Then \(G_{i+1}\subset I_i\subset T_{i+1}\), and the two cores are
Johnson adjacent. \(\square\)

Writing

\[
 Q_i=T_i\setminus G_i,qquad |Q_i|=L,
\tag{5.1}
\]

gives the exact two transition types

\[
\begin{array}{c|c|c}
 &G_i\to G_{i+1}&Q_i\to Q_{i+1}\\ \hline
 x_i\notin G_i&G_i&G_i\text{ fixed},\quad Q_i-x_i+y_i\\
 x_i\in G_i&G_i-x_i+w_i&Q_i-w_i+y_i.
\end{array}
\tag{5.2}

In the first row the fixed-core queue performs the owner exchange.  In
the second row the core and queue make a coupled exchange, while their
union performs the same owner exchange \(x_i\mapsto y_i\).

### Corollary 5.2 (unconditional abstract middle/upper factor)

Open any middle-levels Hamilton cycle on ranks \(m,m+1\) at a rank-
\(m\) owner, and repeat that owner at the terminal occurrence.  Its
rank-\(m\) shore is a Johnson path

\[
 T_0,T_1,\ldots,T_W=T_0,
\]

whose intermediate rank-\((m+1)\) vertices are exactly the unions of
consecutive owners.  Applying Theorem 5.1 gives a dynamic-core path which

1. uses every rank-\(m\) target exactly once before the permitted repeated
   closure occurrence;
2. uses every rank-\((m+1)\) upper colour exactly once; and
3. changes its rank-\(a\) core by at most one Johnson swap per owner step.

Thus owner and immediate-upper factorization do not obstruct a dynamic
core architecture.

## 6. Exact remaining factor

The missing object is an occurrence-labelled lift of Corollary 5.2.
Equivalently, one needs a path of states

\[
 (G_i,Q_i),\qquad |G_i|=a,\quad |Q_i|=L,quad G_i\cap Q_i=\varnothing,
\tag{6.1}
\]

such that:

1. the owners \(G_i\cup Q_i\) are all rank-\(m\) sets exactly once;
2. consecutive owner unions are all rank-\((m+1)\) sets exactly once;
3. equal-core stretches have literal fixed-core rail sources;
4. every adjacent-core transition in (5.2) has a literal splice whose
   overlapping source prescriptions agree with both rails;
5. every prescribed promotion task lies in an equal-core stretch with
   its clean unbordered collar and sphere condition (3.2);
6. all q1 lower colours, residence, deeper upper targets, and the common
   lower compiler are simultaneously valid.

Items 1--2 and the abstract core trajectory are unconditional by the
Middle Levels Theorem and Theorem 5.1.  The clean collar closes each task
locally, but Theorem 2.1 forces those task supports to be isolated inside
their fixed-core stretches.  The genuinely new bridge is item 4: a
literal coupled core/queue splice compatible with the global decorations.

## 7. Verdict

The fixed-core macro route has a sharp boundary:

\[
 \boxed{\text{one fixed core supports exact isolated clean collars, but
 no positive-density overlapping clean-collar family}.}
\]

This does not threaten the actual \(O(d^2)\) Ferrers task bank, whose
disjoint positional cost is negligible relative to \(W\).  It does rule
out a proof that treats one fixed-core periodic rail as the complete
all-owner construction.

Allowing the core to move removes every abstract owner/upper obstruction:
every middle-levels Hamilton path has a coupled core/queue lift.  What
remains is now sharply occurrence-level--construct literal splices for
the coupled transitions and preserve the lower/deep/compiler decorations.
