# Second-wave AD: exact depth-two literalization of rainbow Johnson forests

## Outcome

The depth-one two-sided-rainbow conversion extends to the five central
ranks by a pervasive shared-seam replacement.  The minimal local
requirements for the canonical \(D_i,V_i\) shared-seam masks are only the
exclusion of positive and zero coordinate runs of length one.
Equivalently, consecutive lower edge colours and consecutive upper edge
colours must be distinct.  No exclusion of length-two runs is needed.

For a globally two-sided-rainbow spanning forest, let

\[
W=\binom{2m}{m},\qquad
N_1=\binom{2m}{m-1},\qquad
N_2=\binom{2m}{m-2},
\]

let \(e\) be its total number of edges, put

\[
\delta=N_1-e,
\]

and let \(c_{\ge2}\) count components with at least two edges.  Define
\(M_2^-\) and \(M_2^+\) to be the missing distinct lower and upper
depth-two colours.  Then, for \(m\ge3\), there is a literal OR word
covering every set in ranks \(m-2,\ldots,m+2\) whose length satisfies

\[
\boxed{
L_5\le
W+(N_1-N_2)+c_{\ge2}+\delta
+M_2^-+M_2^++\min\{M_2^-,M_2^+\}.
}
\tag{A}
\]

Since the number of forest components is

\[
W-e=\operatorname{Cat}_m+\delta,
\qquad
\operatorname{Cat}_m=\frac{W}{m+1},
\]

one also has the support-only estimate

\[
\boxed{
L_5\le
W+(W-N_2)+2\delta
+M_2^-+M_2^++\min\{M_2^-,M_2^+\}.
}
\tag{B}
\]

Since

\[
M_2^-+M_2^++\min\{M_2^-,M_2^+\}
\le\frac32(M_2^-+M_2^+),
\]

a convenient symmetric version is

\[
\boxed{
L_5\le
W+\left(4-\frac6{m+2}\right)\operatorname{Cat}_m
+2\delta+\frac32(M_2^-+M_2^+).
}
\tag{C}
\]

The exact constants are

\[
N_1-N_2
=\frac{3m}{(m+1)(m+2)}W,
\]

\[
N_1-N_2
=\left(3-\frac6{m+2}\right)\operatorname{Cat}_m,
\]

\[
W-N_2
=\frac{4m+2}{(m+1)(m+2)}W
=\left(4-\frac6{m+2}\right)\operatorname{Cat}_m.
\]

Consequently, the already proved first-band forest would give a
\(W+o(W)\) five-band word as soon as

\[
\boxed{M_2^-+M_2^+=o(W).}
\tag{D2RS, UNPROVED}
\]

This is now the sole new asymptotic hypothesis in the canonical
depth-two forest route.  First-band rainbowness does not imply it.

## 1. Why sparse extension of the old first-band word is impossible

Let \(A_1,\ldots,A_L\) be an OR word, and let
\(\mathcal R_r(A)\) be its represented \(r\)-sets.  Choose one witnessing
interval \([\ell(S),u(S)]\) for every \(S\in\mathcal R_r(A)\).

Two distinct equal-rank targets cannot have the same left endpoint:
intervals with a common left endpoint are nested, so their unions are
comparable.  The same argument applies to right endpoints.  Moreover,

\[
A_{\ell(S)}\subseteq S,\qquad A_{u(S)}\subseteq S.
\]

Therefore

\[
\boxed{
|\mathcal R_r(A)|
\le \#\{j:|A_j|\le r\}.
}
\tag{1.1}
\]

At depth two,

\[
\frac{N_2}{W}
=\frac{m(m-1)}{(m+1)(m+2)}
=1-\frac{4m+2}{(m+1)(m+2)}.
\tag{1.2}
\]

Thus a five-band word needs \(N_2=W-O(W/m)\) physical entries of
size at most \(m-2\).

The singleton-capped depth-one forest word has only two such entries per
nontrivial component; the other entries have ranks \(m-1\) or \(m\).
If it has \(p=o(W)\) nontrivial components, then inserting \(R\) new
entries and changing \(t\) old entries requires

\[
\boxed{R+t\ge N_2-2p=W-o(W).}
\tag{1.3}
\]

This includes arbitrary seam-crossing witnesses after the edits.
Therefore a depth-two construction of coefficient one cannot preserve the
old facet word as a subsequence or append an independent core.  It must
replace almost every old physical position by low shared seams.  The
construction below does exactly that.

## 2. Minimal local hypotheses

Let

\[
T_0,T_1,\ldots,T_s\in\binom{[2m]}m
\]

be a Johnson path, written

\[
T_i=T_{i-1}-\{r_i\}+\{b_i\},
\qquad 1\le i\le s.
\tag{2.1}
\]

For each edge define its lower and upper colours

\[
C_i=T_{i-1}\cap T_i,\qquad
U_i=T_{i-1}\cup T_i.
\tag{2.2}
\]

For each internal junction define

\[
D_i=C_i\cap C_{i+1},\qquad
V_i=U_i\cup U_{i+1},
\qquad 1\le i<s.
\tag{2.3}
\]

The exact local criterion is

\[
\boxed{
b_i\ne r_{i+1}
\quad\hbox{and}\quad
r_i\ne b_{i+1}
\qquad(1\le i<s).
}
\tag{LP}
\]

Indeed, viewed inside \(T_i\),

\[
C_i=T_i-\{b_i\},\qquad
C_{i+1}=T_i-\{r_{i+1}\},
\]

so

\[
C_i=C_{i+1}
\quad\Longleftrightarrow\quad
b_i=r_{i+1}.
\tag{2.4}
\]

Likewise,

\[
U_i=T_i\cup\{r_i\},\qquad
U_{i+1}=T_i\cup\{b_{i+1}\},
\]

and hence

\[
U_i=U_{i+1}
\quad\Longleftrightarrow\quad
r_i=b_{i+1}.
\tag{2.5}
\]

Thus (LP) is equivalent to

\[
C_i\ne C_{i+1},\qquad U_i\ne U_{i+1}.
\]

Under (LP),

\[
|D_i|=m-2,\qquad |V_i|=m+2.
\tag{2.6}
\]

The first failure in (LP) is exactly an internal positive coordinate run
of length one, with trace \(0,1,0\).  The second is exactly an internal
zero run of length one, with trace \(1,0,1\).  Hence (LP), not any
length-two run condition, is the minimal rank-correctness hypothesis for
the shared-seam construction.

Global lower- and upper-rainbowness imply (LP), but are much stronger than
what the path-level literal identities require.

### Exact cut repair when (LP) fails

Form a graph whose vertices are the edge occurrences of the path and whose
edges are the bad consecutive pairs \(\{i,i+1\}\) at which (LP) fails.
A set of path edges can be deleted so that every resulting fragment
satisfies (LP) if and only if it is a vertex cover of this bad-junction
graph.

The graph is a subgraph of a path and is bipartite.  Therefore its minimum
cut size is exactly its maximum matching size.  Deleting a minimum cover
increases the number of path components by precisely that amount.  This is
the sharp local repair cost for making the canonical depth-two colours have
the correct ranks.  All support defects in later formulas must then be
recomputed for the cut forest.

For a globally two-sided-rainbow forest the bad-junction graph is empty.

## 3. The path-level shared-seam word

Assume (LP).  For an internal lower facet \(C_i\), \(2\le i\le s-1\),
one has

\[
D_{i-1}=C_i-\{b_{i-1}\},
\qquad
D_i=C_i-\{r_{i+1}\}.
\tag{3.1}
\]

Consequently

\[
C_i\setminus(D_{i-1}\cup D_i)
\]

is empty unless

\[
b_{i-1}=r_{i+1}=x_i,
\]

in which case it is the singleton \(\{x_i\}\).  This exceptional case is
exactly the trace

\[
0,1,1,0
\]

on \(T_{i-2},T_{i-1},T_i,T_{i+1}\), namely an internal positive run of
length two.

Define \(Z_i\) to be omitted in the first case and to be
\(\{x_i\}\) in the second.  Then

\[
\boxed{
C_i=D_{i-1}\cup Z_i\cup D_i.
}
\tag{3.2}
\]

Let

\[
a_0=T_0\setminus T_1=\{r_1\},\qquad
a_s=T_s\setminus T_{s-1}=\{b_s\}.
\tag{3.3}
\]

For \(s=0\), emit \(T_0\).  For \(s=1\), emit

\[
a_0,C_1,a_s.
\tag{3.4}
\]

For \(s=2\), emit

\[
a_0,C_1,D_1,C_2,a_2.
\tag{3.5}
\]

For \(s\ge3\), emit

\[
\boxed{
a_0,C_1,D_1,Z_2,D_2,Z_3,\ldots,
D_{s-2},Z_{s-1},D_{s-1},C_s,a_s,
}
\tag{3.6}
\]

with every empty \(Z_i\) omitted.

### Theorem 3.1 (literal five-rank path theorem)

The \(s=0\) one-letter word, or the applicable word (3.4), (3.5), or
(3.6), represents, by contiguous unions,

\[
C_i,\quad D_i,\quad T_i,\quad U_i,\quad V_i
\]

for every valid index.  Thus it represents every designated path colour in
ranks \(m-2,m-1,m,m+1,m+2\).

If \(\rho_2^+(P)\) is the number of internal positive runs of length two,
then its exact physical length is

\[
\begin{cases}
1,&s=0,\\
3,&s=1,\\
(s+1)+2+\rho_2^+(P),&s\ge2.
\end{cases}
\tag{3.7}
\]

#### Proof

Every \(D_i\) is literal.  The endpoint facets \(C_1,C_s\) are literal.
When \(s\ge2\), choose the endpoint facet witnesses to run from \(C_1\)
through \(D_1\), and from \(D_{s-1}\) through \(C_s\), respectively;
their unions remain \(C_1,C_s\) because the seam is a subset of the
facet.  For \(2\le i\le s-1\), the interval from the occurrence of
\(D_{i-1}\) through \(Z_i\), when present, to the occurrence of \(D_i\)
has union \(C_i\) by (3.2).

Let \(I(C_i)\) denote these facet intervals.  Consecutive facet intervals
overlap at their common \(D_i\).  Hence their interval hull is contiguous.
Since
consecutive distinct \(C_i,C_{i+1}\) are two facets of \(T_i\),

\[
T_i=C_i\cup C_{i+1}
\qquad(1\le i<s).
\tag{3.8}
\]

The endpoint identities are

\[
T_0=a_0\cup C_1,\qquad
T_s=C_s\cup a_s.
\tag{3.9}
\]

Thus every \(T_i\) has an interval witness, and the witnesses for
\(T_{i-1}\) and \(T_i\) overlap in the facet witness \(I(C_i)\).
Taking their interval hull gives

\[
U_i=T_{i-1}\cup T_i.
\tag{3.10}
\]

The witnesses for \(U_i,U_{i+1}\) overlap in the witness for \(T_i\).
Their interval hull therefore has union

\[
V_i=U_i\cup U_{i+1}.
\tag{3.11}
\]

Condition (LP) guarantees that (3.8) and (3.11) have the advertised
cardinalities.  This proves all literal identities.

For \(s\ge2\), the applicable word has two caps, two endpoint facets,
\(s-1\) depth-two seam occurrences, and one singleton for each positive
two-run.
Its length is \(s+3+\rho_2^+=(s+1)+2+\rho_2^+\).  The other two cases
are immediate.  \(\square\)

### Scope of the \(\rho_2^+\) charge

The singleton \(Z_i\) is optimal in the declared occurrence-faithful seam
layout: if \(D_{i-1}=D_i=D\) and \(C_i=D\cup\{x_i\}\), an interval
whose declared endpoints are those two seam occurrences needs at least one
intervening letter containing \(x_i\), and \(\{x_i\}\) suffices.

This is not an unconditional lower bound for arbitrary OR layouts.
Coincident seam labels can sometimes share one physical occurrence after a
different local reset.  Section 6 gives an explicit compression.  Thus
(3.7) is the exact length for the stated canonical policy and an upper bound
for unrestricted literalization.

## 4. Forest-level support theorem

Let \(F\) be a spanning linear forest of \(J(2m,m)\), oriented
componentwise, and assume every nontrivial component satisfies (LP).
Let

- \(c_0\) be the number of isolated vertices;
- \(c_1\) be the number of one-edge components;
- \(c_{\ge2}\) be the number of components with at least two edges;
- \(e\) be the total number of forest edges.

Write

\[
p=c_1+c_{\ge2}.
\]

Across all edge and two-edge occurrences define the distinct supports

\[
\mathcal C=\{C_i\},\qquad
\mathcal U=\{U_i\},\qquad
\mathcal D=\{D_i\},\qquad
\mathcal V=\{V_i\}.
\tag{4.1}
\]

Put

\[
M_1^-=N_1-|\mathcal C|,
\qquad
M_1^+=N_1-|\mathcal U|,
\tag{4.2}
\]

\[
M_2^-=N_2-|\mathcal D|,
\qquad
M_2^+=N_2-|\mathcal V|.
\tag{4.3}
\]

The number of depth-two occurrences on each side is

\[
\boxed{
K_2=\sum_P(|E(P)|-1)_+
=e-c_1-c_{\ge2}=e-p.
}
\tag{4.4}
\]

Concatenating the component words from Theorem 3.1 and emitting every
isolated middle vertex literally gives an exact raw length

\[
W+c_1+2c_{\ge2}+\rho_2^+(F).
\tag{4.5}
\]

It already represents every middle vertex and every label in the four
supports (4.1).  Appending each missing mask once as a literal one-entry
interval proves:

### Theorem 4.1 (general depth-two completion)

\[
\boxed{
\begin{aligned}
L_5(F)\le {}&
W+c_1+2c_{\ge2}+\rho_2^+(F)\\
&+M_1^-+M_1^++M_2^-+M_2^+.
\end{aligned}
}
\tag{4.6}
\]

The right side is the exact length of the declared canonical-support
completion policy.  It may exceed the optimum because incidental intervals,
including intervals crossing component seams, may represent labels outside
the four canonical supports.

### Length-two runs are already support defects

For each path, list its \(D\)-occurrences in their chronological order.
By (3.1),

\[
\boxed{
\rho_2^+(F)
=\#\{\hbox{adjacent equal \(D\)-occurrences}\}.
}
\tag{4.7}
\]

For one fixed label, the number of adjacent equal pairs in all of its
occurrence runs is at most its total occurrence multiplicity minus one.
Summing over labels gives

\[
\boxed{
\rho_2^+(F)
\le K_2-|\mathcal D|
=K_2-N_2+M_2^-.
}
\tag{4.8}
\]

Thus a separate hypothesis \(\rho_2^+=o(W)\) is unnecessary whenever the
lower depth-two support defect is \(o(W)\) and \(K_2-N_2=o(W)\).

## 5. Complementary polarity and the sharpened global theorem

Let \(F^\vee\) be the image of \(F\) under global set complementation,

\[
T\longmapsto [2m]\setminus T.
\]

This is an automorphism of \(J(2m,m)\), preserves the component types, and
maps the four supports as follows:

\[
C_i^\vee=[2m]\setminus U_i,\qquad
U_i^\vee=[2m]\setminus C_i,
\tag{5.1}
\]

\[
D_i^\vee=[2m]\setminus V_i,\qquad
V_i^\vee=[2m]\setminus D_i.
\tag{5.2}
\]

Hence complementation swaps \(M_1^-\) with \(M_1^+\), swaps
\(M_2^-\) with \(M_2^+\), and preserves their sums.

A positive length-two run in \(F^\vee\) is a zero length-two run in
\(F\), with trace \(1,0,0,1\).  Let its number be
\(\rho_2^0(F)\).  Applying (4.8) to \(F^\vee\) gives

\[
\boxed{
\rho_2^0(F)
\le K_2-|\mathcal V|
=K_2-N_2+M_2^+.
}
\tag{5.3}
\]

We may construct the word from \(F\) or globally from \(F^\vee\).
Choosing the shorter word in Theorem 4.1 yields

\[
\boxed{
\begin{aligned}
L_5(F)\le {}&
W+c_1+2c_{\ge2}
+M_1^-+M_1^++M_2^-+M_2^+\\
&+\min\{\rho_2^+(F),\rho_2^0(F)\}.
\end{aligned}
}
\tag{5.4}
\]

This is a global choice.  Complementing selected components separately
would generally destroy the spanning partition and is not asserted.
The choice also uses essentially that the ground set has size \(2m\) and
that the complete target band \(m-2,\ldots,m+2\) is invariant under
complementation.  It is not an automatic reduction for an asymmetric
target family or for odd ground-set size.

### Theorem 5.1 (two-sided-rainbow depth-two literalization)

Assume now that all lower edge colours are pairwise distinct and all upper
edge colours are pairwise distinct, separately.  Distinctness only of the
ordered lower-upper colour pairs would not be enough for the two separate
support counts below.  Here \(e\) is the total number of forest edges.
Then

\[
M_1^-=M_1^+=N_1-e=\delta.
\tag{5.5}
\]

Since \(K_2=e-c_1-c_{\ge2}\), equations (4.8), (5.3), and (5.4) give

\[
\begin{aligned}
L_5(F)\le{}&
W+c_1+2c_{\ge2}+2\delta+M_2^-+M_2^+\\
&+e-c_1-c_{\ge2}-N_2+\min\{M_2^-,M_2^+\}.
\end{aligned}
\]

After exact cancellation,

\[
\boxed{
L_5(F)\le
W+(N_1-N_2)+c_{\ge2}+\delta
+M_2^-+M_2^++\min\{M_2^-,M_2^+\}.
}
\tag{5.6}
\]

This is (A).  Because a spanning forest has

\[
c_0+c_1+c_{\ge2}=W-e
=W-N_1+\delta
=\operatorname{Cat}_m+\delta,
\]

\[
c_{\ge2}\le\operatorname{Cat}_m+\delta.
\tag{5.7}
\]

Using

\[
(N_1-N_2)+\operatorname{Cat}_m=W-N_2
\tag{5.8}
\]

in (5.6) proves (B).

No factor is hidden: the coefficient of \(\delta\) is one in the refined
bound (5.6) and two only after eliminating \(c_{\ge2}\) via (5.7).

### Corollary 5.2 (minimal asymptotic support hypothesis)

Suppose a sequence of globally two-sided-rainbow spanning forests satisfies

\[
\delta=o(W),\qquad M_2^-+M_2^+=o(W).
\tag{5.9}
\]

Then

\[
L_5=W+o(W).
\tag{5.10}
\]

Indeed, \(W-N_2=O(W/m)=o(W)\), and every remaining term in (B) is
nonnegative and \(o(W)\).

The known first-band forest already supplies \(\delta=o(W)\).  Therefore
(D2RS) is sufficient to extend the unconditional three-rank literal word
to ranks \(m-2,\ldots,m+2\).

Within the declared canonical-support completion policy, (D2RS) is also
the exact new vanishing-overhead gate, because every missing canonical
depth-two label is appended once.  It is not claimed necessary for an
arbitrary OR word: incidental or cross-component intervals can cover masks
outside the canonical supports.

## 6. Sharp local obstructions and scope

### 6.1 A four-state first-band-rainbow collision

Let \(R\) have size \(m-2\), and choose distinct
\(a,b,c,d\notin R\).  Consider

\[
R ab,\quad R bc,\quad R cd,\quad R da,
\tag{6.1}
\]

where juxtaposition denotes union with the displayed singleton labels.
The lower first-band colours are

\[
Rb,\quad Rc,\quad Rd,
\]

and the upper first-band colours are

\[
Rabc,\quad Rbcd,\quad Racd.
\]

They are pairwise distinct on each side.  Nevertheless,

\[
D_1=D_2=R,
\qquad
V_1=V_2=Rabcd.
\tag{6.2}
\]

The coordinate \(c\) has trace \(0,1,1,0\), while \(a\) has trace
\(1,0,0,1\).  Hence

\[
\rho_2^+=\rho_2^0=1,
\qquad
K_2-|\mathcal D|
=K_2-|\mathcal V|=1.
\tag{6.3}
\]

This saturates both collision inequalities (4.8) and (5.3).  It proves
that first-band two-sided rainbowness does not bootstrap even to adjacent
depth-two injectivity.

It also records the scope of the canonical \(\rho_2\) charge.  The
canonical word has seven entries, but the six-entry word

\[
\{a\},\ Rb,\ R,\ \{c\},\ Rd,\ \{a\}
\tag{6.4}
\]

already represents all designated masks of this path through depth two.
With positions numbered \(1,\ldots,6\), take facet witnesses

\[
I(C_1)=[2,2],\qquad I(C_2)=[3,4],\qquad I(C_3)=[5,5],
\]

middle witnesses

\[
[1,2],\quad[2,4],\quad[3,5],\quad[5,6],
\]

upper witnesses

\[
[1,4],\quad[2,5],\quad[3,6],
\]

and depth-two upper witnesses \([1,5]\) and \([2,6]\).
Thus \(\rho_2\) is not an unrestricted lower bound on OR length.  What
cannot be compressed away inside the canonical support ledger is the fact
that the two depth-two windows contribute only one distinct lower label
and one distinct upper label.  An unrelated incidental interval could
still cover a different target, which is why the ledger is sufficient
rather than necessary for arbitrary OR words.

### 6.2 No length-two run rule controls nonadjacent support collisions

For \(m\ge7\), choose \(R\in\binom{[2m]}{m-2}\), choose
\(x\in R\), and choose nine distinct labels

\[
a,b,c,d,e,f,g,h,j\notin R.
\]

The following is a simple Johnson path:

\[
\begin{aligned}
T_0&=R\cup\{a,g\},\\
T_1&=R\cup\{a,b\},\\
T_2&=R\cup\{b,c\},\\
T_3&=(R-\{x\})\cup\{b,c,d\},\\
T_4&=(R-\{x\})\cup\{c,d,e\},\\
T_5&=(R-\{x\})\cup\{d,e,f\},\\
T_6&=R\cup\{e,f\},\\
T_7&=R\cup\{f,h\},\\
T_8&=R\cup\{h,j\}.
\end{aligned}
\tag{6.5}
\]

Its transitions remove and add, respectively,

\[
\begin{array}{c|cccccccc}
\text{transition}&1&2&3&4&5&6&7&8\\ \hline
\text{removed}&g&a&x&b&c&d&e&f\\
\text{added}&b&c&d&e&f&x&h&j.
\end{array}
\tag{6.6}
\]

Every finite internal positive or zero run has length three.  In
particular there is no positive or zero run of length one or two.

The lower colours are

\[
\begin{aligned}
&R a,\quad R b,\quad (R-x)bc,\quad (R-x)cd,\\
&(R-x)de,\quad (R-x)ef,\quad R f,\quad R h,
\end{aligned}
\tag{6.7}
\]

and are pairwise distinct.  The upper colours are

\[
\begin{aligned}
&Rabg,\quad Rabc,\quad Rbcd,\quad (R-x)bcde,\\
&(R-x)cdef,\quad Rdef,\quad Refh,\quad Rfhj,
\end{aligned}
\tag{6.8}
\]

and are also pairwise distinct.  Yet the depth-two lower colours satisfy

\[
D_1=D_7=R.
\tag{6.9}
\]

There is no adjacent \(D\)-collision here, so \(\rho_2^+=0\); the
collision is genuinely nonlocal.  Global complementation gives the
analogous nonlocal upper collision.

Thus first-band colours plus all run information through depth two do not
control the distinct depth-two support.  A global support theorem such as
(D2RS), not another local run exclusion, is indispensable.

### 6.3 Even geodesic components can collide with one another

No componentwise run hypothesis can control the forestwide support.
Choose distinct \(a,b,c,d\notin R\) and take the two disjoint path
components

\[
Rab,\quad Rbc,\quad Rcd
\tag{6.10}
\]

and

\[
Rac,\quad Rad,\quad Rbd.
\tag{6.11}
\]

The six middle vertices are the six distinct two-element extensions of
\(R\) inside \(\{a,b,c,d\}\).  The four lower colours are exactly

\[
Ra,\quad Rb,\quad Rc,\quad Rd,
\]

and the four upper colours are exactly

\[
Rabc,\quad Rabd,\quad Racd,\quad Rbcd.
\]

Thus the two-component forest is globally two-sided-rainbow.  Each
component is geodesic: an inserted coordinate is never removed and a
removed coordinate never returns.  In particular neither component has
any finite internal positive or zero run.

Nevertheless both components have lower depth-two colour \(R\) and upper
depth-two colour \(Rabcd\).  Hence local run restrictions of arbitrary
radius cannot rule out cross-component depth-two collisions.  The
obstruction in (D2RS) is genuinely global.

### 6.4 Occurrence feasibility

The number of distinct depth-two colours cannot exceed the occurrence
count \(K_2=e-p\).  Therefore

\[
M_2^-\ge(N_2-K_2)_+,\qquad
M_2^+\ge(N_2-K_2)_+.
\tag{6.12}
\]

For a near-spanning first-band forest these lower bounds are only \(o(W)\);
they do not obstruct (D2RS).  They do show that perfect depth-two
rainbowness may require more path breaks than the first-band optimum.

## 7. Exact remaining theorem and implication scope

The current unconditional theorem provides globally two-sided-rainbow
spanning forests with

\[
e=N_1-o(W),
\qquad
\delta=N_1-e=o(W).
\]

What is not proved is that one can choose such forests so that the two
families

\[
\{C_i\cap C_{i+1}\},
\qquad
\{U_i\cup U_{i+1}\}
\]

miss only \(o(W)\) distinct targets in their respective ranks.  The exact
second-wave remaining statement is:

> **Depth-two rainbow-support lemma (D2RS) — UNPROVED.**
> For every sufficiently large integer \(m\), there is a spanning Johnson
> linear forest \(F_m\) on \(\binom{[2m]}m\) such that:
>
> 1. all lower edge colours are pairwise distinct and all upper edge
>    colours are pairwise distinct, separately;
> 2. as \(m\to\infty\), \(\delta_m/W_m\to0\);
> 3. as \(m\to\infty\),
>    \((M_{2,m}^-+M_{2,m}^+)/W_m\to0\).

By Theorem 5.1, D2RS implies a literal \(W+o(W)\) word covering all five
central ranks.  It is a sufficient direct-word statement.  It is not
equivalent to MWB, does not imply labelled common-owner synchronization,
and uses no exact wreath factor.

The route is genuinely exhausted at D2RS.  The local literal identities,
all component and run charges, the complementary-polarity improvement,
and every factor in (A) and (B) are proved.  The missing content is global
near-surjectivity of the two depth-two support maps in one already
near-rainbow spanning chronology.

Independent proof audits separately checked the path interval witnesses,
the \(s=2\) boundary case, both collision identities, complement duality,
the component ledger, and every cancellation in (A)--(C).  No additional
unproved lemma is used.

No web search or finite/computational search was used.
