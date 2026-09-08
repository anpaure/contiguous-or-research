# Independent audit: coupled colored-cycle tower (lane Q)

Date: 2026-07-24

Source audited: `MATH_ATTACK_Q_COUPLED_CYCLE_TOWER_REPORT_RAW_20260724.md`.

## Verdict

The report's central mathematical picture is sound:

1. a shortest odd-graph cycle reindexed by step two is a Johnson cycle;
2. its depth-one lower edge colors are the angle colors, while its upper edge colors are automatically perfect;
3. cutting a wreath at a fixed coordinate gives complementary Johnson geodesics with the stated cap and turn colors;
4. all lower depths of one exact factor form one coupled occurrence-level cycle tower;
5. neither the known two-sided rainbow forest nor one rainbow coordinate cut supplies the missing joint Gaussian-depth factor.

Two statements require genuine correction rather than clarification:

- The fixed-coordinate correspondence is a bijection only after independently orienting every wreath, or after quotienting each Johnson path by reversal.
- The perfect-matching formulation is not equivalent to the stated `o(V)`-defect complementary-completion lemma.  It is a strictly stronger sufficient formulation unless an additional near-perfect-to-perfect repair theorem is proved.

Several other claims are valid only with narrower scope:

- “triple union” must mean three consecutive vertices in the step-two Johnson order, not the original odd-graph order;
- the displayed tower identities require the appropriate boundary range and an explicit `q=-1` upper extension at level zero;
- the `2q` seam calculation is a sharp cut-and-charge or labelled bookkeeping barrier, not an intrinsic unlabelled-overload lower bound;
- the sparse-absorber conclusion concerns `o(B)` applications of the audited `O_A(m)` local switches, not arbitrary absorbers;
- no depth-one-to-Gaussian bootstrap is proved, but nonexistence of every such bootstrap is unsupported and contradicts the report's own statement that even the global implication from depth one to depth two remains open.

The five-coordinate obstruction is valid with constant `1/32`.  Its missing proof of the depth-two collision claim can be supplied directly; a separate four-coordinate family gives the same qualitative point with density `1/16`.

No computational search was used in this audit.  The `m=4` statement is accepted only as the explicit finite certificate already printed and independently audited in the cited workspace reports.

## 1. Odd-graph/Johnson reindexing

Put

\[
n=2m+1,
\qquad
W=\binom{n}{m}.
\]

Let

\[
C_0,C_1,\ldots,C_{n-1}
\]

be one undirected `n`-cycle in `KG(n,m)`, with indices modulo `n`.

### 1.1 Step-two Johnson cycle — valid

Because `gcd(2,n)=1`,

\[
J_j=C_{2j}
\]

reindexes all vertices.  The two sets `C_{2j}` and `C_{2j+2}` are both neighbors of `C_{2j+1}` in the odd graph.  They are distinct `m`-subsets of the `(m+1)`-set `C_{2j+1}^c`.  Consequently

\[
|C_{2j}\cap C_{2j+2}|=m-1,
\qquad
C_{2j}\cup C_{2j+2}=C_{2j+1}^c.
\]

Thus `J_jJ_{j+1}` is a Johnson edge, its lower color is

\[
C_{2j}\cap C_{2j+2}=\chi_F(C_{2j+1}),
\]

and its upper color is

\[
C_{2j}\cup C_{2j+2}=C_{2j+1}^c.
\]

Across an exact factor, the central vertices `C_i` run through every `m`-set exactly once.  Complementation is a bijection between ranks `m` and `m+1`; hence every upper Johnson edge color occurs exactly once.  The report has no indexing or multiplicity error here.

Classification: **valid**.

### 1.2 Rank-`m+2` triple unions — valid after a terminology correction

In a cyclic-interval representation of the step-two Johnson row, write

\[
J_j=I_\pi(j,m).
\]

Then

\[
J_j\cup J_{j+1}\cup J_{j+2}=I_\pi(j,m+2),
\]

and

\[
I_\pi(j,m+2)^c=I_\pi(j+m+2,m-1).
\]

The shift `j -> j+m+2` is a bijection modulo `n`.  Therefore the multiset of rank-`m+2` unions of three consecutive **Johnson-row** vertices is exactly the pointwise complement of the angle-color multiset.

This assertion would be false if “three consecutive” meant the original odd-graph order.  Indeed, three consecutive odd-graph vertices have union `[n]`: the first two cover `2m` points, and the third contains the one point omitted by that union.  The report must explicitly say “three consecutive vertices of the step-two Johnson cycle.”

Classification: **correct after terminology/index clarification**.

## 2. Depth-one overload identity

For `q=1`,

\[
N_1=\binom{2m+1}{m-1},
\qquad
\frac{W}{N_1}=\frac{m+2}{m}.
\]

Hence for `m>=3`,

\[
c_1=1,
\qquad
r_1=W-N_1=\frac{2W}{m+2}.
\]

The report's formula follows from a general identity.  Suppose integer loads `mu` have total

\[
\sum_S\mu(S)=cN+r,
\qquad 0\le r<N.
\]

Put

\[
D=\sum_S(c-\mu(S))_+,
\qquad
E=\sum_S(\mu(S)-c)_+,
\qquad
t=\#\{S:\mu(S)\ge c+1\}.
\]

Conservation gives `E-D=r`.  Starting with quota `c` everywhere produces overload `E`; the `r` upper-quota bonuses can reduce that overload on exactly `min(r,t)` occupied-above-floor targets.  Therefore

\[
O=E-\min(r,t)=D+(r-t)_+.
\]

At depth one, `D=M_1`, so

\[
\boxed{O_1=M_1+(r_1-t_1)_+.}
\]

Consequently

\[
M_1\le O_1\le M_1+r_1,
\]

and, since `r_1/W=2/(m+2)`,

\[
O_1=o(W)\quad\Longleftrightarrow\quad M_1=o(W).
\]

Thus the report's exact depth-one target—an exact factor missing only `o(W)` angle colors—is correct.  It remains an unlabelled statement and does not imply common-owner synchronization.

Classification: **valid**.

## 3. Correct fixed-coordinate normal form

Fix a coordinate `z`, put

\[
Q=[2m+1]\setminus\{z\},
\qquad
V=\binom{2m}{m},
\qquad
B=\frac{V}{m+1}=\operatorname{Cat}_m.
\]

### 3.1 Orientation correction

The correct statement is:

> Undirected exact wreath factors are in bijection with families of `B` **unoriented** complementary Johnson paths of length `m`, satisfying the vertex- and edge-union partitions below.  Equivalently, one may orient every path, modulo independent reversal of each of the `B` paths.

If ordered paths

\[
X_0,X_1,\ldots,X_m
\]

are used without an orientation convention, the representation is `2^B`-to-one rather than bijective.

Classification of the report's literal “bijection”: **corrected**.

### 3.2 Forward construction

In one odd cycle there is one odd-graph edge whose omitted/transition coordinate is `z`.  Its two endpoints avoid `z`, are disjoint `m`-subsets of `Q`, and hence are complements in `Q`.  Cut this edge and follow either orientation.  The vertices alternate as

\[
X_0,A_0,X_1,A_1,\ldots,A_{m-1},X_m,
\]

where the `X_i` avoid `z` and the `A_i` contain `z`.  Since `A_i` is disjoint from both `X_i` and `X_{i+1}`,

\[
U_i=X_i\cup X_{i+1}
\]

has rank `m+1`, and

\[
A_i=\{z\}\cup(Q\setminus U_i).
\]

Also

\[
X_m=Q\setminus X_0.
\]

The path has `m` edges between complementary endpoints whose Johnson distance is `m`; it is therefore geodesic and simple.

### 3.3 Converse and exact partitions

Conversely, a complementary Johnson geodesic gives the simple odd cycle

\[
X_0,A_0,X_1,A_1,\ldots,A_{m-1},X_m,X_0
\]

with the displayed formula for `A_i`.

Across all `B` paths, exact coverage of the `z`-free middle sets is equivalent to the `X_i` occurrences partitioning

\[
\binom{Q}{m}.
\]

Exact coverage of the `z`-containing middle sets is equivalent to the `U_i` occurrences partitioning

\[
\binom{Q}{m+1},
\]

because

\[
U\longmapsto \{z\}\cup(Q\setminus U)
\]

is a bijection onto the `z`-containing `m`-sets.

The report's partition statements are therefore valid, provided “all `X_i`” and “all `U_i`” mean all occurrences across the complete family of `B` paths.

Classification: **valid after the orientation and quantifier correction**.

## 4. Fixed-coordinate angle colors and sector counts

For one reconstructed cycle, the angle colors are exactly the following multiset:

\[
\chi(A_i)=X_i\cap X_{i+1}
\qquad(0\le i<m),
\]

\[
\chi(X_0)=Q\setminus U_0,
\qquad
\chi(X_m)=Q\setminus U_{m-1},
\]

and

\[
\chi(X_i)
=\{z\}\cup\bigl(Q\setminus(U_{i-1}\cup U_i)\bigr)
\qquad(1\le i<m).
\]

The two consecutive upper colors `U_{i-1}` and `U_i` are distinct `(m+1)`-sets containing `X_i`; hence their union has rank `m+2`.  Therefore every displayed turn color has rank `m-1`.

The list is a multiset decomposition.  The two caps need not be distinct from each other or from internal intersections.

Across all paths, the exact counts are

\[
\begin{array}{c|c|c}
\text{sector}&\text{slots}&\text{targets}\\ \hline
z\text{-free}&(m+2)B&\binom{2m}{m-1}=mB\\
z\text{-containing}&(m-1)B&\binom{2m}{m-2}
=\dfrac{m(m-1)}{m+2}B.
\end{array}
\]

Both mean loads equal `(m+2)/m`.  These formulas are exact.

At an internal degree-two path vertex `X`, with incident path edges `e,f`, let their upper colors be `U_e,U_f`.  Then

\[
\kappa_X=U_e\cup U_f
\]

has rank `m+2`, and the turn angle color is its complement in the full ground set \(Q\cup\{z\}\).  This is the precise sense in which the `kappa_X` statistic is complementary to the `z`-containing angle colors.

Classification: **valid**.

## 5. Status of the two-sided rainbow forest and the completion lemma

The theorem in `GK_TWO_SIDED_RAINBOW_FOREST.md` gives a spanning Johnson forest whose retained edges have pairwise distinct lower intersections and pairwise distinct upper unions.  It does not give:

- a linear forest;
- complementary endpoints;
- turn-color control;
- a completion or reconfiguration into an exact wreath factor.

The safe wording is that the forest theorem **provides no proved** turn control or wreath-compatible completion.  It has not been proved that every completion of that particular near-spanning forest is impossible.

### 5.1 Precise collision deficits

For an exact complementary path factor, define

\[
d_{\rm int}
=mB-\#\{X_i\cap X_{i+1}:\text{all internal path edges}\},
\]

and

\[
d_{\rm turn}
=(m-1)B-\#\{U_{i-1}\cup U_i:\text{all internal pivots}\}.
\]

Let `M_free` and `M_z` be the missing angle-color counts in the `z`-free and `z`-containing sectors.  The only extra `z`-free slots are the `2B` caps, so

\[
\max(0,d_{\rm int}-2B)
\le M_{\rm free}
\le d_{\rm int}.
\]

For turns, put

\[
T_z=\binom{2m}{m-2}.
\]

Complementation is injective, and hence

\[
d_{\rm turn}
=M_z+\left((m-1)B-T_z\right)
=M_z+\frac{2(m-1)}{m+2}B.
\]

Since `B=V/(m+1)=o(V)`,

\[
M_1=o(V)
\quad\Longleftrightarrow\quad
d_{\rm int}=o(V)\text{ and }d_{\rm turn}=o(V)
\]

within an exact fixed-coordinate path factor.

Thus the colored complementary-completion lemma is not merely sufficient; its two near-rainbow conditions are asymptotically equivalent to the depth-one target once exact complementary path geometry and the upper-union partition are already present.

Classification: **valid but unproved existence lemma**, with the quantifier understood as “for every sufficiently large `m`, there exists such a factor.”

### 5.2 Perfect matching is stronger, not equivalent

Let

\[
L=\binom{Q}{m-1},
\qquad
R=\binom{Q}{m+1},
\]

and join `S in L` to `U in R` when `S subset U`.  A matched pair with

\[
U\setminus S=\{a,b\}
\]

corresponds to the Johnson edge

\[
\{S\cup\{a\},S\cup\{b\}\}.
\]

Therefore a family using every lower and upper edge color exactly once is exactly a perfect matching in this inclusion graph.

Such a perfect matching yields an exact complementary path factor precisely when its associated graph on `binom(Q,m)` is a spanning linear forest and every component has complementary endpoints.  The edge and vertex counts then force exactly `B` components and exactly `m` edges in each path.

This exact matching theorem is a stronger sufficient formulation.  The report's completion lemma only asks for

\[
d_{\rm int}=o(V),
\]

not `d_int=0`.  No theorem extends the resulting near-perfect matching to a perfect one while preserving the spanning complementary path geometry.  Accordingly “Equivalently” must be replaced by:

> A stronger exact sufficient formulation is to find a perfect inclusion matching whose associated Johnson graph is a spanning complement-ended linear forest, together with `o(V)` turn-color defect.

Classification of the claimed equivalence: **unsupported/false as stated; corrected to a stronger sufficient formulation**.

## 6. Five-coordinate complementary-geodesic obstruction

Assume `m>=3`.  Choose distinct

\[
a,b,c,d,e\in Q
\]

and, for every

\[
R\in\binom{Q\setminus\{a,b,c,d,e\}}{m-2},
\]

form the path

\[
X_0=Rac,
\quad
X_1=Rbc,
\quad
X_2=Rbd,
\quad
X_3=Rde.
\]

The traces on the five special coordinates are

\[
\begin{array}{c|c}
\text{objects}&\text{special-coordinate traces}\\ \hline
\text{vertices}&ac,bc,bd,de\\
\text{lower edge colors}&c,b,d\\
\text{upper edge colors}&abc,bcd,bde\\
\text{consecutive upper-color unions}&abcd,bcde.
\end{array}
\]

These traces determine the object type, after which the ordinary coordinates recover `R`.  Thus all vertices, lower edge colors, upper edge colors, and the two turn statistics are globally injective over all gadgets.  Complementation also makes all corresponding `z`-containing turn colors injective.

Nevertheless

\[
X_0\cap X_3=R,
\]

so the Johnson distance between `X_0` and `X_3` is `2`, whereas the gadget joins them by three edges.  Every subpath of a geodesic is geodesic.  Hence no length-`m` complementary geodesic can contain all three gadget edges.  Equivalently, coordinate `b` is inserted and later removed.

The gadgets are vertex- and edge-disjoint.  If `G` is their union and `P` is any complementary-geodesic path factor, then the exact statement is

\[
|E(G)\setminus E(P)|
\ge
\binom{2m-5}{m-2}.
\]

Moreover

\[
\frac{\binom{2m-5}{m-2}}{V}
=\frac{m(m-1)}{8(2m-1)(2m-3)}
=\frac1{32}+O\left(\frac1m\right).
\]

Thus the report's `1/32` constant and positive-density obstruction are correct.

This proves that arbitrary positive-density partial forests cannot be completed with `o(V)` retained-edge deletions from local lower/upper/turn injectivity alone.  It does not obstruct completion of the particular near-spanning forest produced by the rainbow theorem, nor any theorem with a near-spanning structural hypothesis.

The report calls turn control and geodesic geometry “independent” missing properties.  The gadget proves only that turn rainbowness does not imply geodesic geometry.  Without a reverse separation theorem, “two distinct missing properties” is the justified wording.

Classification: **valid after adding `m>=3` and fixing the exact edit-distance meaning**.

## 7. Depth-two collision obstruction

The report's assertion is true, but it omitted a construction and proof.  One explicit repair uses four fixed coordinates.  For

\[
R\in\binom{Q\setminus\{a,b,c,d\}}{m-2},
\]

take

\[
Y_0=Rab,
\quad
Y_1=Rbc,
\quad
Y_2=Rcd,
\quad
Y_3=Rda.
\]

The vertex traces are `ab,bc,cd,da`; the lower edge-color traces are `b,c,d`; and the upper edge-color traces are `abc,bcd,acd`.  Therefore all vertices and all adjacent lower and upper colors are globally injective across the family.  But

\[
Y_0\cap Y_1\cap Y_2=R
=Y_1\cap Y_2\cap Y_3.
\]

Thus every gadget repeats a depth-two lower color on two consecutive windows.  The density is

\[
\frac{\binom{2m-4}{m-2}}{V}
=\frac{m(m-1)}{4(2m-1)(2m-3)}
=\frac1{16}+O\left(\frac1m\right).
\]

The same five-coordinate gadget from Section 6 is stronger for this purpose: its two consecutive triple intersections are also both `R`, while its two turn statistics remain distinct.

These constructions prove only that generic partial-path depth-one rainbowness does not force depth-two injectivity.  They are not exact factors and do not address a near-spanning or global asymptotic implication.

Classification: **valid after supplying the omitted construction and restricting the scope to partial path forests**.

## 8. The `m=4` one-cut certificate

`MULTIDEPTH_WREATH_CUT_RESEARCH.md`, Proposition 5.1, prints fourteen explicit cyclic rows on `[9]`.  `MULTIDEPTH_WREATH_CUT_AUDIT.md` records an independent audit.  The certificate proves:

1. the rows form an exact `m=4` middle wreath factor;
2. the coordinate-`9` depth-one core triples cover every triple of `[8]` exactly once;
3. the pairs `{1,3}` and `{4,6}` occur in no cyclic rank-two window anywhere in the factor.

Thus one perfect depth-one coordinate cut need not propagate even to global depth-two coverage.  This is a valid finite theorem because the rows are explicit and the decisive equalities are finite certificate checks; the raw Q report should cite the two source files.

The certificate does not give an asymptotic family and does not establish or refute a sequence hypothesis `O_1(F_m)=o(W_m)`.  In particular it does not refute

\[
O_1=o(W)\Longrightarrow O_2=o(W),
\]

which remains open.

Classification: **valid external finite certificate; scope correctly limited, but citation missing in the raw report**.

## 9. Exact occurrence-level cycle tower

For one oriented wreath row define

\[
V^q_{\pi,j}=I_\pi(j,m-q).
\]

For cyclic intervals of length `k=m-q`,

\[
I(j,k)\cap I(j+1,k)=I(j+1,k-1),
\]

and

\[
I(j,k)\cup I(j+1,k)=I(j,k+1).
\]

Therefore

\[
V^q_{\pi,j}\cap V^q_{\pi,j+1}
=V^{q+1}_{\pi,j+1},
\]

and

\[
V^q_{\pi,j}\cup V^q_{\pi,j+1}
=V^{q-1}_{\pi,j}.
\]

The shift `j -> j+1` is a rowwise bijection, so the lower edge-color load is `mu_{q+1}` and the upper edge-color load is `mu_{q-1}`.

The missing range convention is:

- levels `0<=q<=m-1` are genuine Johnson-cycle rows;
- at `q=0`, define `V^{-1}_{pi,j}=I_pi(j,m+1)` if the upper identity is used;
- `V^m` is the terminal empty lower-color level, not a genuine cycle row;
- the union identity is false at `q=m` under the empty-window convention, because its left side is empty while `V^{m-1}` is a singleton.

This boundary correction is harmless on every fixed Gaussian window.

The conclusion that balancing `mu_1` controls the next level's vertex loads but does not, from the identities alone, control its lower edge colors `mu_2` is correct.  It is not a theorem that no additional exact-factor structure could ever produce such a bound.

Classification: **valid after the range/extension correction**.

## 10. General overload and fixed-window asymptotics

The argument in Section 2 works at every depth:

\[
\boxed{O_q=D_q+(r_q-t_q)_+.}
\]

This formula is valid exactly for integer loads of total `W`, with

\[
D_q=\sum_S(c_q-\mu_q(S))_+,
\qquad
t_q=\#\{S:\mu_q(S)\ge c_q+1\}.
\]

The binomial ratio has the symmetric product

\[
\frac{W}{N_q}
=\prod_{i=1}^q\frac{m+1+i}{m+1-i}.
\]

Consequently, uniformly for `q<=A sqrt(m)`,

\[
\log\frac{W}{N_q}
=\frac{q(q+1)}{m+1}+O_A(m^{-1})
=\frac{q(q+1)}m+O_A(m^{-1}).
\]

The report's weaker error `O_A(m^{-1/2})` is therefore safe.  For example, for fixed `A` and all sufficiently large `m`, one may take

\[
c_q\le C_A:=\left\lceil e^{A^2+1}\right\rceil.
\]

Thus the fixed-window objective

\[
\sum_{q\le A\sqrt m}\frac{O_q}{c_q}=o(W)
\]

is stated correctly and must be achieved by one exact factor, not by independent levelwise cycles or forests.

Classification: **valid; the displayed asymptotic can be sharpened**.

## 11. The `2q` seam ledger

After cutting one wreath at `z`, the full `z`-free rank-`m-q` cyclic family has

\[
m+q+1
\]

starts.  The `q`-fold internal intersections of `q+1` consecutive vertices of the complementary middle path have only

\[
m-q+1
\]

starts.  Their difference is exactly `2q`, with `q` fringe starts at each end.

Declaring every such fringe occurrence bad through `K` therefore charges

\[
2B\sum_{q=1}^Kq
=BK(K+1).
\]

For `K=ceil(A sqrt(m))` and `W=(2m+1)B`,

\[
\frac{BK(K+1)}W\longrightarrow\frac{A^2}{2}.
\]

Since `1<=c_q<=C_A`, the weighted charge lies between

\[
\frac1{C_A}BK(K+1)
\quad\text{and}\quad
BK(K+1),
\]

and is `Theta_A(W)`.

This is an exact obstruction to the naive cut-and-charge proof and, literally, to a labelled argument that declares all fringe owners mismatched.  It is not an intrinsic `Omega(W)` lower bound on unlabelled overload: ignored fringe occurrences may duplicate already covered colors or fill available quota slack.

Accordingly, “cross-seam synchronization is indispensable” is justified for this fixed-cut path-tower ledger, not as a universal theorem about every possible proof of MWB.

Classification: **arithmetic valid; universal-barrier wording corrected**.

## 12. Sparse local absorber scale

For the audited profile-3 alternating `C_8` switch, the removal/addition mass is `8` at depth one and `4q+6` for `2<=q<=m-1`; its depth-`m` effect is zero.  Optimal overload is `1`-Lipschitz under one occurrence transfer.  Hence one application changes the fixed-`A` weighted objective by at most

\[
O_A\!\left(\sum_{q\le A\sqrt m}q\right)=O_A(m).
\]

Therefore `t=o(B)` applications change the objective by

\[
o(Bm)=o(W).
\]

Such a family of local moves cannot by itself reduce a `Theta(W)` initial defect to `o(W)`.

The safe statement concerns `o(B)` **applications of these audited local moves**.  It does not cover an arbitrary nonlocal absorber, a gadget with larger action, or constants uniform in a growing `A=A(m)`.

Classification: **valid with move-class and fixed-`A` scope corrections**.

## 13. Implication audit and final classification

### Valid conclusions

- Depth-one upper Johnson edge colors are automatically perfect in every exact factor.
- For `m>=3`, depth-one overload is `o(W)` exactly when the number of missing angle colors is `o(W)`.
- The fixed-coordinate path normal form and all cap/turn/sector formulas are exact modulo path reversal.
- The colored complementary-completion lemma is a sharp asymptotic sufficient condition inside that normal form, but remains unproved.
- The five-coordinate gadget disproves black-box complementary-geodesic completion from arbitrary positive-density lower/upper/turn-rainbow partial forests.
- Generic partial-path depth-one rainbowness does not control depth-two colors.
- One perfect coordinate cut need not propagate to depth two, by the explicit `m=4` certificate.
- The occurrence-level tower identities and the general overload identity are exact in their corrected ranges.
- Fixed-window MWB requires one jointly coupled integral tower inside one exact factor.

### Corrected conclusions

- Replace “bijection with ordered paths” by “bijection with paths modulo independent reversal,” unless orientations are included as extra data.
- Replace the claimed perfect-matching equivalence by a stronger sufficient exact formulation.
- Replace “two independent missing properties” by “two distinct missing properties,” absent a reverse separation theorem.
- Replace “the forest lacks exact-factor extendibility” by “the forest theorem supplies no proved exact-factor completion or extension.”
- Replace the universal seam-barrier wording by the exact naive-ledger/labelled barrier.
- Restrict the sparse-absorber statement to `o(B)` uses of the audited `O_A(m)` local moves.
- Replace “no valid depth-one-to-Gaussian bootstrap exists” by:

  > No such bootstrap follows from the stated local rainbowness or one-cut hypotheses, and none is proved here.

### Unsupported or still unproved

- The colored complementary-completion lemma.
- A near-perfect-to-perfect inclusion-matching repair preserving complementary path geometry.
- Turn-color control or wreath-compatible completion of the particular Greene--Kleitman two-sided rainbow forest.
- Any asymptotic implication `O_1=o(W) => O_2=o(W)`, let alone a depth-one-to-Gaussian theorem.
- Existence of one exact factor with small weighted overload at all levels `q<=A sqrt(m)`.
- Any claim that the proposed completion lemma is formally the “smallest” possible new theorem; it is a natural sufficient next lemma, not a proved minimal one.
- A Gaussian analogue phrased through extra path/turn conditions may be stronger than MWB.  What is exactly equivalent to the remaining unlabelled target is the existence of one exact factor whose tower vertex loads satisfy the fixed-window overload bound.

## Final audited replacement verdict

The report should be retained after the stated corrections.  Its stable theorem-level conclusion is:

> Depth one is exactly an angle-colored Johnson-cycle factor problem with automatic upper colors, and the fixed-coordinate normal form converts it into complementary Johnson geodesics with explicit cap and turn sectors.  The known rainbow forest does not provide the required complement-ended path factor.  At higher depth, one exact wreath factor produces a coupled tower in which level-`q` vertices, lower edge colors, and upper edge colors have loads `mu_q`, `mu_{q+1}`, and `mu_{q-1}`.  The tower identities alone give no depth bootstrap.  Achieving small overload throughout a fixed Gaussian window remains a joint positive-fibre theorem—namely the unlabelled MWB gate—not a consequence of the current depth-one forest or one-cut certificates.

The decisive identities, constants, normal form, matching correction, obstruction gadgets, and implication scopes were independently audited in three separate proof checks before this report was assembled.
