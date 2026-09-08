# The `k=17` two-zone high-rank complement gate and uniform-prefix no-go

Date: 2026-07-31  
Status: exact theorem-level audit after the mixed-width correction.  The
uniform four-window interpretation of the proposed prefix is impossible,
but the live triple-window prefix is not disproved.  Conditional on a
bijective mixed rank-nine chronology, ranks `10,...,17` have the exact
complement-intersection plus boundary-gap characterization below.  No
`k=17` word or upper bound is claimed.

## 1. Verdict

There are two logically separate conclusions.

1. If the prefix is read as having rank-nine **four-windows**, as in the
   original proposal text, it is impossible.  Any five consecutive prefix
   letters force two consecutive rank-nine owners to be equal.
2. The corrected live schedule instead has `7399` internal prefix
   **triple-window** owners, two crossing triple owners, and `16909` tail
   four-window owners.  Its prefix is an upper-rainbow path in `J(17,8)` and
   remains open.
3. Counterfactually assuming that this mixed row bijects the rank-nine
   layer, the complete upper gate is exact and checkable.  Every cap of rank
   at most seven must occur either as the intersection of a consecutive
   owner-complement block or in one explicit prefix-to-tail boundary-gap
   chain.

Neither rank-nine bijectivity nor perfect Johnson-local rank-eight diamonds
imply the upper condition.  An authenticated `k=17` owner cycle satisfying
both misses a rank-ten target whose ten facets lie in ten isolated runs.

## 2. The five-letter uniform-prefix obstruction

Let \(p_0,\ldots,p_4\) be five consecutive letters wholly inside the proposed
prefix, and put

\[
 E_j=p_j\cup p_{j+1}\quad(0\le j\le3),
 \qquad
 R_j=p_j\cup p_{j+1}\cup p_{j+2}\cup p_{j+3}
 \quad(j=0,1).                                      \tag{2.1}
\]

### Theorem 2.1 (prefix rank-eight/rank-nine no-go)

It is impossible that \(E_1,E_2\) are distinct rank-eight sets while
\(R_0,R_1\) are distinct rank-nine sets.

#### Proof

The shared triple satisfies

\[
 E_1\cup E_2=p_1\cup p_2\cup p_3\subseteq R_0\cap R_1. \tag{2.2}
\]

Two distinct rank-eight sets have a union of rank at least nine.  Since each
\(R_j\) has rank nine, (2.2) forces

\[
 R_0=E_1\cup E_2=R_1,
\]

contrary to rank-nine injectivity.  \(\square\)

The uniform reading has a prefix of length `7401`; lower bijectivity requires
all `7400` adjacent unions to be distinct rank-eight targets, while that
reading requires all `7398` internal four-windows to be distinct rank-nine
owners.  Theorem 2.1 applies throughout its interior.

This does **not** close the corrected one-pivot prefix.  There the rank-eight
vertices are

\[
 C_i=p_i\cup p_{i+1}\qquad(0\le i<7400),
\]

and the internal rank-nine owners are the `7399` triples

\[
 M_i=p_i\cup p_{i+1}\cup p_{i+2}=C_i\cup C_{i+1}.
\]

Distinct consecutive \(C_i\)'s are Johnson-adjacent and have rank-nine
union; the corresponding four-window has rank ten, not nine.  Thus the live
prefix is an occurrence-labelled upper-rainbow path problem, not an empty
four-window plateau.

## 3. Exact mixed-width upper-rank criterion

Let

\[
 A=(A_0,\ldots,A_{24312})
\]

be a physical word in the corrected two-zone schedule.  Its selected
rank-nine row is

\[
 M_i=
 \begin{cases}
 A_i\cup A_{i+1}\cup A_{i+2},&0\le i\le7400,\\
 A_i\cup A_{i+1}\cup A_{i+2}\cup A_{i+3},
     &7401\le i\le24309.
 \end{cases}                                         \tag{3.1}
\]

Counterfactually assume that these are the `24310` rank-nine subsets of
`[17]`, each exactly once, and put

\[
 H_i=[17]\setminus M_i.                              \tag{3.2}
\]

Thus \(H=(H_i)\) is a permutation of the rank-eight layer.  There is one
mixed-width boundary-gap family:

\[
 G_a=\bigcup_{j=a}^{7403}A_j,\qquad
 K_a=[17]\setminus G_a,\qquad 0\le a\le7400.         \tag{3.3}
\]

### Lemma 3.1 (exact interval classification)

Every physical interval of rank at least ten is either the union of a
consecutive block of the selected owners \(M\), or is one of the intervals
\(G_a\) in (3.3).  More precisely,

\[
 \bigcup_{i=p}^{q}M_i=
 \begin{cases}
 \displaystyle\bigcup_{j=p}^{q+2}A_j,&q\le7400,\\[2mm]
 \displaystyle\bigcup_{j=p}^{q+3}A_j,&q\ge7401.
 \end{cases}                                         \tag{3.4}
\]

#### Proof

The two identities in (3.4) follow directly from the overlapping triple or
quadruple windows; the second also holds when the owner interval crosses
the boundary.  A physical interval ending at most at position `7402` is
recovered from triple owners, and one ending at least at position `7404` is
recovered from the mixed row.  The unrecovered intervals ending exactly at
`7403` are precisely (3.3).  All remaining intervals too short to be
represented have rank at most nine under the selected lower schedule.
\(\square\)

Fix an upper target \(U\), \(10\le |U|\le17\), put

\[
 C=[17]\setminus U,                                  \tag{3.5}
\]

and call \(i\) \(C\)-clean when \(C\subseteq H_i\), equivalently
\(M_i\subseteq U\).

### Theorem 3.2 (exact complement-run plus gap criterion)

The following are equivalent.

1. \(U\) is a contiguous OR of the physical word \(A\).
2. Either \(U=G_a\) for some \(a\), or some consecutive block of \(M\)
   has union \(U\).
3. Either \(C=K_a\) for some \(a\), or some consecutive block of \(H\)
   has intersection \(C\).
4. Either \(C\in\{K_a:0\le a\le7400\}\), or some maximal
   \(C\)-clean run \(J\) satisfies

   \[
      \bigcap_{i\in J}H_i=C,
      \qquad\text{equivalently}\qquad
      \bigcup_{i\in J}M_i=U.                         \tag{3.6}
   \]

#### Proof

Lemma 3.1 and complementation prove `1 <=> 2 <=> 3`.  A block whose
intersection is \(C\) consists only of \(C\)-clean indices.  Extending it
to its maximal clean run does not change the intersection: every added
\(H_i\) still contains \(C\).  This proves `3 <=> 4`.  \(\square\)

Theorem 3.2 is the weakest literal high-rank condition.  It is necessary
and sufficient, contains no abundance assumption, and allows witnesses for
different targets to overlap.  The gap unions \(G_a\) form one nested chain,
so they contain at most one distinct target of each rank.

### Corollary 3.3 (rank-ten gate)

A rank-ten target \(U\) occurs if and only if either:

1. two consecutive owners are two distinct rank-nine facets of \(U\), so
   their union is \(U\); or
2. \(U\) is the rank-ten member, if any, of the boundary-gap chain
   \((G_a)\).

Indeed, any two distinct rank-nine subsets of a ten-set unite to that
ten-set.  Conversely, a clean run uniting to \(U\) contains two consecutive
distinct owners because the owner row is injective.

## 4. Exact prefix--seam--tail composition

For a nonempty sequence \(X=(X_1,\ldots,X_t)\) of complement owners define

\[
\begin{aligned}
 \kappa(X)&=\bigcap_{i=1}^{t}X_i,\\
 \operatorname{Pre}(X)&=
   \left\{\bigcap_{i=1}^{j}X_i:1\le j\le t\right\},\\
 \operatorname{Suf}(X)&=
   \left\{\bigcap_{i=j}^{t}X_i:1\le j\le t\right\},\\
 \operatorname{Cov}(X)&=
   \left\{\bigcap_{i=a}^{b}X_i:1\le a\le b\le t\right\}.
                                                               \tag{4.1}
\end{aligned}
\]

### Theorem 4.1 (intersection endpoint monoid)

For two nonempty sequences \(X,Y\),

\[
\begin{aligned}
 \kappa(XY)
   &=\kappa(X)\cap\kappa(Y),\\
 \operatorname{Pre}(XY)
   &=\operatorname{Pre}(X)\cup
     \{\kappa(X)\cap P:P\in\operatorname{Pre}(Y)\},\\
 \operatorname{Suf}(XY)
   &=\operatorname{Suf}(Y)\cup
     \{S\cap\kappa(Y):S\in\operatorname{Suf}(X)\},\\
 \operatorname{Cov}(XY)
   &=\operatorname{Cov}(X)\cup\operatorname{Cov}(Y)\cup
     \{S\cap P:S\in\operatorname{Suf}(X),
                    P\in\operatorname{Pre}(Y)\}.     \tag{4.2}
\end{aligned}
\]

#### Proof

Every prefix of \(XY\) lies wholly in \(X\), or consists of all of \(X\)
and a prefix of \(Y\); the suffix statement is symmetric.  Every interval
lies wholly in one factor, or is a suffix of \(X\) followed by a prefix of
\(Y\).  Intersections give exactly (4.2).  \(\square\)

Both prefix- and suffix-intersection families have at most nine distinct
members: they form descending chains starting from an eight-set, and a
strict change deletes at least one coordinate.

For reversal one has exactly

\[
\begin{aligned}
 \kappa(X^{\mathrm{rev}})&=\kappa(X),&
 \operatorname{Cov}(X^{\mathrm{rev}})&=\operatorname{Cov}(X),\\
 \operatorname{Pre}(X^{\mathrm{rev}})&=\operatorname{Suf}(X),&
 \operatorname{Suf}(X^{\mathrm{rev}})&=\operatorname{Pre}(X).
                                                               \tag{4.2a}
\end{aligned}
\]

In the corrected split, the complement-owner row has the shape

\[
 H=H^L H^T,
 \qquad |H^L|=7401,\quad |H^T|=16909,                \tag{4.3}
\]

where \(H^L\) consists of the `7399` internal prefix triples and two
crossing triples.  Applying (4.2), and then adjoining the separate gap caps
\(\mathcal K=\{K_a:0\le a\le7400\}\), gives an exact compositional audit of
every upper target.

### Corollary 4.2 (weakest two-zone check)

Conditional on rank-nine bijectivity, ranks `10,...,17` are complete if and
only if

\[
 \binom{[17]}{\le7}\subseteq
 \operatorname{Cov}(H^L H^T)\cup\mathcal K.           \tag{4.4}
\]

Equivalently, for every cap \(C\) of rank at most seven, \(C\) is witnessed
internally in one owner zone, is obtained by intersecting a suffix of
\(H^L\) with a prefix of \(H^T\), or belongs to the physical boundary-gap
chain \(\mathcal K\).

This is the precise tail-ear/prefix chronology interface.  A protected
upper bank is any choice, for every such \(C\), of either one owner interval
\(I_C\) with

\[
 C\subseteq H_i\quad(i\in I_C),qquad
 \bigcap_{i\in I_C}H_i=C.                             \tag{4.5}
\]

or one physical boundary interval \([a,7403]\) with \(K_a=C\).

Certificates need not be disjoint.  An interval internal to a frozen owner
fragment survives arbitrary movement of other fragments; any legal reversal
that reverses its internal owner row only reverses the certificate.  For a
certificate inherited from a physical word, its whole supporting interval
\([p,q+2]\) when \(q\le7400\), or \([p,q+3]\) when \(q\ge7401\), must be
frozen.
A boundary certificate survives
exactly when the new suffix/prefix intersection in (4.2) remains \(C\).
Thus an ear completion may be audited using only its internal `Cov` bank and
its two endpoint chains, but it may not discard the endpoint chains.
In particular, each tail component or ear exports precisely the four-tuple
\((\kappa,\operatorname{Pre},\operatorname{Suf},\operatorname{Cov})\);
reversal swaps `Pre` and `Suf` while preserving \(\kappa\) and `Cov`, and
the ordered tail state is obtained by repeated application of (4.2).
Together with the prefix gap chain, condition (4.4) is then necessary and
sufficient.

The final left/tail split has at most \(9\cdot9=81\) new crossing cap
values.  At rank ten, all crossing owner intervals contain the same two
boundary owners, so at most one rank-ten colour is supplied across that
split.  The gap chain supplies at most one further rank-ten colour.  The
tail has `16908` internal owner transitions, hence supplies at most `16908`
distinct rank-ten targets.  Of the `19448` rank-ten targets, at least
`2540` must be supplied outside the tail, and at least `2538` must be
internal to the left owner block after allowing both the owner boundary and
the physical gap their maximum one colour each.

## 5. Three useful sufficient conditions

The exact test (3.6), together with the gap chain, is preferable when a
literal chronology is available.
The following stronger conditions are useful while constructing one.

### Theorem 5.1 (sharp universal clean-run count)

Let \(\rho_U\) be the number of maximal runs of owners contained in \(U\).
If

\[
                         \rho_U\le9,                 \tag{5.1}
\]

then \(U\) is covered.

#### Proof

Write \(r=|U|\) and \(d=r-9\).  Suppose \(U\) is missing.  For every clean
run \(J\), choose

\[
 x_J\in U\setminus\bigcup_{i\in J}M_i,               \tag{5.2}
\]

which exists by Theorem 3.2.  For every \(d\)-set \(D\subseteq U\), the
rank-nine owner \(U\setminus D\) occurs in one clean run \(J\).  Since
\(x_J\notin U\setminus D\), one has \(x_J\in D\).  Hence the selected
coordinates hit every \(d\)-subset of \(U\).

A hitting set for all \(d\)-subsets of an \(r\)-set has size at least
\(r-d+1=10\): otherwise its complement contains a \(d\)-set.  Therefore a
missing \(U\) has at least ten clean runs.  \(\square\)

The constant nine is sharp as a uniform owner-chronology guarantee.  For a
rank-ten target, owner-row missingness is exactly the separation of its ten
facets into ten distinct runs; the authenticated example in Section 6
attains this equality.  In the mixed physical word, full missingness also
requires that the target not belong to the gap chain.

For the final two-block split, if \(\rho_L(C),\rho_T(C)\) count clean runs
on the two sides, then

\[
 \rho(C)=\rho_L(C)+\rho_T(C)
 -\mathbf 1_{\{\text{the last left and first right owners are both
                    contained in }[17]\setminus C\}}.             \tag{5.3}
\]

Thus the right side of (5.3) being at most nine for every \(|C|\le7\) is a
simple checkable sufficient tail/prefix condition.

### Theorem 5.2 (sharp one-run length bound)

Let \(|U|=r\).  A run of distinct rank-nine owners contained in \(U\), of
length greater than

\[
                         \binom{r-1}{9},              \tag{5.4}
\]

must unite to \(U\).

#### Proof

If its union is proper, it is contained in \(U\setminus\{x\}\) for some
\(x\in U\), which has only \(\binom{r-1}{9}\) rank-nine subsets.  \(\square\)

The first forcing lengths for ranks `10,...,17` are

\[
 2,\ 11,\ 56,\ 221,\ 716,\ 2003,\ 5006,\ 11441.      \tag{5.5}
\]

The bound is sharp from length data alone: all rank-nine subsets of a fixed
\((r-1)\)-subset form a bad family of size \(\binom{r-1}{9}\).

### Theorem 5.3 (Johnson first-arrival flag)

Suppose the owner block \(M_\ell,\ldots,M_r\) is Johnson-adjacent, written

\[
 M_{i+1}=M_i-\{b_i\}+\{a_i\},
 \qquad \ell\le i<r.                                  \tag{5.6}
\]

Then for \(\ell\le p\le q\le r\),

\[
 \bigcup_{i=p}^{q}M_i
   =M_p\cup\{a_p,a_{p+1},\ldots,a_{q-1}\}.            \tag{5.7}
\]

Consequently, for \(U\supsetneq M_p\), define the first future arrival

\[
 \tau_p(x)=\min\{i:p\le i<r,\ a_i=x\},                \tag{5.8}
\]

with value \(+\infty\) if \(x\) is not added before this block ends.  Some
interval \([p,q]\) contained in the block has union \(U\) if and only if

\[
 \max_{x\in U\setminus M_p}\tau_p(x)
   <\min_{y\notin U}\tau_p(y).                         \tag{5.9}
\]

Here the minimum of the empty set is \(+\infty\); a required coordinate
with no future arrival makes the left side \(+\infty\).  When (5.9) holds,
one may take \(q=1+\max_{x\in U\setminus M_p}\tau_p(x)\).

#### Proof

Equation (5.7) follows by induction: passing from \(M_i\) to \(M_{i+1}\)
can add only \(a_i\) to the accumulated union.  The first endpoint after
the last required arrival witnesses \(U\) exactly when no forbidden
coordinate has arrived earlier.  \(\square\)

Ordering the eight coordinates outside \(M_p\) by finite first arrival
therefore gives one nested flag of at most eight upper targets from
that start.  The internal upper bank of a Johnson segment is exactly the
union of these flags over starts whose witnessing endpoints stay in the
segment.  If the entire owner row is Johnson-adjacent, its interval bank
contains every upper target exactly when these flags are surjective; in the
mixed physical schedule the separate gap chain may supply additional
targets.  Local diamonds make each step a singleton exchange; they impose
no ordering relation between required and forbidden first arrivals.

## 6. Exact failures of automatic propagation

### 6.1 Authenticated global owner-cycle counterexample

The file

```text
scratch/k17_opt28_connected_owner_cycle_20260731.word
SHA-256 a736ef9def43415ce54e6ca72abf5718e922e9d39de336b463dce7af3a1073aa
```

is an authenticated cyclic ordering of every rank-nine mask exactly once.
Every cyclic adjacency is a Johnson edge, and the `24310` adjacent
intersections are every rank-eight mask exactly once.  Nevertheless

\[
 U=\mathtt{0x7bf}
\]

is a missing rank-ten target.  Its ten facets occur at the following
one-based positions:

\[
 1547,2100,5641,6044,10925,12033,12556,14959,16792,18178. \tag{6.1}
\]

They are cyclically isolated, hence form ten clean runs.  Cutting the cycle
anywhere preserves the missing target and all remaining Johnson-local
transitions, although it deletes the one rank-eight colour on the cut edge.
The same cyclic chronology misses
`1900,911,128` targets in ranks `10,11,12`, respectively, and none in ranks
at least thirteen.

The independent cycle-shadow audit supporting these upper-hole counts is

```text
scratch/audit_independent_k17_opt28_owner_cycle_banks_shadows_20260731.py
SHA-256 c6834f6e6b168c7a639139b4c04ab01e1a7054018c429bceef3b231c5399e675

scratch/k17_opt28_independent_cycle_banks_shadows_20260731.audit.json
SHA-256 f79d95403a8a55e820497766a12adf3aeb3ec6a8cbb04195a91895600157c6be
payload 93a6bf299a5b055b3ad477a77857faf5305f4d6e1582c66f7b0f615dc82a28fe
```

This is a counterexample at the owner-chronology level.  It is not asserted
to be the selected mixed-width row of a completed physical `k=17` word.

### 6.2 Genuine five-letter Boolean-diamond stall

Let \(S\) have rank five and \(V\) rank eight, with
\(V\setminus S=\{g,x,y\}\).  Choose distinct \(a,b\in S\), and put

\[
 C=(S\setminus\{a,b\})\cup\{g\},\qquad
 R=C\cup\{a,x\},\qquad T=C\cup\{b,y\}.                \tag{6.2}
\]

This is the proposal's literal diamond: \(R,S,T\) have ranks `6,5,6`,
their two adjacent unions have rank seven, and
\(R\cup S\cup T=V\).  Choose \(r\in R,t\in T\) and distinct
\(u,v\notin V\), and extend it to the linear five-letter word

\[
 L=(R\setminus\{r\})\cup\{u\},\qquad
 (L,R,S,T,N),\qquad
 N=(T\setminus\{t\})\cup\{v\}.                       \tag{6.3}
\]

All four adjacent unions have rank seven.  Its three triple unions are

\[
 (R\cup S)\cup\{u\},\qquad V,\qquad
 (S\cup T)\cup\{v\},                                 \tag{6.4}
\]

all of rank eight.  The two four-window owners are the distinct rank-nine
sets \(V\cup\{u\}\) and \(V\cup\{v\}\), meeting in \(V\), while the full
five-window union is the rank-ten set \(V\cup\{u,v\}\).

Thus a genuine local Boolean diamond supplies the exact `7,8,9,10`
staircase but contains no condition forcing any rank-eleven coordinate.
This is a local physical counterexample to automatic continued growth, not
a global lower-layer atlas.  Together with Section 6.1 it separates the two
false implications: rank-nine ownership does not force rank ten globally,
and literal local diamonds do not force the rest of the upper tower.

## 7. Exact remaining boundary

The uniform-four-window reading of the proposal is closed by Theorem 2.1,
but the corrected triple-window prefix remains open.  Conditional on
constructing that mixed rank-nine row, the minimum honest upper hypothesis
is exactly

\[
 \forall C\in\binom{[17]}{\le7}\quad
 C\in\operatorname{Cov}(H^L H^T)\cup\mathcal K.      \tag{7.1}
\]

Equivalently, every cap needs one protected clean-run certificate (4.5) or
one boundary-gap witness.  A stronger monotone sufficient condition is that
every cap not already in \(\mathcal K\) have at most nine clean runs, or
have one clean run exceeding the sharp length in (5.4).  On Johnson pieces,
the equivalent constructive data are the first-arrival flags of
Theorem 5.3.

Therefore a tail-ear theorem must export not only fresh rank-eight and
rank-nine labels, but also its internal cap bank and both endpoint
intersection chains.  A prefix theorem must cover the residual caps under
the exact product in (4.2), with the physical gap chain carried separately.
Marginal rank counts, local Boolean diamonds, and rank-nine bijectivity
alone are insufficient.
