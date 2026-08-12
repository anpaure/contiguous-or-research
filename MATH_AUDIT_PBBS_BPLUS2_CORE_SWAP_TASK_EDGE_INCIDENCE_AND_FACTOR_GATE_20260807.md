# The punctured \(B+2\) core swap: exact task--edge incidence and factor gate

**Date:** 2026-08-07  
**Status:** unconditional audit of the local repair and its symmetric core
graph.  Every promotion flag has many compatible Johnson-core arcs, and
the abstract flag-to-arc incidence has an exact saturating matching.  This
does not yet serialize the arcs in one literal owner/palette factor.

## 1. Local normal form

Put

\[
 n=2m+1,\qquad L=d+2,\qquad a=m-L=m-d-2.
\tag{1.1}
\]

Use the notation of
`MATH_THEOREM_PBBS_BPLUS2_SHIFTED_HINGE_ENDPOINT_HOLE_AND_CORE_SWAP_REPAIR_20260807.md`.
Thus

\[
 M=K\dot\cup A,\quad |M|=a,\quad |A|=d,
 \qquad
 G=K\dot\cup C,\quad |C|=d,
\tag{1.2}
\]

and the puncture chooses \(z\in C\) and the distinguished
\(a_0\in A\).  The outgoing core is

\[
 \boxed{G'=G-z+a_0.}
\tag{1.3}
\]

Hence every punctured splice projects to an oriented edge of

\[
 J(n,a).
\tag{1.4}
\]

The two central owners, their q1 colour and their upper colour remain

\[
\begin{aligned}
 T_-&=M+C+u+x,\\
 T_0&=M+C+u+y,\\
 I_-&=M+C+u,\\
 J_-&=M+C+u+x+y.
\end{aligned}
\tag{1.5}
\]

If the next new-rail toggle is \(w\), then

\[
 T_+=T_0-z+w,
\tag{1.6}
\]

and the next two immediate colours are literal:

\[
 I_+=T_0\cap T_+=M+(C-z)+u+y,
\tag{1.7}
\]

\[
 J_+=T_0\cup T_+=M+C+u+y+w.
\tag{1.8}
\]

Thus the punctured splice has no local **edge-palette** sidecar.  It does,
however, export the authoritative forced successor coatom

\[
 Y_{\rm forced}=M+C+y=T_0-u.
\tag{1.9}
\]

The unpunctured source represents this target literally, but repeats
\(T_0\) at the next start and forces one unused left endpoint per hinge.
The punctured source restores the next Johnson step, but the corresponding
short cell is only

\[
 Y_{\rm forced}-z,
\tag{1.10}
\]

of rank \(m-2\).  Hence every punctured task still needs one named
forced-coatom/compiler ticket.  The edge-palette statement must not be
read as complete promotion-ticket closure.

## 2. The ideal core graph

The vertex set is \(\binom{[n]}a\), and from every \(G\) there is one
oriented arc for each ordered pair

\[
 z\in G,\qquad a_0\notin G.
\]

Therefore

\[
 \boxed{d^+(G)=d^-(G)=a(n-a)=a(m+d+3).}
\tag{2.1}
\]

The underlying graph is the Johnson graph \(J(n,a)\).  In particular it
is connected; indeed it is Hamiltonian.  This settles abstract core-state
reachability.  It says nothing yet about the occurrence-labelled source
letters or the owner/lower/upper palettes carried by a walk.

## 3. Exact flag-to-core-edge incidence

Let a promotion task be a flag

\[
 f=(M,U=M+u),\qquad |M|=a.
\tag{3.1}
\]

Put

\[
 N=m+d+2=n-a-1.
\tag{3.2}
\]

### Theorem 3.1 (biregular incidence)

The number of **distinct oriented core arcs** compatible with one fixed
flag is

\[
 \boxed{
 D_{F\to E}
 =\binom ad\binom Nd d^2.}
\tag{3.3}
\]

The number of flags compatible with one fixed oriented core arc is

\[
 \boxed{
 D_{E\to F}
 =\binom{a-1}{d-1}\binom N{d-1}(m+3).}
\tag{3.4}
\]

Moreover

\[
 \boxed{\frac{D_{F\to E}}{D_{E\to F}}=a.}
\tag{3.5}
\]

#### Proof

For a fixed flag, choose \(A\subset M\) and
\(C\subset[n]\setminus(M+u)\), both of size \(d\), then choose
\(a_0\in A\) and \(z\in C\).  The resulting arc has

\[
 G=(M-A)+C,
 \qquad G'=G-z+a_0.
\]

Conversely, the flag and the oriented arc recover

\[
 a_0=G'-G,\quad z=G-G',\quad
 K=G\cap M,\quad A=M-K,\quad C=G-K,
\]

so no two choices give the same arc.  This proves (3.3).

For a fixed arc \(G\to G-z+a_0\), choose
\(C\subset G\) of size \(d\) containing \(z\), then choose the other
\(d-1\) members of \(A\) outside \(G+a_0\).  These choices determine
\(K=G-C\) and \(M=K+A\).  Finally choose
\(u\notin G\cup A\), giving \(m+3\) choices.  This proves (3.4).

The binomial identities

\[
 \frac{\binom ad}{\binom{a-1}{d-1}}=\frac ad,
 \qquad
 \frac{\binom Nd}{\binom N{d-1}}=\frac{m+3}{d}
\]

give (3.5). \(\square\)

### Corollary 3.2 (abstract distinct-arc assignment)

The bipartite graph between all flags and all oriented Johnson-core arcs
has a matching saturating every flag.

#### Proof

It is biregular with left degree \(D_{F\to E}=aD_{E\to F}\).  For every
set \(X\) of flags, edge counting gives

\[
 D_{F\to E}|X|
 \le D_{E\to F}|N(X)|,
\]

and hence \(|N(X)|\ge a|X|\ge|X|\).  Hall's theorem applies. \(\square\)

The same conclusion holds for every subfamily of flags, including every
target-disjoint task bank.

## 4. Source-labelled multiplicities

Once a flag and a compatible core arc are fixed, the unordered sets
\(A,C\) and the distinguished labels \(a_0,z\) are fixed.  Ordering the
remaining \(a_1,\ldots,a_{d-1}\) and choosing the four exterior roles
\(u,x,y,w\), when \(u\) is not already fixed by the task, give the
corresponding source-labelled multiplicities.

For example, with the flag \((M,M+u)\) fixed, each compatible arc has

\[
 \boxed{(d-1)!(m+2)_3}
\tag{4.1}
\]

literal choices for the remaining ordered \(A\)-roles and
\((x,y,w)\).  With only the oriented core arc fixed, the full number of
literal completions is

\[
 \boxed{
 \binom{a-1}{d-1}(N)_{d-1}(m+3)_4.}
\tag{4.2}
\]

These large multiplicities are prospective.  Once the literal old source
word is frozen, the occurrence fibre can collapse to one option; the
counts must not be reused as a frozen-word neighbourhood.

## 5. What the matching does not prove

Corollary 3.2 closes one precise marginal problem:

\[
 \boxed{\text{promotion tasks can be assigned distinct abstract
 Johnson-core arcs}.}
\]

A source chronology needs much more.  The selected arcs must be ordered
so that the head core of one transition is the tail core of the next, or
must be joined by additional compatible core arcs.  Simultaneously:

1. all overlapping source positions must receive the same literal set;
2. each core entry/exit and each toggle occurrence must satisfy residence;
3. the rank-\(m\) owners and rank-\((m+1)\) upper colours must have their
   required one-copy multiplicities; and
4. the shorter cells must support the same lower compiler.

Distinct-edge assignment imposes none of these four correlations.  Even
distinct tails and heads would give only a disjoint union of directed
paths/cycles, not one occurrence-labelled factor.

Thus the ideal Johnson graph has ample degree and no connectivity
obstruction.  The remaining theorem is a **coloured core-walk lift**:
select and join the task arcs inside one resident literal walk while
preserving all named palettes and the compiler.  This is a global factor
problem, not an additional local supply problem.
