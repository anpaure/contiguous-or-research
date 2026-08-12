# Audit and strengthening of the owner-fixed spike chart

Date: 2026-07-25

Method: pure mathematics only. No computation, search, or solver is used.

## 0. Verdict

The main theorem of PAIR_OMISSION_OWNER_FIXED_SPIKE_CHART_20260725.md is
correct, with two clarifications.

First, the pointwise fixed central object is the token incidence

\[
 (S_i,Y_i),\qquad S_i\subset Y_i,
\]

not necessarily the whole Johnson edge consisting of the two adjacent
middle owners. The other adjacent owner, and hence the upper q=1 flag,
may change.

Second, a source row must carry its factor-copy label. If two partner
pairs \(B_i,B_k\) coincide, either regard \(\theta_iF_A\) and
\(\theta_kF_A\) as separate exact factor copies, which is harmless for a
literal concatenated word, or choose one canonical bijection
\(\theta_B:A\to B\) and use the same factor

\[
 F_B=\theta_BF_A
\]

for every occurrence with partner \(B\). With this convention, overlap
or equality among the \(B_i\)'s causes no inconsistency.

After these clarifications:

* every corner is lower-saturating and middle-injective;
* all lower flags are fixed;
* every upper cross-Gram term is nonnegative;
* the floor Haar identity is exact;
* the source-row increase is at most \(2t\).

Moreover the strengthened helper construction works at every positive
upper depth, including q=1, and tensorizes over every collision fibre at
one fixed depth inside one source phase. If \(C_{\ge K}\) is the number of
same-target collision pairs belonging to fibres of multiplicity at least
\(K\), all such collisions can be exposed with at most

\[
 {4C_{\ge K}\over K-1}
\]

new source-row runs. This is the promised global high-multiplicity
collision-versus-run lemma.

At depth one there is a further current-endpoint theorem. With a fixed
marker in \(A\), the spike images are automatically distinct, and the
expected current-energy change can be written exactly. Concentrated q=1
collision mass larger than the load on those images is therefore removable
without the unresolved coherent-endpoint orientation. An optional
full-collar spike gives the analogous statement at q=2, but unlike the
helper version it need not fix the q=1 flags.

## 1. Literal source-row and factor consistency

Use the tight-row convention

\[
 S_i=I_\pi(i,m-1),\qquad
 Y_i=I_\pi(i-1,m),\qquad
 U_p^{(i)}=I_\pi(i-1,m+p).
\tag{1.1}
\]

Then

\[
 S_i\subseteq Y_i\subseteq U_p^{(i)}.
\tag{1.2}
\]

At the distinguished depth \(q\ge1\), let

\[
 b_i\in U_q^{(i)}\setminus U_{q-1}^{(i)}
\tag{1.3}
\]

be the unique entering coordinate, using \(U_0^{(i)}=Y_i\). Since
\(|U_H^{(i)}|=m+H\), the number of possible helpers is

\[
 |[n]\setminus(U_H^{(i)}\cup A)|
 =2m+1-(m+H)-2=m-H-1\ge1
\tag{1.4}
\]

when \(H\le m-2\). Choose such a helper \(z_i\), and put

\[
 B_i=\{b_i,z_i\}.
\tag{1.5}
\]

The source row avoids \(A\), while \(b_i,z_i\notin Y_i\). Hence

\[
 B_i\cap Y_i=\varnothing,\qquad B_i\cap S_i=\varnothing.
\tag{1.6}
\]

Let \(\theta_i\) exchange \(A\) and \(B_i\) coordinatewise. Equations
(1.2) and (1.6) give

\[
 \theta_iS_i=S_i,\qquad \theta_iY_i=Y_i.
\tag{1.7}
\]

The row \(\theta_i\pi\) belongs to the exact factor copy
\(\theta_iF_A\) on \([n]\setminus B_i\), and at the same start it carries
the same lower-owner incidence \((S_i,Y_i)\). Thus replacing the old row
realization by the conjugate realization does not alter any designated
lower target or middle owner.

It may alter the other middle state adjacent through \(S_i\). Therefore
“the complete central edge is fixed” is correct only if central edge means
the bipartite token incidence \(S_i\subset Y_i\). It is not a claim that
the entire Johnson edge is fixed.

Different partner pairs use different omitted-pair row systems. These
are independent physical sources and may be concatenated. If the formal
model insists on one preselected factor for each omitted pair, define
\(\theta_B\) once for each \(B\) and use \(F_B=\theta_BF_A\). Repeated
partners then use rows of the same factor. Nothing in the proof requires
disjoint partner pairs.

Because the designated owners \(Y_i\) were distinct before the operation
and remain pointwise fixed, every corner is middle-injective. Every lower
flag is a subset of \(S_i\), so (1.7) fixes all lower flags as well.

## 2. All-depth cross-Gram sign

At upper depth \(p\), write

\[
 d_{i,p}=\delta_{\theta_iU_p^{(i)}}-\delta_{U_p^{(i)}}.
\tag{2.1}
\]

Every old \(U_p^{(i)}\) avoids \(A\). If \(d_{i,p}\ne0\), then
\(U_p^{(i)}\) meets \(B_i\), and its image meets \(A\). Hence, for
\(i\ne k\),

\[
 \theta_iU_p^{(i)}\ne U_p^{(k)},\qquad
 U_p^{(i)}\ne\theta_kU_p^{(k)}.
\tag{2.2}
\]

Expanding the four unit-vector terms gives exactly

\[
 \left\langle d_{i,p},d_{k,p}\right\rangle
 =
 \mathbf1_{\{U_p^{(i)}=U_p^{(k)}\}}
 +
 \mathbf1_{\{\theta_iU_p^{(i)}=\theta_kU_p^{(k)}\}}
 \ge0.
\tag{2.3}
\]

This proof uses only the common omitted source pair \(A\); overlap among
the \(B_i\)'s is irrelevant.

For \(p<q\), the old flag \(U_p^{(i)}\) contains neither \(b_i\) nor
\(z_i\), so its innovation is zero. For \(p\ge q\), it contains \(b_i\)
and omits \(z_i\), so its nonzero image meets \(A\). At the distinguished
depth all old targets still equal \(U\).

Therefore

\[
 \left\langle d_{i,q},d_{k,q}\right\rangle
 =1+\mathbf1_{\{\theta_iU=\theta_kU\}}\ge1.
\tag{2.4}
\]

After stacking ranks with nonnegative weights,

\[
 \left\|\sum_i d_i\right\|_w^2-\sum_i\|d_i\|_w^2
 =2\sum_{i<k}\langle d_i,d_k\rangle_w
 \ge w_q^+t(t-1).
\tag{2.5}
\]

Thus the all-depth Gram assertion is valid exactly as stated.

## 3. Exact factorial-floor Haar identity

Let \(f^0\) be the old profile and

\[
 f^1=f^0+\sum_i d_i
\]

the all-spike profile. A fair independent corner is

\[
 f^\varepsilon={f^0+f^1\over2}
 +{1\over2}\sum_i\varepsilon_i d_i.
\tag{3.1}
\]

Consequently

\[
 \mathbb E\|f^\varepsilon\|_w^2
 =\left\|{f^0+f^1\over2}\right\|_w^2
  +{1\over4}\sum_i\|d_i\|_w^2,
\tag{3.2}
\]

whereas the average endpoint square has
\(\|\sum_i d_i\|_w^2/4\) in the last term. At every rank, every corner
has the same total number of flag occurrences. For

\[
 Q_c(x)=\sum_Z(x_Z-c)(x_Z-c-1),
\]

the difference from \(\sum_Zx_Z^2\) is a linear function of this fixed
mass plus a rank-dependent constant. Hence

\[
 \mathbb E Q(f^\varepsilon)
 ={Q(f^0)+Q(f^1)\over2}
  -{1\over4}\left(
    \left\|\sum_i d_i\right\|_w^2-\sum_i\|d_i\|_w^2\right).
\tag{3.3}
\]

This proves the floor Haar assertion without any divisibility assumption.
Combining (2.5) and (3.3), some integral corner lies at least

\[
 {1\over4}w_q^+t(t-1)
\]

below the higher coherent endpoint.

## 4. Exact run accounting

Remove one selected token from its old source-row run. This raises the
number of old-row components by at most one. Insert its conjugate
realization into its labelled alternate source row; treating it as a
singleton raises the number of alternate-row components by at most one.
Therefore \(t\) switches give

\[
 J(M_\varepsilon)\le J(M_0)+2t.
\tag{4.1}
\]

Coincident alternate factors or rows can only join singleton pieces and
improve this bound. The endpoint initialization cost is \(O(Ht)\). Thus
the spike chart is compatible with the coefficient-one ledger whenever
the total number of spiked tokens is \(o(W/H)\).

## 5. Global high-multiplicity collision-versus-run lemma

Fix one omitted source phase \(A\), one depth \(q\ge1\), and a family
\(\mathcal T_A\) of its selected tokens. For an upper target \(U\), put

\[
 G_U=\{i\in\mathcal T_A:U_q^{(i)}=U\},\qquad
 \mu_U=|G_U|.
\tag{5.1}
\]

Fix a threshold \(K\ge2\), and define

\[
 \mathcal U_K=\{U:\mu_U\ge K\},
\]

\[
 T_K=\sum_{U\in\mathcal U_K}\mu_U,\qquad
 C_K=\sum_{U\in\mathcal U_K}{\mu_U\choose2}.
\tag{5.2}
\]

Apply one owner-fixed spike to every occurrence in every \(G_U\),
\(U\in\mathcal U_K\). Choose a canonical conjugacy for every repeated
partner pair. The groups \(G_U\) are token-disjoint. Section 2 gives
nonnegative cross-Gram between different groups, while within \(G_U\)
it gives at least one at depth \(q\) for every unordered pair. Therefore

\[
 \boxed{
 \mathfrak A-\mathfrak V\ge2w_q^+C_K.}
\tag{5.3}
\]

Some integral corner consequently satisfies

\[
 \boxed{
 E(M_\varepsilon)
 \le\max\{E(M_0),E(M_{\rm all})\}
   -{w_q^+\over2}C_K.}
\tag{5.4}
\]

The run toll satisfies

\[
 J(M_\varepsilon)-J(M_0)\le2T_K.
\tag{5.5}
\]

Since

\[
 {\mu\choose2}\ge{\mu(K-1)\over2}\qquad(\mu\ge K),
\]

we obtain the collision-versus-run inequality

\[
 \boxed{
 J(M_\varepsilon)-J(M_0)
 \le {4C_K\over K-1}.}
\tag{5.6}
\]

Thus a fibre of multiplicity \(\mu\) exposes quadratic curvature
\(\Theta(\mu^2)\) for only linear run cost \(O(\mu)\). More generally,
the same proof applies to any token-disjoint family of collision groups
\((q_\alpha,U_\alpha,G_\alpha)\) at possibly different depths:

\[
 \mathfrak A-\mathfrak V
 \ge\sum_\alpha
 w_{q_\alpha}^+|G_\alpha|(|G_\alpha|-1).
\tag{5.7}
\]

The common-source-phase hypothesis is essential in this simultaneous
form: it is what makes every negative old/image cross equality impossible.
Charts based on different omitted source pairs need not have nonnegative
mutual Gram.

## 6. A current-relative depth-one sink

At \(q=1\), the entering coordinate is characterized by

\[
 Y_i=U\setminus\{b_i\}.
\tag{6.1}
\]

Distinct middle owners and the common old target \(U\) force the markers
\(b_i\) to be distinct within every collision fibre. Fix an ordering

\[
 A=\{a_1,a_2\},
\]

and choose every helper conjugacy so that

\[
 b_i\longleftrightarrow a_1,\qquad
 z_i\longleftrightarrow a_2.
\tag{6.2}
\]

The q=1 spike image is then

\[
 V_i=(U\setminus\{b_i\})\cup\{a_1\}
 =Y_i\cup\{a_1\}.
\tag{6.3}
\]

The map \(Y_i\mapsto Y_i\cup\{a_1\}\) is injective because every old
owner avoids \(A\). Thus the \(V_i\)'s are distinct not only within one
collision fibre, but across every selected q=1 fibre in the source phase.

Let \(b_i^\star\) denote the current q=1 load at \(V_i\), and put

\[
 B_K^{(1)}
 =\sum_{i\in\bigcup_{U\in\mathcal U_K}G_U}b_i^\star.
\tag{6.4}
\]

Assume the usual first-avoided phase separation, so a source-\(A\) old
target \(U\) has no occurrence from another phase, and take each selected
\(G_U\) to be the complete source-\(A\) occurrence fibre of \(U\).
Switching all selected occurrences then removes every selected old
collision fibre completely and adds one occurrence at each distinct
\(V_i\). Therefore

\[
 Q_1(M_{\rm all})-Q_1(M_0)
 =2\bigl(B_K^{(1)}-C_K\bigr).
\tag{6.5}
\]

At q=1, old-old Gram terms are exactly the pairs counted by \(C_K\), all
image-image terms vanish, and the negative terms are impossible. Hence

\[
 \mathfrak A-\mathfrak V=2C_K
\tag{6.6}
\]

for the energy supported only at q=1. The exact Haar identity now yields

\[
 \boxed{
 \mathbb E Q_1(M_\varepsilon)
 =Q_1(M_0)+B_K^{(1)}-\frac32C_K.}
\tag{6.7}
\]

Consequently \(C_K>(2/3)B_K^{(1)}\) gives an integral current-descending
q=1 corner with run toll at most \(4C_K/(K-1)\). Since the images are
distinct,

\[
 B_K^{(1)}\le\sum_V\mu_1(V).
\tag{6.8}
\]

The helper coordinates are used only to keep the owner and all earlier
flags fixed; they do not appear in the q=1 images. This proves the proposed
marker-based q=1 sink exactly.

## 7. An optional current-relative depth-two sink

There is a stronger conclusion at \(q=2\). For an occurrence in a
collision fibre, the two-set choice is forced:

\[
 B_i=D_i=U\setminus Y_i.
\tag{7.1}
\]

Its alternate q=2 target is

\[
 V_i=(U\setminus D_i)\cup A=Y_i\cup A.
\tag{7.2}
\]

Distinct middle owners \(Y_i\subseteq[n]\setminus A\) give distinct
targets \(V_i\). This remains true across different old collision
fibres. Let \(b_i\) be the current q=2 load at \(V_i\), and put

\[
 B_K=\sum_{i\in\bigcup_{U\in\mathcal U_K}G_U}b_i.
\tag{7.3}
\]

Assume the ordinary first-avoided phase separation: every old target
\(U\) in the source-\(A\) phase has no occurrences from another phase,
and every selected \(G_U\) is its complete occurrence fibre. Switching all
selected occurrences then removes each complete selected fibre and adds
one occurrence to each distinct \(V_i\). For the doubled
factorial-floor energy at q=2,

\[
 Q_2(M_{\rm all})-Q_2(M_0)=2(B_K-C_K).
\tag{7.4}
\]

At this single depth, image-image cross terms vanish and old-old cross
terms are exactly the pairs counted by \(C_K\). Therefore

\[
 \mathfrak A-\mathfrak V=2C_K.
\tag{7.5}
\]

Substitution in the Haar identity gives the exact current-relative law

\[
 \boxed{
 \mathbb E Q_2(M_\varepsilon)
 =Q_2(M_0)+B_K-\frac32C_K.}
\tag{7.6}
\]

In particular, if

\[
 C_K>{2\over3}B_K,
\]

some integral corner strictly decreases the current q=2 energy, with run
toll at most \(4C_K/(K-1)\). Because the \(V_i\)'s are distinct,

\[
 B_K\le\sum_V\mu_2(V),
\tag{7.7}
\]

the total q=2 flag mass. Hence every q=2 collision reservoir with
\(C_K\) larger than \(2/3\) of that total mass is unconditionally
current-descending.

This optional full-collar choice generally changes the q=1 flags. The
helper construction from Sections 1--5 fixes every earlier upper flag but
does not force distinct q=2 images. Thus (7.6) is a separate q=2 tool, not
an automatic property of every helper spike. At depths \(q>2\), selecting
partner pairs so as to control image loads is a separate matching problem.

## 8. Audit of the lower-dual spike

The lower-dual construction in the updated source note is valid for
\(q\ge2\). Suppose

\[
 L_q(e_i)=L
\]

for all selected occurrences, let

\[
 b_i\in L_{q-1}(e_i)\setminus L,
\qquad a_i\in L,
\qquad \sigma_i=(a_i\ b_i).
\tag{8.1}
\]

Because \(q\ge2\), both \(L\) and \(L_{q-1}(e_i)\) are subsets of the
central lower endpoint \(S_i=L_1(e_i)\). Hence

\[
 a_i,b_i\in S_i\subset Y_i.
\]

The transposition \(\sigma_i\) fixes \(S_i\) and \(Y_i\) setwise and acts
inside the omitted-pair complement, so \(\sigma_iF_A\) is an exact factor
on the same local universe with the same designated token incidence.
Every upper flag contains \(S_i\), and is therefore fixed setwise.

For \(p<q\), nesting gives

\[
 \{a_i,b_i\}\subseteq L_p(e_i),
\]

so the earlier lower flags are fixed. At depth q,

\[
 \sigma_iL=(L\setminus\{a_i\})\cup\{b_i\}\ne L.
\tag{8.2}
\]

For \(p>q\), every old lower flag is contained in the common set \(L\).
If its innovation is nonzero, its image contains
\(b_i\notin L\). Thus a nonzero image can never equal any old target at
that depth. The two negative unit-vector equalities vanish, while the
old-old equality at depth q contributes one for every occurrence pair.
Therefore

\[
 \left\|\sum_i d_i^-\right\|_w^2
 -\sum_i\|d_i^-\|_w^2
 \ge w_q^-t(t-1).
\tag{8.3}
\]

The same floor Haar and \(2t\)-run proofs apply. Separate conjugate factor
copies must again be retained as source-row labels when the
\(\sigma_iF_A\)'s differ.

The restriction \(q\ge2\) is real. At q=1, the last deleted coordinate
lies in \(Y_i\setminus S_i\), so swapping it with a point of
\(L_1=S_i\) would not fix the central lower endpoint.

Thus the lower-dual marker argument, including helper-free existence and
all-depth Gram sign, passes the audit exactly.

## 9. Exact remaining boundary

The audited chart solves the local legality, Gram-sign, floor, and run
questions. The high-multiplicity theorem (5.3)--(5.6) shows that
concentrated collision fibres are cheap in physical boundaries.

It does not by itself prove a global contraction from the present state:
outside the q=1 and optional q=2 sinks of Sections 6--7, the old coherent
endpoint need not be the higher one. Nor may charts from different source
phases simply be
placed in one Gram cube. The remaining global problem is therefore
narrow:

1. use long interval charts for diffuse, cross-packet collisions;
2. use (5.6) for high-multiplicity residual fibres;
3. orient or charge the coherent spike endpoint outside the current-relative
   sinks;
4. schedule source phases so the cumulative token count is \(o(W/H)\).

No coefficient-one conclusion is claimed here.
