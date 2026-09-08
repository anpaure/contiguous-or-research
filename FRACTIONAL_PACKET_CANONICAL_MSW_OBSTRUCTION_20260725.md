# A Catalan packet obstruction for the canonical MSW factor

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, random
experiment, solver, or asymptotic matching theorem is used.

## 0. Outcome

This note does **not** prove or disprove \(\mathrm{FSP}_A\) over the whole
exact-factor fibre.  It does prove that the unchanged canonical
Mütze--Standke--Wiechert factor is separated from \(\mathrm{FSP}_A\) by a
positive-density exact-factor edit barrier.

Let

\[
 n=2m+1,\qquad t=\operatorname{Cat}_m=\frac1{m+1}\binom{2m}{m},
\]

and let \(F_m^{\rm MSW}\) be the canonical exact wreath factor indexed by
the Dyck words of semilength \(m\).  For every \(m\ge4\), every balanced
quota system containing depth one satisfies

\[
 \boxed{
 \vartheta(F_m^{\rm MSW},\beta)
 \ge \operatorname{Cat}_{m-4}.
 }
 \tag{0.1}
\]

Since

\[
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
 \longrightarrow\frac1{256},
\]

the left side is \(\Omega(t)\), whereas \(\mathrm{FSP}_A\) asks for
\(o_A(t/\sqrt m)\).  Thus the canonical factor fails the fractional
packet theorem by a factor of order \(\sqrt m\).

Since every integral quota-safe exceptional family is a packet vertex
cover, the same argument also gives

\[
 \tau(F_m^{\rm MSW},\beta)
 \ge\vartheta(F_m^{\rm MSW},\beta)
 \ge\operatorname{Cat}_{m-4}.
\]

Thus the canonical factor fails the hard-quota core theorem at positive
Catalan density as well.

The obstruction is robust.  If \(F\) is any exact factor and

\[
 d(F,F_m^{\rm MSW})
 :=|F_m^{\rm MSW}\setminus F|
 =|F\setminus F_m^{\rm MSW}|,
\]

then

\[
 \boxed{
 \vartheta(F,\beta)
 \ge
 \bigl(\operatorname{Cat}_{m-4}-d(F,F_m^{\rm MSW})\bigr)_+.
 }
 \tag{0.2}
\]

Consequently any factor satisfying \(\mathrm{FSP}_A\) must replace at
least

\[
 \left(\frac1{256}-o(1)\right)t
\]

canonical wreaths.  No sparse family of exact-factor trades, and no
trajectory which leaves all but \(o(t)\) canonical rows untouched, can
prove \(\mathrm{FSP}_A\).

The proof is a bounded-congestion packing in the exact compressed cut dual
(3.14) of `PACKET_HALL_RECOURSE_20260725.md`.  Its local seed is an explicit
three-owner collision in semilength four; Dyck-suffix locality suspends that
seed independently over all \(\operatorname{Cat}_{m-4}\) suffixes.

## 1. A general disjoint-packet dual certificate

Fix one exact factor \(F\), integral quotas \(\beta(a)\), owner sets
\(\mathcal O_a\subseteq F\), and packet sizes

\[
 k_a=\beta(a)+1.
\]

Recall that the survival packets for resource \(a\) are all
\(k_a\)-subsets of \(\mathcal O_a\).

### Lemma 1.1 -- bounded-congestion packet packing

Let \(\mathcal A\) be a resource family.  Suppose that for every
\(a\in\mathcal A\) one has selected a packet

\[
 P_a\subseteq\mathcal O_a,
 \qquad |P_a|=k_a,
\]

and that every wreath belongs to at most \(D\) selected packets, where
\(D\ge1\).  Then

\[
 \boxed{
 \vartheta(F,\beta)\ge\frac{|\mathcal A|}{D}.
 }
 \tag{1.1}
\]

In particular, pairwise disjoint selected packets give
\(\vartheta(F,\beta)\ge|\mathcal A|\).

#### Proof

In the packet-packing dual, assign weight \(1/D\) to every selected packet
and zero to every other packet.  The congestion at a wreath is at most one,
so the assignment is feasible and has value \(|\mathcal A|/D\).

The same certificate can be checked directly in the compressed cut dual.
Set \(Y_a=1/D\) on \(\mathcal A\).  For every \(Z\subseteq F\),

\[
 \bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
 \le |P_a\cap Z|.
 \tag{1.2}
\]

Indeed \(P_a\setminus Z\subseteq\mathcal O_a\setminus Z\), so the
untruncated left side is at most
\(k_a-|P_a\setminus Z|=|P_a\cap Z|\).  Hence

\[
 \sum_{a\in\mathcal A}
 \frac1D
 \bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
 \le
 \frac1D\sum_{a\in\mathcal A}|P_a\cap Z|
 \le |Z|.
\]

These are exactly the cuts in (3.14), proving (1.1).  \(\square\)

## 2. The semilength-four three-owner seed

Use \(1\) for an up-step and \(0\) for a down-step.  For a Dyck root
\(w\) of semilength four, write the MSW flip permutation as

\[
 \pi(w)=(a_0,b_0,a_1,b_1,a_2,b_2,a_3,b_3).
\]

The three roots

\[
 w^{(1)}=11110000,
 \qquad
 w^{(2)}=11101000,
 \qquad
 w^{(3)}=11001100
 \tag{2.1}
\]

have flip permutations

\[
\begin{aligned}
 \pi(w^{(1)})&=(8,2,6,4,5,3,7,1),\\
 \pi(w^{(2)})&=(8,2,4,3,6,5,7,1),\\
 \pi(w^{(3)})&=(4,2,3,1,8,6,7,5).
\end{aligned}
\tag{2.2}
\]

These three identities follow directly from the recursive MSW formula

\[
 \pi(1u0v)
 =\bigl(|u|+2,\ |u|+2-\pi(\operatorname{rev}u),\ 1,\
              |u|+2+\pi(v)\bigr).
 \tag{2.3}
\]

Let \(x_i\) be the balanced state after \(i\) complete MSW moves in the
column rooted at \(w\).  At the internal state \(x_i\), the second-upper
colour is

\[
 \Gamma(x_i)=x_i\cup\{a_i,b_{i-1}\}.
 \tag{2.4}
\]

For the three roots in (2.1), the state at \(i=2\) and its colour are

\[
\begin{array}{c|c|c}
 w&x_2&\Gamma(x_2)\\ \hline
 11110000&\{1,3,6,8\}&\{1,3,4,5,6,8\}\\
 11101000&\{1,4,5,8\}&\{1,3,4,5,6,8\}\\
 11001100&\{3,4,5,6\}&\{1,3,4,5,6,8\}.
\end{array}
\tag{2.5}
\]

For example, in the first row the first two complete moves are

\[
 \{1,2,3,4\}
 \xrightarrow{+8-2}
 \{1,3,4,8\}
 \xrightarrow{+6-4}
 \{1,3,6,8\},
\]

and (2.4) adjoins \(a_2=5\) and \(b_1=4\).  The other two rows are the
same literal check from (2.2).

Put

\[
 T_0=\{1,3,4,5,6,8\}.
 \tag{2.6}
\]

Its eight-letter incidence word is \(10111101\).  In expressions such as
\(T_0V\) below, concatenation refers to this incidence word followed by
the Dyck word \(V\).

Equation (2.5) is therefore a genuine three-owner colour collision in the
canonical semilength-four factor.  It is the collision companion to the
well-known contextual hole seed, but the argument below uses only the
explicit collision (2.5).

## 3. Dyck-suffix suspension of the collision

Let \(V\) be any Dyck word of semilength \(m-4\).  Concatenation gives the
three Dyck roots

\[
 w^{(1)}V,\qquad w^{(2)}V,\qquad w^{(3)}V
 \tag{3.1}
\]

of semilength \(m\).

We use the following elementary locality fact.

### Lemma 3.1 -- prefix locality

Let \(P\) be a balanced word and let \(V\) be Dyck.  If the coordinate
selected by the MSW map \(g\) on \(P\) lies in \(P\), then

\[
 g(PV)=g(P)V.
 \tag{3.2}
\]

If the subsequent coordinate selected by \(h\) also lies in \(P\), then

\[
 f(PV)=f(P)V.
 \tag{3.3}
\]

#### Proof

The statistic \(d_0\) used by \(g\) counts down-steps starting at height
zero.  A Dyck suffix, begun at height zero, has no such down-step.  Hence
the candidate count and the selected prefix candidate are unchanged.

After \(g\) changes one down-step to an up-step, the suffix begins at
height two.  Every up-step in the Dyck suffix then starts at height at least
two, so none enters the height-zero-or-one candidate list used by \(h\).
The selected prefix coordinate is again unchanged.  \(\square\)

Apply Lemma 3.1 successively to the first two complete moves of every row
of (2.5), and once more to the \(g\)-move selecting \(a_2\).  All selected
coordinates lie among the first eight positions by (2.2).  Therefore the
three extended columns have at their second internal states the common
colour

\[
 \Gamma(x_2V)=T_0V.
 \tag{3.4}
\]

In the odd wreath, a core rank-\((m+2)\) colour \(T\) corresponds by
complementation to the lower depth-one target

\[
 S(T)=\{\infty\}\cup([2m]\setminus T).
 \tag{3.5}
\]

Thus put

\[
 S_V=\{\infty\}\cup([2m]\setminus T_0V).
 \tag{3.6}
\]

The three canonical wreaths indexed by (3.1) all belong to the owner set
of \(S_V\).

Distinct suffixes \(V\) give distinct targets \(S_V\).  More importantly,
the three-owner families

\[
 \mathcal T_V
 :=\{E(w^{(1)}V),E(w^{(2)}V),E(w^{(3)}V)\}
 \tag{3.7}
\]

are pairwise disjoint.  Indeed a root word has a unique first-eight-letter
prefix and remaining suffix, and the three prefixes in (2.1) are distinct.
The MSW cycle factor has one distinct wreath for every Dyck root.

There are exactly

\[
 |\mathcal D_{m-4}|=\operatorname{Cat}_{m-4}
 \tag{3.8}
\]

such disjoint owner triples.

## 4. The packet lower bound

At depth one,

\[
 \lambda_1=\frac{m+2}{m}\in(1,2)
 \qquad(m\ge3),
\]

so every balanced quota has value either one or two.

Fix an arbitrary balanced depth-one quota \(\beta_1\).  For each suffix
\(V\):

* if \(\beta_1(S_V)=1\), choose any two members of \(\mathcal T_V\);
* if \(\beta_1(S_V)=2\), choose all three members of \(\mathcal T_V\).

The chosen set \(P_V\) has cardinality \(\beta_1(S_V)+1\) and lies inside
the owner set of \(S_V\).  Hence it is a survival packet.  By (3.7), the
packets \(P_V\) are pairwise disjoint.  Lemma 1.1 with \(D=1\) gives

\[
 \vartheta(F_m^{\rm MSW},\beta_1)
 \ge\operatorname{Cat}_{m-4}.
 \tag{4.1}
\]

Adding more controlled depths only adds packet constraints, so (4.1) proves
(0.1) for every fixed Gaussian window and every choice of balanced quotas
through that window.

The exact density is

\[
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
 =
 \frac{(m-2)(m-1)m(m+1)}
 {16(2m-7)(2m-5)(2m-3)(2m-1)}
 =\frac1{256}+O(m^{-1}).
 \tag{4.2}
\]

Consequently

\[
 \frac{\vartheta(F_m^{\rm MSW},\beta)}{t/\sqrt m}
 \ge
 \left(\frac1{256}+o(1)\right)\sqrt m
 \longrightarrow\infty.
 \tag{4.3}
\]

This is an all-dimensional theorem, not an inference from the finite
positive missing fractions of the canonical factor.

## 5. Robustness under exact-factor trades

Let \(F\) be another exact factor and put

\[
 d=|F_m^{\rm MSW}\setminus F|.
\]

The owner triples \(\mathcal T_V\) are pairwise disjoint.  Hence deleting
\(d\) canonical wreaths can meet at most \(d\) of them.  For at least

\[
 \operatorname{Cat}_{m-4}-d
\]

suffixes \(V\), all three canonical owner wreaths remain in \(F\).  The
target \(S_V\) is therefore still owned by those three wreaths, regardless
of what new wreaths were inserted into \(F\).

For each intact triple choose the two- or three-element packet dictated by
the new quota \(\beta_1(S_V)\), exactly as in Section 4.  These packets are
still disjoint, so Lemma 1.1 proves

\[
 \vartheta(F,\beta)
 \ge
 \bigl(\operatorname{Cat}_{m-4}-d\bigr)_+.
 \tag{5.1}
\]

This is (0.2).

Coordinate relabelling preserves packet-cover values.  Therefore (5.1)
also holds, with the same constant, around every relabelled canonical
factor \(\sigma F_m^{\rm MSW}\): replace the distance in (5.1) by
\(|\sigma F_m^{\rm MSW}\setminus F|\) and relabel the displayed packet
family by \(\sigma\).

### Corollary 5.1 -- positive-density trade barrier

If \(F_m\) satisfies the fractional survival-packet target

\[
 \vartheta_A(F_m)=o_A(t/\sqrt m),
\]

then

\[
 d(F_m,F_m^{\rm MSW})
 \ge
 \operatorname{Cat}_{m-4}-o_A(t/\sqrt m)
 =\left(\frac1{256}-o(1)\right)t.
 \tag{5.2}
\]

In particular, suppose an exact-factor trajectory starts at the canonical
factor and all its trades together remove only \(o(t)\) distinct canonical
wreaths.  No state on that trajectory can satisfy \(\mathrm{FSP}_A\).
If every trade replaces at most \(s\) previously untouched canonical
wreaths, at least

\[
 \left(\frac1{256}-o(1)\right)\frac ts
\]

such effective trades are necessary.

The theorem does not say that positive-density reconfiguration is
sufficient.  It proves that it is necessary even for the weaker
fractional packet gate.

## 6. Exact destruction cost inside the native \((2\ 3)\)-switch cube

The edit lower bound in Section 5 is not merely formal.  The exact MSW
transposition-component hierarchy locates the three distinguished owners
and gives positive-density exact rebundlings which destroy this particular
certificate.

Let \(\tau=(2\ 3)\).  The audited component hierarchy for the overlay of
\(F_m^{\rm MSW}\) and \(\tau F_m^{\rm MSW}\) is as follows.  Put

\[
 \mathcal A_j=
 \{1u0:u\in\mathcal D_{j+1}\}
 \mathbin{\dot\cup}
 \{10\,1v0:v\in\mathcal D_j\}.
 \tag{6.1}
\]

For every \(R\in\mathcal D_{m-j-2}\), the left side of one independently
switchable component is

\[
 \mathcal C_{j,R}=\{AR:A\in\mathcal A_j\},
 \tag{6.2}
\]

and

\[
 |\mathcal C_{j,R}|=\operatorname{Cat}_j+\operatorname{Cat}_{j+1}.
 \tag{6.3}
\]

These components partition all canonical rows.  Choosing the right side of
any component, independently of all others, gives another exact factor.

### Theorem 6.1 -- locations of the three owners

For every \(V\in\mathcal D_{m-4}\):

\[
 E(w^{(1)}V),E(w^{(2)}V)\in\mathcal C_{2,V},
 \qquad |\mathcal C_{2,V}|=7,
 \tag{6.4}
\]

while

\[
 E(w^{(3)}V)\in\mathcal C_{0,1100V},
 \qquad |\mathcal C_{0,1100V}|=2.
 \tag{6.5}
\]

The displayed components are distinct as \(V\) varies, and the component
in (6.4) is always different from the component in (6.5).

#### Proof

The words \(w^{(1)}=11110000\) and \(w^{(2)}=11101000\) are primitive
Dyck words of semilength four.  Thus each has the form \(1u0\) with
\(u\in\mathcal D_3\), placing both in \(\mathcal A_2\).  Appending \(V\)
gives (6.4).  Formula (6.3) gives

\[
 |\mathcal C_{2,V}|=\operatorname{Cat}_2+\operatorname{Cat}_3=2+5=7.
\]

On the other hand

\[
 w^{(3)}V=1100\,(1100V).
\]

Here \(1100\in\mathcal A_0=\{1100,1010\}\) and
\(1100V\in\mathcal D_{m-2}\), proving (6.5).  Its size is
\(\operatorname{Cat}_0+\operatorname{Cat}_1=2\).

The component representation (6.2) is unique, so all asserted
distinctness statements follow.  \(\square\)

### Theorem 6.2 -- exact native-cube certificate-breaking costs

Consider all children of the canonical factor obtained by independently
switching components of its \(\tau=(2\ 3)\) overlay.

First note that

\[
 F_m^{\rm MSW}\cap\tau F_m^{\rm MSW}=\varnothing.
 \tag{6.5a}
\]

Indeed, in every wreath some middle interval contains both coordinates
\(2,3\), or neither.  Otherwise all \(n\) middle intervals would contain
exactly one of them, whereas their total incidence with the two coordinates
is \(2m=n-1\).  Such an interval is fixed by \(\tau\).  Therefore, if a
row \(\tau E\) were also a canonical row, it would share this fixed middle
set with \(E\); exact factorization would force the two rows to be the same
wreath.  But a transposition cannot stabilize an unoriented odd cyclic
order: its induced permutation would have to be dihedral, while a
nonidentity dihedral permutation on \(n\ge9\) positions is not a single
transposition.  This proves (6.5a).

Consequently switching a component with \(s\) rows on each side replaces
exactly \(s\) canonical rows, and costs from distinct components add.

1. The minimum number of canonical rows which must be replaced in order to
   destroy every distinguished three-row set \(\mathcal T_V\) is exactly
   \[
    \boxed{2\operatorname{Cat}_{m-4}.}
    \tag{6.6}
   \]
2. The minimum number which must be replaced in order that every
   \(\mathcal T_V\) retain at most one canonical row is exactly
   \[
    \boxed{7\operatorname{Cat}_{m-4}.}
    \tag{6.7}
   \]
3. More quantitatively, every child \(F_\varepsilon\) in this component
   cube, at canonical-row distance \(d\), satisfies for every balanced
   quota system which controls depth one
   \[
    \boxed{
    \vartheta(F_\varepsilon,\beta)
    \ge
    \left(\operatorname{Cat}_{m-4}-\frac d2\right)_+.
    }
    \tag{6.7a}
   \]

#### Proof

For a fixed \(V\), the only component choices capable of removing a member
of \(\mathcal T_V\) are the two components in (6.4)--(6.5).  To destroy
the full three-set, one must switch at least one of them.  Their costs are
seven and two canonical rows, respectively.  Distinct suffixes use
distinct components, so the costs add.  Choosing every size-two component
\(\mathcal C_{0,1100V}\) attains total cost
\(2\operatorname{Cat}_{m-4}\), proving (6.6).

To leave at most one of the three distinguished rows, the two rows in
\(\mathcal C_{2,V}\) must both be removed.  Switching only the size-two
component leaves those two rows.  Hence every seven-row component
\(\mathcal C_{2,V}\) must be switched, and switching all of them attains
the sum in (6.7).

For (6.7a), call a suffix \(V\) hit when at least one of its two components
in (6.4)--(6.5) is switched.  An unhit suffix retains its full disjoint
owner triple and therefore supplies one unit to the packet dual exactly as
in Section 4.  No component hits two different suffixes, and every switched
component costs at least two canonical rows.  Thus at most \(d/2\) suffixes
are hit.  The remaining packet triples prove (6.7a).
\(\square\)

The first construction is particularly explicit.  For
\(R=1100V\), the size-two trade replaces the two canonical roots

\[
 1100R=w^{(3)}V,
 \qquad 1010R,
\]

by their \((2\ 3)\)-transposed wreaths.  In omitted-label form the four
orders have prefixes

\[
 (4,2,3,1),\quad(2,1,4,3),\quad
 (4,3,2,1),\quad(3,1,4,2)
\]

and a common tail.  The two old wreaths and two new wreaths resolve exactly
the same middle masks, so switching all suffix-indexed pairs is one genuine
exact factor, not a partial packing.

The effect on the contextual target can in fact be determined exactly.

### Lemma 6.3 -- suffix separation for the two relevant targets

Let

\[
 Q=10111101,
 \qquad Q'=11011101,
 \tag{6.8}
\]

the incidence words of \(T_0\) and \((2\ 3)T_0\), respectively.  Let
\(V\) be Dyck.  Every canonical preimage of \(QV\), or of \(Q'V\), under
the internal map \(\Gamma\) has both of its two added coordinates among
the first eight positions.  Consequently all canonical owners of these
targets are obtained by appending \(V\) to base owners in semilength four.

#### Proof

Suppose

\[
 \Gamma(x_i)=QV,
 \qquad x_i=QV\setminus\{a,b\},
\]

where \(a\) is selected by \(g(x_i)\) and \(b\) is deleted by the
preceding \(h\)-move.  The prefix \(Q\) ends at height four, and the Dyck
suffix never falls below that height.  Before \(a\), at most the other
deleted up-step can lower the height by two.  Since \(g\) selects a
down-step starting at height zero or one, \(a\) cannot lie in the suffix.

If \(b\) lies in the suffix, inspection of the up-steps of \(Q\) leaves
only \(a\in\{1,3,4\}\).  The choice \(a=1\) is impossible: coordinate one
is the first \(g\)-candidate, while it itself creates a down-step starting
at zero, so \(d_0(x_i)\ge1\) and \(g\) selects candidate number at least
two.  For \(a=3\), direct application of the \(h\)-rule to \(QV-a\)
selects coordinate five; for \(a=4\), it selects coordinate three.  In
both cases it cannot select the supposed suffix coordinate \(b\).

For \(Q'\), the same argument leaves
\(a\in\{1,2,4\}\).  Again \(a=1\) is impossible.  Applying the
\(h\)-rule to \(Q'V-a\) selects coordinate five for both \(a=2\) and
\(a=4\).  Thus \(b\) cannot lie in the suffix here either.

We have proved that \(a,b\) are both in the prefix.  The remaining
eight-letter state is balanced, and prefix locality identifies its owner
as the corresponding semilength-four owner followed by \(V\).  Hence the
whole preimage is the suffix lift of a base preimage.  More explicitly, the
MSW path of a concatenated root first traverses the complete base path with
\(V\) held fixed; after that segment, every new \(g\)-selection lies in the
suffix.  Since the present \(a\) lies in the prefix, the state is in the
first segment and is one of the base internal states listed below.
\(\square\)

For completeness, the following symbolic base table lists, for every
semilength-four Dyck root, the two-element complement of its three internal
\(\Gamma\)-colours.  Thus, for example, \(57\) denotes the set
\(\{5,7\}\).  The table follows by repeated use of (2.3)--(2.4).

\[
\begin{array}{c|ccc}
\text{root}&i=1&i=2&i=3\\ \hline
11110000&57&27&24\\
11101000&67&27&23\\
11100100&45&56&26\\
11011000&37&34&45\\
11010100&35&36&46\\
11100010&58&28&23\\
11010010&38&48&24\\
11001100&78&27&12\\
11001010&68&28&12\\
10111000&67&17&14\\
10110100&57&15&16\\
10110010&58&18&14\\
10101100&78&17&13\\
10101010&68&18&13
\end{array}
\tag{6.9}
\]

Thus \(Q\), whose complement is \(27\), has exactly the three base owners
in (2.1).  Lemma 6.3 proves

\[
 \boxed{\mu_{F_m^{\rm MSW}}(S_V)=3.}
 \tag{6.10}
\]

Now simultaneously switch every size-two component
\(\mathcal C_{0,1100V}\), and call the resulting exact factor
\(F_m^\dagger\).  The removed rows are

\[
 11001100V,\qquad10101100V.
\]

Only the first is one of the three owners in (6.10).  A transposed new row
owns \(S_V\) exactly when its old row owns \((2\ 3)S_V\), whose upper-core
word is \(Q'V\).  In table (6.9), the rows \(11001100\) and
\(10101100\) have complement triples

\[
 (78,27,12),\qquad(78,17,13),
\]

neither of which contains \(37\), the complement of \(Q'\).  Lemma 6.3
therefore rules out hidden suffix preimages.  Neither new transposed row
owns \(S_V\), and hence

\[
 \boxed{\mu_{F_m^\dagger}(S_V)=2
 \qquad(V\in\mathcal D_{m-4}).}
 \tag{6.11}
\]

There are enough upper depth-one quotas to assign quota two to every
\(S_V\): the number of such quotas is

\[
 \rho_1=W-N_1=\frac{2W}{m+2}>t>\operatorname{Cat}_{m-4}.
\]

After doing so, none of the contextual resources \((1,S_V)\) generates a
survival packet in \(F_m^\dagger\).  Thus a genuine exact factor at row
distance \(2\operatorname{Cat}_{m-4}\) completely removes the Catalan
resource family which proves (0.1).

Equations (6.6)--(6.7) characterize the native switch cost of erasing the
displayed **canonical owner certificate**.  Equations (6.10)--(6.11) show
more for the size-two construction: after a compatible quota choice, the
entire displayed resource family has no packets.  This still does not prove
that the new factor has small packet-cover value; unrelated resources may
carry old or new packets.  Thus the positive-density lower bound is
order-sharp for escaping this obstruction, while \(\mathrm{FSP}_A\) after
the escape remains open.

## 7. Exact depth-one graph gate after triple elimination

The construction above removes one explicit triple family but does not
prove that every first-shadow multiplicity is at most two.  If a rebundling
does attain that low-multiplicity regime, the remaining depth-one packet
problem has an exact graph form.

Let \(F\) be any exact factor with

\[
 \mu_1(S)\in\{0,1,2\}
 \qquad(S\in\tbinom{[n]}{m-1}).
 \tag{7.1}
\]

Put

\[
 M=|\{S:\mu_1(S)=0\}|,
 \qquad
 \rho=W-N_1=\frac{2W}{m+2}.
 \tag{7.2}
\]

For every double target \(S\), its two owners form a labelled edge \(e_S\)
on the vertex set \(F\).  Let \(G_F\) be the resulting labelled multigraph;
different targets may give parallel owner pairs.

Write \(\tau_f(G[J])\) for the ordinary fractional vertex-cover value of
the labelled edge subfamily \(J\).  Also let \(i_G(B)\) be the number of
labelled edges of \(G_F\) incident with a vertex set \(B\subseteq F\).

### Theorem 7.1 -- exact low-multiplicity graph reduction

The number of labelled edges of \(G_F\) is exactly

\[
 |E(G_F)|=\rho+M.
 \tag{7.3}
\]

If \(\vartheta_1^*(F)\) denotes packet-cover mass minimized over all
balanced depth-one quotas, and \(\tau_1^*(F)\) is the corresponding minimum
integral exceptional-family size, then

\[
 \boxed{
 \vartheta_1^*(F)
 =min_{\substack{J\subseteq E(G_F)\\|J|=M}}
       \tau_f(G_F[J]),
 }
 \tag{7.4}
\]

and

\[
 \boxed{
 \tau_1^*(F)
 =\min\{|B|:B\subseteq F,\ i_G(B)\ge M\}.
 }
 \tag{7.5}
\]

Equivalently,

\[
 \boxed{
 \vartheta_1^*(F)
 =\min\left\{
 \sum_{E\in F}x_E:
 0\le x_E\le1,\
 \#\{S:\mu_1(S)=2,\ x_{E_1(S)}+x_{E_2(S)}\ge1\}
 \ge M
 \right\}.
 }
 \tag{7.6}
\]

Finally,

\[
 \boxed{
 \frac Mn\le\vartheta_1^*(F)
 \le\tau_1^*(F)
 \le\min\{M,t\}.
 }
 \tag{7.7}
\]

The fractional upper bound can separately be sharpened to
\(\vartheta_1^*(F)\le t/2\).

#### Proof

Let \(n_j=|\{S:\mu_1(S)=j\}|\).  From total target count and total slot
count,

\[
 n_0+n_1+n_2=N_1,
 \qquad n_1+2n_2=W.
\]

Subtracting gives

\[
 n_2-n_0=W-N_1=\rho,
\]

which is (7.3).

A balanced depth-one quota has value two on exactly \(\rho\) targets and
one elsewhere.  A target of load zero or one generates no packet under
either quota.  A double target generates its unique two-owner packet
exactly when it receives quota one.  In an optimal quota choice, every
upper quota may therefore be placed on a double target: moving an upper
quota from a zero or singleton target to a low-quota double target removes
one constraint and creates none.  Since there are \(\rho+M\) double
targets, exactly \(M\) labelled edge constraints remain, and every choice
of \(M\) residual edges is attainable.  This proves (7.4).

For the integral statement, a row set \(B\) covers some attainable
\(M\)-edge residual system exactly when at least \(M\) labelled edges of
the original graph are incident with \(B\).  Choose those edges as the
residual low-quota targets and give upper quotas to the remaining
\(\rho\) double targets.  Conversely, every cover of an attainable
residual system is incident with its \(M\) labelled edges.  This proves
(7.5).

Formula (7.6) says the same thing fractionally: a weight vector is feasible
for some \(M\)-edge residual graph if and only if at least \(M\) original
edge labels satisfy their vertex-cover inequality.

For the lower bound, fix any residual \(J\) of size \(M\).  One wreath owns
exactly \(n\) depth-one targets, so the labelled maximum degree of
\(G_F[J]\) is at most \(n\).  Summing its \(M\) edge inequalities gives

\[
 M\le\sum_{E\in F}\deg_J(E)x_E
 \le n\sum_{E\in F}x_E.
\]

Thus every residual fractional cover has mass at least \(M/n\).  Choosing
one endpoint from every residual labelled edge gives an integral cover of
size at most \(M\); choosing all \(t\) rows is the other displayed trivial
bound.  Finally \(x_E=1/2\) for every row covers every graph edge and has
mass \(t/2\).  \(\square\)

### Consequence 7.2 -- the precise post-triple target

In the regime (7.1), the depth-one part of \(\mathrm{FSP}_A\) is exactly
the assertion that the double-colour multigraph contains a selectable
\(M\)-edge subgraph with fractional vertex-cover mass

\[
 o(t/\sqrt m).
 \tag{7.8}
\]

Equivalently, the integral hard-quota version asks for a set of
\(o(t/\sqrt m)\) wreaths incident with at least \(M\) double-colour labels.
The universal lower bound in (7.7) shows that this is impossible unless

\[
 M=o(W/\sqrt m).
 \tag{7.9}
\]

Conversely, the stronger condition \(M=o(t/\sqrt m)\) is sufficient by
the upper bound in (7.7).  The gap between these two scales is exactly a
question of how strongly the extra double colours can be concentrated on a
small wreath family.

This graph theorem identifies the next positive construction problem after
triple collisions have been removed.  It is not solved by the contextual
switch in Section 6.

## 8. Adversarial self-audit

1. **The three base rows are symbolic.**  The permutations in (2.2) follow
   from the recursive identity (2.3).  The three equal colours in (2.5)
   are then obtained by two displayed set exchanges and (2.4).  No finite
   enumeration is being imported.
2. **The suffix really remains inert.**  Every prefix state in the first
   two complete moves is balanced on the first eight coordinates.  The
   appended word is Dyck.  Lemma 3.1 therefore applies at every required
   step, including the \(g\)-selection of \(a_2\).
3. **The suspended target has the right rank.**  The word \(T_0\) has six
   up-steps and \(V\) has \(m-4\), so \(T_0V\) has \(m+2\) up-steps.
   Its complement in the \(2m\)-core has \(m-2\) elements; adjoining
   \(\infty\) gives a lower target of rank \(m-1\).
4. **Different suffixes do not share distinguished owners.**  Each owner
   root has a unique decomposition into its first eight letters and its
   suffix.  The three base prefixes are distinct, and the canonical factor
   has one wreath per Dyck root.
5. **Extra target owners are harmless.**  A survival packet is any
   \((\beta+1)\)-subset of the full owner set.  The selected two or three
   distinguished owners remain a valid packet even if \(S_V\) has further
   owners.
6. **The quota choice is genuinely arbitrary.**  At depth one the only
   balanced values are one and two.  The proof selects a two-packet in the
   first case and a three-packet in the second; it does not assume which
   targets receive the upper quota.
7. **The cut-dual direction is correct.**  Inequality (1.2) bounds the
   forced mass inside a cut by the selected packet's actual intersection
   with that cut.  Pairwise disjoint packets therefore pay every cut with
   unit wreath capacity.
8. **Trade robustness uses only shared rows.**  If one canonical row from a
   triple is removed, the proof discards that entire triple.  Thus one
   removed row destroys at most one certificate, and no assumption is made
   about the newly inserted rows or the legality of an individual local
   trade.
9. **The result is scoped to the canonical basin.**  It rules out the
   canonical factor and every \(o(t)\)-edit perturbation.  It gives no lower
   bound for factors at positive-density distance, and therefore does not
   disprove \(\mathrm{FSP}_A\) itself.

10. **The native-cube destruction theorem concerns distinguished owners.**
   It computes exactly when the old sets \(\mathcal T_V\) cease to survive,
   not the full new multiplicity of \(S_V\).  No conclusion about the packet
   LP of the switched factor is inferred.
11. **Component costs add.**  The exact hierarchy partitions all canonical
   rows, and the suffix labels in (6.4)--(6.5) are unique.  Therefore a
   component used for one suffix cannot pay for a different suffix in this
   fixed \((2\ 3)\)-cube.
11a. **The strengthened native-cube bound uses component size.**  The
   general edit estimate (5.1) charges one destroyed packet per removed
   canonical row.  Inside the native cube, a nontrivial component replaces
   at least two rows and no relevant component hits two suffix groups,
   yielding the sharper factor \(d/2\) in (6.7a).
12. **Suffix separation checks the preceding \(h\)-move.**  Once the
   inserted coordinate \(a\) is confined to the prefix, the possible
   suffix coordinate \(b\) is excluded by applying \(h\) to the uniquely
   determined word \(QV-a\) or \(Q'V-a\).  Merely noting that the suffix
   begins high would not by itself exclude \(b\).
13. **The switched factor is not declared packet-free.**  Equation (6.11)
   removes exactly the contextual triple resources after assigning them
   upper quotas.  No estimate for the other \(N_1-\operatorname{Cat}_{m-4}\)
   depth-one resources, or for deeper ranks, is inferred.
14. **Parallel graph edges stay labelled.**  In Section 7 two different
   targets may have the same owner pair.  They remain separate quota labels
   and count separately in \(|J|\), degrees, and \(i_G(B)\).  Repeated
   vertex-cover inequalities are harmless but their quota slots are not
   identified.
15. **Upper quotas may be moved onto doubles.**  Under (7.1), zero and
   singleton targets have no packet for either quota value.  Exchanging an
   upper quota from such a target with a low-quota double only deletes a
   packet constraint.  Hence an optimum with all \(\rho\) upper quotas on
   doubles always exists.
16. **The graph theorem is conditional on maximum load two.**  A target of
   load at least three gives a complete graph or three-uniform packet
   system, not one labelled edge.  Section 7 is deliberately the exact
   post-triple gate, not a formula for arbitrary factors.

## 9. Exact status

### Proved

1. A general bounded-congestion certificate in the compressed packet cut
   dual.
2. An explicit three-owner semilength-four MSW collision.
3. Independent Dyck-suffix suspension of that collision over all
   \(\operatorname{Cat}_{m-4}\) suffixes.
4. The canonical lower bound
   \[
   \vartheta_A(F_m^{\rm MSW})\ge\operatorname{Cat}_{m-4}=\Omega(t).
   \]
5. The robust edit-distance lower bound (5.1).
6. A positive-density exact-factor trade barrier for every attempted proof
   of \(\mathrm{FSP}_A\) starting from the canonical MSW factor.
7. The exact costs \(2\operatorname{Cat}_{m-4}\) and
   \(7\operatorname{Cat}_{m-4}\) for destroying, respectively, the old
   three-owner certificates and all their old pair subpackets inside the
   native \((2\ 3)\)-component cube.
7a. The factor-wide native-cube lower bound
   \[
   \vartheta(F_\varepsilon,\beta)
   \ge(\operatorname{Cat}_{m-4}-d/2)_+,
   \]
   which forces distance \(2\operatorname{Cat}_{m-4}-o(t/\sqrt m)\)
   for every \(\mathrm{FSP}_A\) child in that cube.
8. Exact suffix separation for the contextual target and its transposed
   companion, proving that the target has multiplicity exactly three before
   the size-two switch and exactly two afterward.
9. A concrete exact factor at distance \(2\operatorname{Cat}_{m-4}\) and
   a balanced quota choice for which the entire displayed Catalan resource
   family generates no packets.
10. The exact depth-one graph characterization (7.4)--(7.6) whenever all
    first-shadow loads are at most two, together with the sharp universal
    scale bounds (7.7).

### Still open

Construct a positive-density re-bundled exact factor with
\(o_A(t/\sqrt m)\) packet-cover mass, or prove a factor-independent packet
packing obstruction.  The present theorem shows that the canonical factor
cannot be the nearly-correct starting state for that task.
