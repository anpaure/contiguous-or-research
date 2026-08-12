# `k=17`: the exact low-quota colored transversal over the fixed GKS surgery

Date: 2026-08-01  
Fixed input: the authenticated GKS rank-`6,7,8` controlled-surgery skeleton  
Scope: static rank-`2,...,5` attachment and completion of the nine age
partitions.  No owner-cycle order, changing-owner transition, voltage, or
opening statement is made.
Status: the exact criterion is proved below and is satisfied by the frozen
1430-row certificate audited in Section 8.

## 0. Verdict

After the fixed central surgery, let

* `S` be its 286 skip packets, with rank-six heads; and
* `P` be its 702 pair packets, with rank-seven heads.

The entire residual problem is one quota-constrained colored matching.  Its
skip and pair quotas at ranks `2,3,4,5` are

\[
 q^S=(0,20,0,127),
 \qquad
 q^P=(8,20,140,237).                                 \tag{0.1}
\]

Put

\[
 \mathcal L=\mathcal O_2\mathbin{\dot\cup}\mathcal O_3
             \mathbin{\dot\cup}\mathcal O_4
             \mathbin{\dot\cup}\mathcal O_5,        \tag{0.2}
\]

where the four orbit-set sizes are `8,40,140,364`.  The following is exact.

> Choose 20 rank-three target orbits and 127 rank-five target orbits to use
> skip packets.  They must have a joint matching into `S`.  All remaining
> low target orbits must have a joint matching into `P`.

Equivalently, there must be sets

\[
 X_3\subseteq\mathcal O_3,\qquad |X_3|=20,
 \qquad
 X_5\subseteq\mathcal O_5,\qquad |X_5|=127,          \tag{0.3}
\]

such that, for `X=X_3\mathbin{\dot\cup}X_5`,

\[
 \begin{array}{ll}
 |N_S(Y)|\ge |Y|&\text{for every }Y\subseteq X,\\
 |N_P(Z)|\ge |Z|&\text{for every }Z\subseteq
                                      \mathcal L-X.
 \end{array}                                         \tag{0.4}
\]

The neighbourhoods use aligned orbit containment in the already fixed
rank-six or rank-seven packet head.  Parallel alignment shifts are retained
in a replay certificate, although only their support enters (0.4).

If (0.3)--(0.4) hold, the two Hall matchings give exactly the bins

\[
 (A,D,G)=(139,20,127),qquad
 (B,C,E,F,H)=(297,8,20,140,237),                      \tag{0.5}
\]

and hence complete all nine static age partitions.  Conversely, every such
completion induces (0.3)--(0.4).  Thus this is not merely a relaxation.

There is no single ordinary-flow conclusion before `X_3,X_5` are chosen.
The natural fractional colored-matching system is not integral in general;
a four-target counterexample is given in Section 6.  For each fixed choice
of `X`, however, (0.4) is exactly two ordinary integral max-flow tests.

## 1. The frozen packet shores

Use the literal central skeleton

```text
scratch/threadA_k17_gks_rank678_skeleton_20260801.tsv
```

produced with the certified 286-edge surgery

```text
scratch/threadA_k17_gks_rank678_surgery_20260801.tsv
```

Its packet census is

| packet kind | count | central flag |
|---|---:|---|
| `triple` | 442 | `6<7<8` |
| `skip` | 286 | `6<8` |
| `pair_broken` | 286 | `7<8` |
| `pair_native` | 416 | `7<8` |

Let `S` be the 286 `skip` rows and let `P` be the union of the 286 broken
and 416 native pair rows.  Every packet has a fixed rank-eight root and a
fixed rank-nine current owner in this static skeleton.  Write `H_p` for its
rank-six head when `p in S` and its rank-seven head when `p in P`.

For `R in O_s`, `2<=s<=5`, and a packet `p`, retain a labelled containment
edge

\[
                         (R,p,\delta)                 \tag{1.1}
\]

when the rotation `rho^delta R` is a subset of the fixed head `H_p`.
Different valid shifts remain distinct labels.  Let `G_S` and `G_P` denote
the simple bipartite supports obtained on packet shores `S` and `P`.

No chronology is used here.  Therefore a selected low-target shift may be
chosen independently for each packet.  This independence would cease to be
valid after a common owner chronology or an absolute phase guard is imposed.

## 2. Why the quota table is forced

The certified types have the following strict-low and central suffix ranks:

| type | mass | suffix ranks | packet shore |
|---|---:|---|---|
| `A=(1,5,2,1)` | 139 | `1<6<8` | skip |
| `D=(3,3,2,1)` | 20 | `3<6<8` | skip |
| `G=(5,1,2,1)` | 127 | `5<6<8` | skip |
| `B=(1,6,1,1)` | 297 | `1<7<8` | pair |
| `C=(2,5,1,1)` | 8 | `2<7<8` | pair |
| `E=(3,4,1,1)` | 20 | `3<7<8` | pair |
| `F=(4,3,1,1)` | 140 | `4<7<8` | pair |
| `H=(5,2,1,1)` | 237 | `5<7<8` | pair |
| `I=(6,1,1,1)` | 442 | `6<7<8` | triple |

Thus rank two and rank four are forced entirely onto `P`.  Rank three must
split `20+20` between `S,P`, and rank five must split `127+237`.  The
unmatched packet counts are

\[
 |S|-(20+127)=139,
 \qquad
 |P|-(8+20+140+237)=297,                             \tag{2.1}
\]

which are exactly the `A` and `B` masses.  There is no remaining scalar
slack or rounding decision after the colored matching is chosen.

## 3. Exact colored-Hall theorem

### Theorem 3.1 (two-shore quota transversal)

The fixed GKS central skeleton extends to a static packetization using every
rank-`2,...,8` target orbit exactly once and having all nine certified type
multiplicities if and only if there are `X_3,X_5` satisfying (0.3)--(0.4).

#### Proof

Assume first that a completed packetization exists.  Let `X_3` be the
rank-three targets placed in type-`D` skip packets and `X_5` the rank-five
targets placed in type-`G` skip packets.  Their sizes are 20 and 127.  The
packetization supplies an injection of `X=X_3\mathbin{\dot\cup}X_5` into
`S`, so Hall
gives the first family in (0.4).  Every other low target lies in a packet of
type `C,E,F`, or `H`, hence is injected into `P`; Hall gives the second
family.

Conversely, use Hall to choose injections

\[
 \mu_S:X\hookrightarrow S,
 \qquad
 \mu_P:\mathcal L-X\hookrightarrow P.               \tag{3.1}
\]

Label the images as follows:

\[
\begin{array}{c|c}
\text{packet bin}&\text{image}\\ \hline
D&\mu_S(X_3)\\
G&\mu_S(X_5)\\
A&S-\mu_S(X)\\
C&\mu_P(\mathcal O_2)\\
E&\mu_P(\mathcal O_3-X_3)\\
F&\mu_P(\mathcal O_4)\\
H&\mu_P(\mathcal O_5-X_5)\\
B&P-\mu_P(\mathcal L-X).
\end{array}                                          \tag{3.2}
\]

The counts in (0.5) and the table in Section 2 follow immediately.  Choose
one recorded alignment shift on each matched containment.  The rank-six,
rank-seven, and rank-eight entries are already pairwise exact in the frozen
central skeleton.  Section 5 constructs the literal age classes.  This
gives the required static packetization. `square`

### Corollary 3.2 (exact failure alternative)

The frozen skeleton fails the low gate exactly when, for every

\[
 X_3\in{\mathcal O_3\choose20},
 \qquad X_5\in{\mathcal O_5\choose127},               \tag{3.3}
\]

at least one of the following occurs:

1. some `Y subseteq X_3\mathbin{\dot\cup}X_5` has
   `|N_S(Y)|<=|Y|-1`; or
2. some `Z subseteq \mathcal L-(X_3\mathbin{\dot\cup}X_5)` has
   `|N_P(Z)|<=|Z|-1`.

This is the exact quantifier order.  Separate Hall success for rank three
and rank five on the whole skip shore does not suffice: their matchings may
compete for the same packets.

### Proposition 3.3 (direct finite certificate)

Let `E` be the labelled edge set (1.1), and for `e in E` write `t(e)` for
its low target and `p(e)` for its packet.  The low gate is equivalently the
following binary system:

\[
 \begin{aligned}
 \sum_{e:t(e)=R}z_e&=1
     &&(R\in\mathcal L),\\
 \sum_{e:p(e)=p}z_e&\le1
     &&(p\in S\mathbin{\dot\cup}P),\\
 \sum_{\substack{e:t(e)\in\mathcal O_s\\p(e)\in S}}z_e&=q^S_s
     &&(2\le s\le5),\\
 \sum_{\substack{e:t(e)\in\mathcal O_s\\p(e)\in P}}z_e&=q^P_s
     &&(2\le s\le5),\\
 z_e&\in\{0,1\} &&(e\in E).
 \end{aligned}                                       \tag{3.4}
\]

The pair-quota row is redundant given the target equations and
`q^S_s+q^P_s=|\mathcal O_s|`, but retaining it makes a replay self-auditing.
The selected labelled edges themselves are a complete positive certificate;
their shifts verify literal containment without reconstructing a matching
algorithm.

## 4. Transversal-matroid and rank-function form

Let `M_S` and `M_P` be the transversal matroids on ground set `\mathcal L`
induced by `G_S` and `G_P`.  Thus `U subseteq \mathcal L` is independent in
`M_h` exactly when it can be injected into packet shore `h`.

Theorem 3.1 is equivalently the following quota-constrained matroid
partition statement:

\[
 \boxed{
 \begin{array}{c}
 \exists X\subseteq\mathcal L:\quad
 |X\cap\mathcal O_s|=q^S_s\ (2\le s\le5),\\
 X\in\mathcal I(M_S),
 \qquad \mathcal L-X\in\mathcal I(M_P).
 \end{array}}                                        \tag{4.1}
\]

For `A subseteq \mathcal L`, write `r_S(A),r_P(A)` for the two transversal
matroid ranks.  They are ordinary matching min--max quantities:

\[
 r_h(A)=\min_{Y\subseteq A}
             \bigl(|A-Y|+|N_h(Y)|\bigr).             \tag{4.2}
\]

Consequently an exact finite binary cut formulation is to find
`x in {0,1}^{\mathcal L}` satisfying

\[
 \begin{aligned}
 x(\mathcal O_s)&=q^S_s &&(2\le s\le5),\\
 x(A)&\le r_S(A) &&(A\subseteq\mathcal L),\\
 x(A)&\ge |A|-r_P(A) &&(A\subseteq\mathcal L).
 \end{aligned}                                       \tag{4.3}
\]

Indeed `X={u:x_u=1}` is independent in `M_S` precisely by the upper rank
inequalities.  The lower inequalities say

\[
              |A-X|\le r_P(A)\qquad(A\subseteq\mathcal L), \tag{4.4}
\]

which is equivalent to independence of `\mathcal L-X` in `M_P`.

If the quota equations are deleted, Edmonds' matroid-union theorem reduces
existence to the structural Hall family

\[
                  r_S(A)+r_P(A)\ge |A|
                  \qquad(A\subseteq\mathcal L).      \tag{4.5}
\]

The fixed quota vector is stronger.  Equation (4.5) proves only that some
shore split is possible, not that it has `20` skip rank-three and `127`
skip rank-five targets.

Another exact formulation uses two labelled copies of each low target.
On

\[
                    E=\mathcal L\times\{S,P\},       \tag{4.6}
\]

take the direct-sum matroid `M_S\oplus M_P` and the partition matroid
with capacity one on every pair `{(u,S),(u,P)}`.  A common independent set
of size 552 chooses one shore for every target and is matchable there.  The
quota rows require the exact weight vector

\[
       |I\cap(\mathcal O_s\times\{S\})|=q^S_s.       \tag{4.7}
\]

Thus the residual object is an exact-weight common independent set of
cardinality 552 (equivalently, a common base after truncating
`M_S\oplus M_P` to rank 552).  Ordinary unweighted matroid intersection
does not by itself force (4.7).

## 5. Literal completion of all nine age partitions

A positive replay certificate consists of

1. the lists `X_3,X_5`;
2. the two injections in (3.1); and
3. one containment shift `delta` witnessing every selected low-target edge.

For a skip or pair packet `p`, let

\[
 L_p\subset H_p\subset Q_p\subset T_p              \tag{5.1}
\]

be respectively its selected low target, its fixed rank-six or rank-seven
head, its fixed rank-eight root, and its fixed rank-nine current owner.  If
the assigned type is `c=(c_0,c_1,c_2,c_3)`, then

\[
 |L_p|=c_0,qquad |H_p|=c_0+c_1,qquad |Q_p|=8,
 \qquad |T_p|=9.                                    \tag{5.2}
\]

Define

\[
 C_{p,0}=L_p,qquad
 C_{p,1}=H_p-L_p,qquad
 C_{p,2}=Q_p-H_p,qquad
 C_{p,3}=T_p-Q_p.                                   \tag{5.3}
\]

These four sets are disjoint, partition `T_p`, and have sizes `c`.  For the
139 type-`A` and 297 type-`B` packets, choose any aligned singleton inside
`H_p` as `L_p`; exactly one of the 436 singleton suffix occurrences is
designated as the marked rank-one target orbit.  Repetitions among the
other unmarked singleton occurrences are allowed.

The 442 frozen triple packets receive type `I`.  Their native flag

\[
 Q_{p,6}\subset Q_{p,7}\subset Q_{p,8}\subset T_{p,9} \tag{5.4}
\]

is inserted into (5.3) with `L_p=Q_(p,6)` and `H_p=Q_(p,7)`.

The matchings use every rank-two through rank-five orbit once.  The fixed
surgery uses every rank-six, rank-seven, and rank-eight orbit once.  Hence
(5.3)--(5.4) are exactly the full nine-type static age partition system,
not merely their scalar census.

## 6. Why the outer quota choice is not one ordinary flow

For fixed `X`, the two tests in (0.4) are ordinary bipartite flows and are
integral.  Allowing `X` to vary with exact rank quotas adds a genuine colored
choice.  The natural LP obtained by adding the quota rows to the matching
polytope need not be integral, even with exactly two packet shores.

Here is a four-target witness.  Let rank class `A` contain `a_1,a_2` and
rank class `B` contain `b_1,b_2`; require one target of each class on shore
`S`.  Let

\[
 S=\{s_1,s_2\},\qquad P=\{p_1,p_2\},                \tag{6.1}
\]

with edges

\[
\begin{array}{c|cc}
 &S&P\\ \hline
 a_1&s_1&p_1\\
 a_2&s_2&p_2\\
 b_1&s_1&p_2\\
 b_2&s_2&p_1.
\end{array}                                          \tag{6.2}
\]

An integral skip choice must take one `a` and one `b`.  Equal indices
collide on `S`; unequal indices leave two complementary targets colliding
on `P`.  Hence no integral colored matching exists.  Assigning weight
`1/2` to every displayed edge satisfies every target equation, packet
capacity, and shore quota.

Therefore separate scalar counts, the uncolored union condition (4.5), or
fractional colored flow do not certify the GKS low gate.  A positive theorem
must supply the integral data of Section 5, or prove (0.3)--(0.4) for a
specific quota-valid split.

## 7. Quantifier audit and exact frontier

The valid static quantifier order is

\[
 \exists X_3, X_5\ \text{with the exact sizes}
 \quad
 \forall Y\subseteq X_3\dot\cup X_5
 \quad
 \forall Z\subseteq\mathcal L-(X_3\dot\cup X_5):    \tag{7.1}
\]

\[
               |N_S(Y)|\ge|Y|,\qquad |N_P(Z)|\ge|Z|. \tag{7.2}
\]

Hall then supplies the two injections, after which the type bins and all
age classes are deterministic up to the recorded alignment choices and
the harmless singleton choices.

It is invalid to reverse the first existential with the Hall rows by
checking each rank against the entire shore independently.  Different
ranks can pass those separate tests while requiring the same packet.

Section 8 verifies that the particular 286/702 packet shores satisfy this
criterion.  No statement about putting the resulting partitions on an
owner cycle is made.

## 8. Positive certificate and adversarial literal-phase audit

The positive certificate is

```text
scratch/threadA_k17_gks_full_static_flags_20260801.tsv
SHA256 5fc20be6e76a5ca0336ce9bc51e252d2d597f2ec2ea9ff96a54264eb050cf886
```

Its independent replay is

```text
scratch/verify_threadA_k17_gks_full_static_flags_20260801.py
SHA256 d4ffe1166f82685d8baeeb905c5ae0e2a2ce985c5b92a24db04b66fa291f791d
```

and returns `PASS_K17_GKS_FULL_STATIC_AGE_FLAGS`.  The audit payload has
SHA256
`f41e4bb870a4f2e81ecb9483461a7d41b04629594fe885a117f560feb737191d`.

### Proposition 8.1 (the fixed-surgery static gate is closed)

The certificate satisfies (3.4), hence the Hall criterion of Theorem 3.1.
It produces all nine type masses and every suffix orbit at ranks two through
eight exactly once.

More strongly, compatibility is literal rather than marginal.  On every
row the verifier checks that `C0,C1,C2,C3` are nonempty, pairwise disjoint,
have exactly the declared type sizes, and partition the same displayed
rank-nine owner.  It checks

\[
       \rho^{\text{lower_shift}}(\text{lower_rep})=C_0, \tag{8.1}
\]

and, in the packet's fixed coordinate phase,

\[
 \begin{array}{ll}
 C_0\cup C_1=\text{base}_{6},&p\in S,\\
 C_0\cup C_1=\text{base}_{7},&p\in P,\\
 C_0\cup C_1\cup C_2=Q_8,&\text{all packets},\\
 C_0\cup C_1\cup C_2\cup C_3=T_9.&
 \end{array}                                         \tag{8.2}
\]

For a moved skip head, the authenticated skeleton already has

\[
 \text{base}_6=ho^{\text{surgery rotation}}(Q_6^{\rm native})
          \subset Q_8\subset T_9.                    \tag{8.3}
\]

Equations (8.1)--(8.3) show that the low `C_0` target is placed inside the
**rotated** moved rank-six head, not inside an independently phased copy of
its native representative.  Thus there is one common literal phase from
`C_0` through the moved `Q_6`, `Q_8`, and owner.  The rank-six suffix audit
finds 728 distinct orbits, so the 286 moved heads and 442 retained heads
neither duplicate nor omit a rank-six target.

The exact suffix-orbit census is

\[
                   (8,40,140,364,728,1144,1430)       \tag{8.4}
\]

at ranks two through eight, and the quota rows are exactly (0.1).
Therefore the certificate proves joint type compatibility, not merely the
nine marginal type counts.

One replay-hardening caveat remains: the full-flag verifier consumes the
frozen skeleton and checks its SHA, but does not itself reparse the earlier
286-edge surgery TSV.  Literal moved-head alignment is certified
compositionally by the independently audited skeleton generator plus
(8.1)--(8.2).  A single monolithic verifier could additionally accept the
surgery TSV and recheck (8.3); this is a provenance hardening, not a
mathematical gap in the chained certificates.
