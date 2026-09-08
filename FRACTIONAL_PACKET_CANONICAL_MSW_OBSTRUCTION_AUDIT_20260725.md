# Independent audit: Catalan packet obstruction for the canonical MSW factor

Date: 2026-07-25

Audited source: `FRACTIONAL_PACKET_CANONICAL_MSW_OBSTRUCTION_20260725.md`.

Method: pure symbolic mathematics.  No web search, finite enumeration,
random experiment, solver, or computer algebra is used.

## 0. Verdict

\[
\boxed{\text{PASS}}
\]

The canonical lower bound, its Catalan density, and the edit-distance
robustness theorem are correct.  In particular, the three displayed MSW
flip permutations and their common second-upper colour check exactly; the
colour-to-lower-target complement map has the right orientation and rank;
Dyck-suffix suspension preserves the required three owners; arbitrary
balanced depth-one quotas produce packets of the required size; and deleting
one canonical wreath destroys at most one member of the disjoint certificate
family.

No mathematical correction or failed claim was found.  There is only one
minor formal convention worth making explicit: the congestion parameter
\(D\) in Lemma 1.1 is positive (as is already forced by the use of \(1/D\)).
Every application in the source has \(D=1\).

## 1. Claim-by-claim status

| Source claim | Status | Audit conclusion |
|---|---:|---|
| Lemma 1.1, bounded-congestion packet packing | PASS | The packet dual and compressed-cut proof have the correct direction and normalization. |
| Equations (2.2), the three flip permutations | PASS | All three follow symbolically from the displayed MSW recursion. |
| Equations (2.4)--(2.6), the three-owner collision | PASS | The two complete moves and the next \(g\)-coordinate give the same six-set \(T_0\) in all three rows. |
| Lemma 3.1 and suffix suspension | PASS | A Dyck suffix introduces no relevant \(g\)- or \(h\)-candidate, and the concatenation identity gives the same conclusion directly. |
| Equations (3.5)--(3.7), target map and disjoint triples | PASS | Complementation gives a rank-\(m-1\) lower interval containing \(\infty\); different suffixes give different targets and disjoint distinguished owners. |
| Section 4, arbitrary balanced quota and packet choice | PASS | At depth one every quota is exactly \(1\) or \(2\), so the owner triple always contains a packet of size \(\beta+1\). |
| Equation (4.2), Catalan ratio | PASS | The exact rational expression and limit \(1/256\) are correct. |
| Section 5, edit-distance robustness | PASS | A deleted canonical wreath meets at most one disjoint triple; retaining all three owners is sufficient independently of inserted wreaths. |
| Corollary 5.1 and trade barrier | PASS | The asymptotic subtraction and the conditional \(t/s\) trade count are correct. |

There are no entries with status **CORRECT** (true only after a substantive
repair) and no entries with status **FAIL**.

## 2. Packet-packing lemma and cut direction

For a selected packet \(P_a\subseteq\mathcal O_a\) of size \(k_a\) and a
cut \(Z\subseteq F\),

\[
 |P_a\setminus Z|\le |\mathcal O_a\setminus Z|.
\]

Therefore

\[
 k_a-|\mathcal O_a\setminus Z|
 \le k_a-|P_a\setminus Z|
 =|P_a\cap Z|.
\]

The right side is nonnegative, so taking the positive part on the left
preserves the inequality:

\[
 \bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
 \le |P_a\cap Z|.
\]

If every wreath belongs to at most \(D\) selected packets, summing with
weight \(1/D\) gives

\[
 \sum_a\frac1D
 \bigl(k_a-|\mathcal O_a\setminus Z|\bigr)_+
 \le \frac1D\sum_a|P_a\cap Z|
 \le |Z|.
\]

Thus the proposed compressed-dual vector pays every cut.  Equivalently,
putting packet-dual weight \(1/D\) on every selected packet gives wreath
congestion at most one.  The lower bound is therefore \(|\mathcal A|/D\),
with no reversed inequality and no missing factor of \(k_a\).

## 3. Symbolic recomputation of the flip permutations

Write \(\mu\) for reverse-complement.  The recursion is

\[
 \pi(1u0v)=
 \bigl(|u|+2,\ |u|+2-\pi(\mu u),\ 1,\ |u|+2+\pi(v)\bigr).
\]

The basic identities are

\[
 \pi(10)=(2,1),
\]

\[
 \pi(1100)
 =(4,4-(2,1),1)
 =(4,2,3,1),
\]

and, using concatenation,

\[
 \pi(1010)=(2,1,4,3).
\]

All relevant inner Dyck words below are fixed by \(\mu\).  First,

\[
 \pi(111000)
 =(6,6-\pi(1100),1)
 =(6,2,4,3,5,1),
\]

so

\[
\begin{aligned}
 \pi(11110000)
 &=(8,8-\pi(111000),1)\\
 &=(8,2,6,4,5,3,7,1).
\end{aligned}
\]

For the second row it is important to use the primitive decomposition

\[
 110100=1(1010)0,
\]

not a nonexistent decomposition after its fourth letter.  Hence

\[
 \pi(110100)
 =(6,6-\pi(1010),1)
 =(6,4,5,2,3,1),
\]

and consequently

\[
\begin{aligned}
 \pi(11101000)
 &=(8,8-\pi(110100),1)\\
 &=(8,2,4,3,6,5,7,1).
\end{aligned}
\]

Finally \(11001100=(1100)(1100)\), so the concatenation identity gives

\[
\begin{aligned}
 \pi(11001100)
 &=\pi(1100)\mathbin\Vert(4+\pi(1100))\\
 &=(4,2,3,1,8,6,7,5).
\end{aligned}
\]

Thus all three permutations in source (2.2), including their orientation,
are exact.

## 4. Symbolic recomputation of the common colour

At the second internal state, the first two ordered exchange pairs and the
next inserted coordinate are as follows:

\[
\begin{array}{c|c|c|c}
w&x_0&(a_0,b_0),(a_1,b_1)&a_2\\ \hline
11110000&\{1,2,3,4\}&(8,2),(6,4)&5\\
11101000&\{1,2,3,5\}&(8,2),(4,3)&6\\
11001100&\{1,2,5,6\}&(4,2),(3,1)&8
\end{array}
\]

Performing the two exchanges gives

\[
\begin{aligned}
 \{1,2,3,4\}&\longmapsto\{1,3,4,8\}
                    \longmapsto\{1,3,6,8\},\\
 \{1,2,3,5\}&\longmapsto\{1,3,5,8\}
                    \longmapsto\{1,4,5,8\},\\
 \{1,2,5,6\}&\longmapsto\{1,4,5,6\}
                    \longmapsto\{3,4,5,6\}.
\end{aligned}
\]

Since

\[
 y_{1}=x_2\cup\{b_1\},\qquad
 y_2=x_2\cup\{a_2\},
\]

one has

\[
 \Gamma(x_2)=y_1\cup y_2=x_2\cup\{a_2,b_1\}.
\]

The three values are respectively

\[
\begin{aligned}
 \{1,3,6,8\}\cup\{5,4\},\\
 \{1,4,5,8\}\cup\{6,3\},\\
 \{3,4,5,6\}\cup\{8,1\},
\end{aligned}
\]

and all equal

\[
 T_0=\{1,3,4,5,6,8\}.
\]

This is a literal collision of three different canonical columns, not a
collision caused by reversing an omitted-label cycle or identifying two
slots in one wreath.

## 5. Orientation and the lower-target complement map

In the odd MSW cycle, the core upper states are \(y_i\), while the
corresponding middle vertices containing the new coordinate are

\[
 \widetilde y_i=([2m]\setminus y_i)\cup\{\infty\}.
\]

The two such middle vertices adjacent through the internal core state
\(x_i\) are \(\widetilde y_{i-1}\) and \(\widetilde y_i\).  Their
rank-\((m-1)\) intersection is

\[
\begin{aligned}
 \widetilde y_{i-1}\cap\widetilde y_i
 &=\{\infty\}\cup
   \bigl([2m]\setminus(y_{i-1}\cup y_i)\bigr)\\
 &=\{\infty\}\cup([2m]\setminus\Gamma(x_i)).
\end{aligned}
\]

This proves the source's map

\[
 S(T)=\{\infty\}\cup([2m]\setminus T)
\]

without choosing an orientation of the cyclic omitted-label word.  If
\(|T|=m+2\), then its core complement has size \(m-2\), and adjoining
\(\infty\) gives size \(m-1\), exactly lower depth one.  There is no
rank shift or complement reversal.

## 6. Dyck-suffix suspension

Let \(V\) be Dyck of semilength \(m-4\).  Each base word \(w^{(j)}\)
ends at height zero, so \(w^{(j)}V\) is Dyck of semilength \(m\).

The source's locality proof is correct.  For a balanced prefix state \(P\),
the appended Dyck suffix starts at height zero and has no down-step starting
at height zero.  It therefore does not change the statistic \(d_0\) used
by \(g\).  If \(g\)'s selected candidate lies in \(P\), every suffix
candidate comes later, so the same coordinate is selected in \(PV\).
After that down-to-up flip, the suffix begins at height two.  Every suffix
up-step starts at height at least two, so none enters the height-zero/one
candidate list used by \(h\).  A prefix \(h\)-selection is likewise
unchanged.

There is also a direct consistency check from the recursion:

\[
 \pi(PV)=\pi(P)\mathbin\Vert(|P|+\pi(V))
\]

for Dyck \(P,V\).  Hence all eight prefix coordinates are flipped, in the
same order as in the base column, before any suffix coordinate.  In
particular, the first two complete moves and the next \(g\)-move give

\[
 x_2(w^{(j)}V)=x_2(w^{(j)})V,
 \qquad
 \Gamma(x_2(w^{(j)}V))=T_0V.
\]

The word \(T_0V\) has \(6+(m-4)=m+2\) up-steps, so its associated lower
target has the required rank.

## 7. Distinct targets and disjoint owner triples

If \(V\ne V'\), then \(T_0V\ne T_0V'\); complementation is injective, so
\(S_V\ne S_{V'}\).  Also every root in the displayed family has a unique
decomposition into its first eight letters and its remaining suffix.  Thus

\[
 w^{(j)}V=w^{(j')}V'
 \quad\Longrightarrow\quad j=j'\text{ and }V=V'.
\]

The canonical MSW factor has one distinct wreath for each Dyck root.  One
can also see why no hidden cyclic-order identification is possible: two
equal wreaths would have the same middle intervals, whereas distinct MSW
cycles are vertex-disjoint in the exact factor.  Therefore the triples

\[
 \mathcal T_V=
 \{E(w^{(1)}V),E(w^{(2)}V),E(w^{(3)}V)\}
\]

are pairwise disjoint.  Their number is exactly the number of Dyck suffixes,
\(\operatorname{Cat}_{m-4}\).

## 8. Arbitrary balanced depth-one quotas

At depth one,

\[
 \lambda_1=
 \frac{\binom{2m+1}{m}}{\binom{2m+1}{m-1}}
 =\frac{m+2}{m}.
\]

For \(m\ge4\), this lies strictly between one and two.  Hence
\(c_1=1\), and every balanced quota value is either

\[
 \beta_1(S)=1\quad\text{or}\quad\beta_1(S)=2.
\]

No assumption about which targets receive the upper value is used.  The
three distinguished owners of \(S_V\) supply a two-element packet when
\(\beta_1(S_V)=1\) and the whole three-element packet when
\(\beta_1(S_V)=2\).  In either case the selected size is exactly
\(\beta_1(S_V)+1\).  Extra owners of the same target do not invalidate a
subset packet.

Since the distinguished triples are disjoint, these selected packets have
congestion one.  Lemma 1.1 yields

\[
 \vartheta(F_m^{\rm MSW},\beta)
 \ge \operatorname{Cat}_{m-4}
\]

for every quota system containing depth one.  Adding other depths adds
constraints to the primal packet cover, so it cannot decrease its optimum.

## 9. Exact Catalan ratio

Direct cancellation gives

\[
\begin{aligned}
 \frac{\operatorname{Cat}_{m-4}}{\operatorname{Cat}_m}
 &=\frac{m+1}{m-3}
   \frac{\bigl(m(m-1)(m-2)(m-3)\bigr)^2}
   {(2m)(2m-1)\cdots(2m-7)}\\
 &=\frac{(m-2)(m-1)m(m+1)}
 {16(2m-7)(2m-5)(2m-3)(2m-1)}.
\end{aligned}
\]

The leading-term ratio is

\[
 \frac{m^4}{16(2m)^4}=\frac1{256},
\]

and expansion of the rational function gives an error \(O(m^{-1})\).
Since \(t=\operatorname{Cat}_m\),

\[
 \frac{\vartheta(F_m^{\rm MSW},\beta)}{t/\sqrt m}
 \ge\left(\frac1{256}+O(m^{-1})\right)\sqrt m,
\]

which diverges.  The claimed order-\(\sqrt m\) separation from the
\(o_A(t/\sqrt m)\) target is correct.

## 10. Edit-distance robustness and exact factor counting

Every exact factor contains exactly \(t\) wreaths.  Therefore, for two exact
factors,

\[
 |F_m^{\rm MSW}\setminus F|=|F\setminus F_m^{\rm MSW}|;
\]

the source's distance is the number of replacements, equivalently half the
symmetric-difference size.

Let this number be \(d\).  Because the \(\mathcal T_V\) are pairwise
disjoint, one removed canonical wreath meets at most one triple.  Thus at
least

\[
 \bigl(\operatorname{Cat}_{m-4}-d\bigr)_+
\]

triples remain intact.  Each intact triple still consists of three owners of
the same target in \(F\).  Inserted wreaths can add owners but cannot remove
those incidences.  Selecting the quota-dependent two- or three-packet from
each intact triple again produces disjoint packets, proving

\[
 \vartheta(F,\beta)
 \ge
 \bigl(\operatorname{Cat}_{m-4}-d(F,F_m^{\rm MSW})\bigr)_+.
\]

If \(\vartheta_A(F_m)=o_A(t/\sqrt m)\), rearrangement gives

\[
 d(F_m,F_m^{\rm MSW})
 \ge \operatorname{Cat}_{m-4}-o_A(t/\sqrt m)
 =\left(\frac1{256}-o(1)\right)t.
\]

This argument deliberately discards a triple after even one of its owners
is removed.  It therefore makes no unsupported assumption about the new
wreaths or about the shape of individual exact-factor trades.  If each
effective trade removes at most \(s\) previously untouched canonical
wreaths, the number of such trades is at least the required replacement
count divided by \(s\), exactly as claimed.

## 11. Final scope audit

The proof establishes a positive-density obstruction only around the
canonical MSW factor.  It does not show that every exact factor has a
similar packet packing and does not disprove \(\mathrm{FSP}_A\).  Its
logical conclusion is exactly the stated one: any factor meeting
\(\mathrm{FSP}_A\) must lie at positive-density replacement distance from
the canonical factor.  The source's final open-problem statement respects
that scope.

## 12. Addendum audit: exact native \((2\ 3)\)-cube costs

This section audits the subsequently added source Section 6.

### 12.1 Verdict on the extension

\[
\boxed{\text{CORRECT AT FIRST AUDIT; PASS AFTER SOURCE PATCH}}
\]

The component locations and the exact costs

\[
 2\operatorname{Cat}_{m-4}
 \quad\text{and}\quad
 7\operatorname{Cat}_{m-4}
\]

are mathematically correct.  At the time of the first extension audit, the
proof omitted a necessary justification when it identified component size
with the number of canonical rows replaced.  The source now includes the
needed disjointness statement \(F_m^{\rm MSW}\cap\tau F_m^{\rm MSW}
=\varnothing\) and its proof.  The argument independently derived in Section
12.3 below agrees with that patch, so Theorems 6.1 and 6.2 now pass as written.

### 12.2 Component indices and uniqueness

The active-atom hierarchy gives each Dyck root a unique expression

\[
 x=AR,
 \qquad A\in\mathcal A_j,\qquad R\in\mathcal D_{m-j-2},
\]

where \(A\) is the shortest Dyck prefix of length at least four.  For the
first two distinguished roots,

\[
\begin{aligned}
 11110000&=1(111000)0,\\
 11101000&=1(110100)0.
\end{aligned}
\]

Both inner words lie in \(\mathcal D_3\), and both eight-letter words are
primitive.  Their active atom is therefore the whole eight-letter prefix,
so, after appending \(V\),

\[
 E(w^{(1)}V),E(w^{(2)}V)\in\mathcal C_{2,V}.
\]

The component has

\[
 |\mathcal C_{2,V}|
 =|\mathcal A_2|
 =\operatorname{Cat}_3+\operatorname{Cat}_2
 =5+2=7.
\]

For the third root,

\[
 w^{(3)}V=1100\,(1100V).
\]

The shortest Dyck prefix of length at least four is \(1100\), and

\[
 \mathcal A_0=\{1100,1010\}.
\]

Since \(1100V\in\mathcal D_{m-2}\), this gives

\[
 E(w^{(3)}V)\in\mathcal C_{0,1100V},
 \qquad |\mathcal C_{0,1100V}|=2.
\]

The unique active-atom factorization proves all needed distinctness:

* \(\mathcal C_{2,V}=\mathcal C_{2,V'}\) forces \(V=V'\);
* \(\mathcal C_{0,1100V}=\mathcal C_{0,1100V'}\) forces \(V=V'\);
* a \(j=2\) component cannot equal a \(j=0\) component.

Thus no single native component is being charged to two different suffix
certificates.

### 12.3 Why component size equals canonical-row edit cost here

Let \(F=F_m^{\rm MSW}\) and \(\tau=(2\ 3)\).  In fact the following
stronger statement holds:

\[
 \boxed{F\cap\tau F=\varnothing.}
\]

To prove it, let \(C\) be any wreath, viewed as an unoriented cyclic order
on \(n=2m+1\) labels.  Across its \(n\) cyclic intervals of length \(m\),
each of the labels \(2,3\) occurs exactly \(m\) times.  Their total incidence
is therefore

\[
 2m=n-1.
\]

If every middle interval contained exactly one of \(2,3\), that total would
instead be \(n\).  Hence some middle interval \(M\) contains both labels or
neither, and consequently

\[
 \tau M=M.
\]

Suppose \(\tau C=D\) for two wreaths \(C,D\in F\).  Then \(M\) is a middle
interval of both \(C\) and \(D\).  Exactness of \(F\) forces \(C=D\).
But a single transposition cannot stabilize an unoriented cyclic order of
odd length: a nonidentity rotation fixes no labels, while an odd reflection
has cycle type \(1\,2^m\); neither has the cycle type of \((2\ 3)\), namely
one transposition and \(n-2\) fixed labels.  Thus \(C=D\) is also impossible,
proving the displayed disjointness.

Now let \(L\subseteq F\) be any union of left sides of overlay components.
Switching precisely those components gives

\[
 F_L=(F\setminus L)\cup\tau L.
\]

Because \(\tau L\subseteq\tau F\) and \(F\cap\tau F=\varnothing\),

\[
 F\setminus F_L=L,
 \qquad F_L\setminus F=\tau L.
\]

Therefore

\[
 d(F_L,F)=|L|,
\]

and edit costs of distinct switched components add exactly.  This is the
missing step needed to interpret the sizes two and seven as numbers of
canonical rows replaced, rather than merely as bipartite component
cardinalities.

### 12.4 Exact destruction cost for every full triple

For fixed \(V\), the three distinguished canonical rows lie in exactly two
left components:

\[
 \{E(w^{(1)}V),E(w^{(2)}V)\}\subseteq\mathcal C_{2,V},
 \qquad
 E(w^{(3)}V)\in\mathcal C_{0,1100V}.
\]

A canonical row remains present if and only if its own left component is not
switched; Section 12.3 also rules out its accidental reintroduction from a
right side.  Thus breaking the full triple requires switching at least one
of these two components.  Their exact edit costs are seven and two.  The
minimum local cost is therefore two, attained by switching
\(\mathcal C_{0,1100V}\).

The relevant size-two components are distinct as \(V\) varies, so the local
lower bounds add.  Switching all of them replaces exactly

\[
 2|\mathcal D_{m-4}|=2\operatorname{Cat}_{m-4}
\]

canonical rows and removes every \(E(w^{(3)}V)\).  Hence source (6.6) is
exact.

### 12.5 Leaving at most one distinguished owner

Switching the size-two component removes only \(E(w^{(3)}V)\) from the
distinguished triple and leaves the other two canonical rows.  Therefore it
cannot by itself leave at most one distinguished owner.

Both remaining rows lie on the left side of the single component
\(\mathcal C_{2,V}\).  A component switch is all-or-nothing, so switching
\(\mathcal C_{2,V}\) removes both

\[
 E(w^{(1)}V)\quad\text{and}\quad E(w^{(2)}V).
\]

Neither can reappear on its right side by Section 12.3.  Conversely, if this
seven-row component is not switched, both rows remain, regardless of every
other component choice.  Thus every feasible cube vertex must switch
\(\mathcal C_{2,V}\) for every \(V\).

These seven-row components are distinct, so their exact edit costs add to

\[
 7|\mathcal D_{m-4}|=7\operatorname{Cat}_{m-4}.
\]

Switching all of them attains the bound and leaves the third distinguished
canonical owner in each triple.  Switching the corresponding size-two
components as well would cost more and is unnecessary.  Source (6.7) is
therefore exact.

### 12.6 Scope of the cube-cost conclusion

The costs concern removal of the displayed **canonical distinguished
owners**, not removal of all owners of \(S_V\) in the switched factor.
Right-side transposed wreaths or other retained wreaths may still own
\(S_V\).  The source states this limitation explicitly, so it does not infer
a small packet-cover value from the native switches.  The claim of
order-sharpness is valid only for escaping this particular canonical
certificate, which is the scope actually stated.

## 13. Addendum audit: exact multiplicity, transposed owners, and cube bound

This section audits the later Lemma 6.3, table (6.9), equations
(6.10)--(6.11), the compatible quota choice, and quantitative bound (6.7a).

### 13.1 Verdict

\[
\boxed{\text{PASS}}
\]

The suffix-separation lemma is correct for both

\[
 Q=10111101,
 \qquad Q'=11011101.
\]

The base complement table is correct, \(QV\) has exactly three canonical
internal \(\Gamma\)-preimages, the simultaneous size-two switches remove
exactly one of them and add none, and the resulting multiplicity is exactly
two.  There are enough quota-two assignments to eliminate every displayed
resource.  The native-cube inequality

\[
 \vartheta(F_\varepsilon,\beta)
 \ge
 \left(\operatorname{Cat}_{m-4}-\frac d2\right)_+
\]

is also correct under the standing hypothesis that the controlled quota
system contains depth one.  For a standalone statement, source (6.7a)
should repeat that qualifier; without a controlled depth-one resource the
packet certificates used in its proof would not be constraints of the LP.

Two residual display slips do not affect the mathematics: the current source
rendering of (6.3) has `operatorname{Cat}` instead of
`\operatorname{Cat}`, and (6.11) has `mu` instead of `\mu`.

### 13.2 Height audit: the inserted coordinate cannot enter the suffix

Both \(Q\) and \(Q'\) have six up-steps and therefore end at height four.
After appending a Dyck word \(V\), every position in the suffix starts at
height at least four in the target word.

If

\[
 \Gamma(x_i)=QV,
 \qquad x_i=QV\setminus\{a,b\},
\]

then \(a\) is the down-step selected by \(g(x_i)\).  Before coordinate
\(a\), deletion of the other added coordinate \(b\) lowers the target
height by at most two.  Thus, if \(a\) were in the suffix, its starting
height in \(x_i\) would be at least two.  The map \(g\) selects only a
down-step starting at height zero or one, a contradiction.  This argument
applies verbatim to \(Q'V\).

Now suppose \(b\) is in the suffix.  Then \(a<b\), so deletion of \(b\)
does not affect the starting height at \(a\).  The heights immediately before
the up-steps of \(Q\) show that the only candidates are

\[
 a\in\{1,3,4\};
\]

for \(Q'\), they are

\[
 a\in\{1,2,4\}.
\]

In either word, \(a=1\) is impossible.  Turning its first up-step down makes
coordinate one the first \(g\)-candidate and also creates a down-step from
height zero.  Hence \(d_0(x_i)\ge1\), while \(g\) selects candidate number
\(d_0(x_i)+1\ge2\).

### 13.3 Direct recomputation of the four \(h\)-cases

For an upper word \(y\), let \(u_1(y)\) be the number of up-steps starting
at height one.  The MSW map \(h\) flips the \(u_1(y)\)-th up-step, in
left-to-right order, among the up-steps starting at height zero or one.

The input to \(h\) is

\[
 y_{i-1}=QV\setminus\{a\}
 \quad\text{or}\quad
 y_{i-1}=Q'V\setminus\{a\}.
\]

After deletion of \(a\), the eight-letter prefix ends at height two, so no
up-step in the Dyck suffix begins at height zero or one.  The choice of
\(h\) is therefore determined entirely by the displayed prefix.  The four
nontrivial cases are

\[
\begin{array}{c|c|c|c|c}
\text{target}&a&\text{prefix of }y_{i-1}&u_1&h\text{-coordinate}\\ \hline
Q&3&10011101&2&5\\
Q&4&10101101&2&3\\
Q'&2&10011101&2&5\\
Q'&4&11001101&3&5
\end{array}
\]

For example, in \(10011101\) the candidate up-steps occur at coordinates
\(1,5,6,8\), while the height-one up-steps are \(6,8\).  Thus \(u_1=2\)
and \(h\) selects the second candidate, coordinate five.  In
\(10101101\), the candidates begin \(1,3,5,6,8\), the height-one up-steps
are \(6,8\), and the second candidate is coordinate three.  In
\(11001101\), the height-one up-steps are \(2,6,8\), and the third
candidate is coordinate five.  Every selected coordinate is in the first
eight positions, contradicting the assumption that \(b\) lies in the
suffix.

Thus both added coordinates \(a,b\) lie in the first eight positions for
both targets.

### 13.4 From prefix coordinates to a suffix-lifted owner

Deleting \(a,b\) from either eight-letter target prefix leaves a balanced
eight-letter state \(P\), and the full state is \(PV\).  Let \(u\) be the
unique semilength-four Dyck root whose MSW path contains \(P\).  The
concatenation identity

\[
 \pi(uV)=\pi(u)\mathbin\Vert(8+\pi(V))
\]

shows that the path rooted at \(uV\) contains \(PV\).  Since the canonical
MSW paths partition the balanced words, this is the unique global owner
root of \(PV\).  Therefore every preimage of \(QV\) or \(Q'V\) is obtained
by appending the same suffix \(V\) to a base preimage.  This also rules out
cross-suffix preimages with some \(V'\ne V\).

### 13.5 Independent check of the base complement table

Let a semilength-four root have initial one-set \(X\), zero-set
\(Z=[8]\setminus X\), and flip order

\[
 (a_0,b_0,a_1,b_1,a_2,b_2,a_3,b_3).
\]

The complements of its three internal colours admit the following compact
formula:

\[
\begin{aligned}
 [8]\setminus\Gamma(x_1)
   &=Z\setminus\{a_0,a_1\},\\
 [8]\setminus\Gamma(x_2)
   &=\{b_0\}\cup\bigl(Z\setminus\{a_0,a_1,a_2\}\bigr),\\
 [8]\setminus\Gamma(x_3)
   &=\{b_0,b_1\}.
\end{aligned}
\]

Indeed, after \(i\) complete moves, \(x_i\) is obtained from \(X\) by
inserting \(a_0,\ldots,a_{i-1}\) and deleting
\(b_0,\ldots,b_{i-1}\), while \(\Gamma(x_i)\) restores
\(b_{i-1}\) and inserts \(a_i\).

Applying the recursive flip formula and this identity to the fourteen Dyck
roots gives exactly

\[
\begin{array}{c|ccc}
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
10101010&68&18&13.
\end{array}
\]

The complement of \(Q\) is \(27\), which occurs exactly in the three rows

\[
 11110000,\qquad11101000,\qquad11001100,
\]

each at \(i=2\).  A lower target containing \(\infty\) arises only from
the internal colour family

\[
 \{\infty\}\cup([2m]\setminus\Gamma(x_i));
\]

the other depth-one colour types do not contain \(\infty\).  Hence there
are no uncounted boundary-type owners.  Suffix separation now proves

\[
 \mu_{F_m^{\rm MSW}}(S_V)=3
\]

exactly, as claimed.

The complement of \(Q'\) is \(37\).  It occurs once in the base table, in
root \(11011000\) at \(i=1\); in particular it occurs in neither of the two
base rows removed by the relevant size-two switch.

### 13.6 Transposed replacement rows and exact new multiplicity

Switching all components \(\mathcal C_{0,1100V'}\), over all suffixes
\(V'\), removes the old roots

\[
 11001100V',\qquad10101100V'
\]

and inserts their \(\tau\)-transposed wreaths.  Among the three old owners
of \(S_V\), exactly \(11001100V\) is removed, so precisely two old owners
remain.

A new row \(\tau E\) owns \(S_V\) if and only if \(E\) owns
\(\tau S_V\).  Since \(\tau\) fixes \(\infty\) and commutes with core
complementation, the upper-core word corresponding to \(\tau S_V\) is

\[
 \tau(QV)=Q'V.
\]

Suffix separation says that an old canonical owner of \(Q'V\) must have
root \(11011000V\).  No removed old row has that prefix: all have prefix
\(11001100\) or \(10101100\), even when their suffix \(V'\) varies.
Therefore none of the inserted transposed rows owns \(S_V\).  Combining
the two retained old owners with zero new owners gives

\[
 \mu_{F_m^\dagger}(S_V)=2
\]

for every \(V\).

### 13.7 Compatible balanced quotas

At depth one, every balanced quota is one or two.  If \(r_1\) denotes the
number of targets assigned quota two, then total quota \(W\) forces

\[
 r_1=W-N_1
 =W\left(1-\frac{m}{m+2}\right)
 =\frac{2W}{m+2}.
\]

Since \(t=W/(2m+1)\),

\[
 \frac{2W}{m+2}>t>\operatorname{Cat}_{m-4}
\]

for \(m\ge4\).  The targets \(S_V\) are distinct, so one may assign quota
two to all of them and distribute the remaining quota-two assignments
arbitrarily among the other targets.  Their owner sets then have size two,
while their survival packets would have size three.  Consequently none of
the resources \((1,S_V)\) generates a packet in \(F_m^\dagger\).

### 13.8 Native-cube quantitative lower bound

For each suffix write

\[
 A_V=\mathcal C_{2,V},
 \qquad B_V=\mathcal C_{0,1100V}.
\]

Unique active-atom factorization implies that the \(A_V\) are pairwise
distinct, the \(B_V\) are pairwise distinct, and no \(A_V\) equals any
\(B_{V'}\).  Hence one component of the native hierarchy is associated
with at most one suffix group.

Call \(V\) hit if \(A_V\) or \(B_V\) is switched.  Every unhit suffix
retains all three distinguished owners and therefore supplies one member of
the same pairwise-disjoint packet packing as in Section 4, for either value
of its depth-one balanced quota.

If \(L\) is the union of all switched left component sides, the patched
disjointness

\[
 F_m^{\rm MSW}\cap\tau F_m^{\rm MSW}=\varnothing
\]

gives the exact row distance

\[
 d=|L|=\sum_{K\text{ switched}}|K|.
\]

Every component has size
\(\operatorname{Cat}_j+\operatorname{Cat}_{j+1}\ge2\), and no switched
component hits two suffixes.  Therefore

\[
 \#\{V:V\text{ is hit}\}
 \le \frac d2.
\]

At least \((\operatorname{Cat}_{m-4}-d/2)_+\) unhit suffixes remain.  Their
disjoint packets prove source (6.7a).  Components unrelated to all
\(A_V,B_V\), or switching both associated components for one suffix, merely
increase \(d\) without increasing the number of hit suffixes, so neither
can invalidate the estimate.
