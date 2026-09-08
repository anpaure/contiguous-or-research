# K16 G0 rank-seven hosts: no universal odd-parity law and an exact movable token

Date: 2026-07-30

Status: theorem and exact light audit PASS.  A universal odd-zero invariant is
false.  The two new old-facet-complete 5-opt carriers exhibit an integer-exact
one-token transfer.  No zero-host-free carrier is constructed here.

## 1. Exact host families

Let \({\cal R}=\binom{[16]}7\).  For a fixed exact depth-three chronology and
its maximal envelope \(E_p\), a compiler cell \(J=[s,s+\ell)\),
\(1\le\ell\le3\), has joined mask \(U_J\) and mandatory mask \(M_J\).  Its
exact rank-seven host family is

\[
 {\cal F}_J=\{T\in{\cal R}:M_J\subseteq T\subseteq U_J,
                 \ E_p\cap T\ne\varnothing\text{ for every }p\in J\}.
 \tag{1.1}
\]

Thus

\[
 h_C(T)=|\{J:T\in{\cal F}_J\}|,
 \qquad Z(C)=\{T:h_C(T)=0\}                              \tag{1.2}
\]

are physical static-host multiplicity and the zero-host set.  Formula (1.1)
is the exact maximal-envelope criterion; none of the conclusions below is
inferred merely from the number of cells.

## 2. The proposed universal parity law is false

Put \(n_j(C)=|\{T:h_C(T)=j\}|\) and
\(I(C)=\sum_T h_C(T)\).  Since

\[
 |{\cal R}|=\binom{16}{7}=11440\equiv0\pmod2,
\]

we have the exact identity

\[
 |Z(C)|\equiv I(C)+
   \sum_{\substack{j\ge2\\j\text{ even}}}n_j(C)\pmod2. \tag{2.1}
\]

Indeed, \(I\bmod2\) counts the targets of positive odd multiplicity, while
the second term adds the positive even-multiplicity targets; their sum is
the number of hosted targets, congruent to the number of unhosted targets
because \(|{\cal R}|\) is even.

The independently authenticated old state2 carriers \(u_0,u_1\) are both
exact G0 depth-three carriers with complete upper coverage, yet their exact
rank-seven ledgers are

\[
\begin{array}{c|ccccc|c|c}
 &n_0&n_1&n_2&n_3&n_4&I&Z\\ \hline
u_0&1&10057&1321&55&6&12888&\{0x4c71\}\\
u_1&2&10055&1322&55&6&12888&\{0x4879,0x4c39\}.
\end{array}                                             \tag{2.2}
\]

Their complete integer degree-vector difference is

\[
 h_{u_1}-h_{u_0}
 =-e_{0x4879}-e_{0x4c39}+e_{0x4c71}+e_{0x4a39}.         \tag{2.3}
\]

In particular, equal total incidence coexists with opposite zero parity.
This refutes an odd-zero theorem for the stated broad class, not merely a
guess based on the two new carriers.

## 3. Exact comparison of the two new 5-opt carriers

Call the two new chronologies \(C_0,C_1\).  Their cut lists are

\[
 (1058,3278,6388,9716,12826),\qquad
 (1987,3278,6388,9716,12826),                           \tag{3.1}
\]

and both have form \(A+D_3+D_1+D_4+D_2+F\).  Each preserves the exact
middle multiset, has nonzero maximal-envelope replay, is G0 depth three,
and has no upper hole.  They are related directly by

\[
C_1=C_0[:1059]\mathbin\Vert C_0[4387:5316]
 \mathbin\Vert C_0[1059:4387]\mathbin\Vert C_0[5316:], \tag{3.2}
\]

a standard three-cut block transposition of \(C_0\).

### Theorem 3.1 (integer host-token identity)

The two full static rank-seven ledgers satisfy

\[
 h_{C_1}-h_{C_0}=e_{0x1639}-e_{0x1879}.                 \tag{3.3}
\]

More strongly, in the free abelian group on nonempty unlabelled host families
(with the empty family declared zero),

\[
 \sum_{J:\mathcal F_J(C_1)\ne\varnothing}[\mathcal F_J(C_1)]
 -\sum_{J:\mathcal F_J(C_0)\ne\varnothing}[\mathcal F_J(C_0)]
   =[\{0x1639\}]-[\{0x1879\}].                         \tag{3.4}
\]

#### Proof

The exact family census gives, for either carrier,

\[
\begin{array}{c|ccccc|c}
&n_0&n_1&n_2&n_3&n_4&I\\ \hline
C_i&1&10058&1320&55&6&12887.
\end{array}                                             \tag{3.5}
\]

At the cell-family level, each has 12,869 singleton families and precisely
three nonsingleton families, of sizes \(7,6,5\), all based at the initial
cell.  The nonsingleton families are identical in \(C_0,C_1\).  Relative to
the adjacent rank-seven intersection deck, the entire common correction is

\[
2[\{0x246d\}]+[\{0x4e61\}]+[\{0x8c63\}]
 +[F_7]+[F_6]+[F_5],                                    \tag{3.6}
\]

where

\[
\begin{aligned}
F_7&=\{0x0c6d,0x286d,0x2c2d,0x2c4d,0x2c65,0x2c69,0x2c6c\},\\
F_6&=F_7\setminus\{0x0c6d\},\\
F_5&=F_6\setminus\{0x2c2d\}.
\end{aligned}                                           \tag{3.7}
\]

It remains only to compare the three changed seams in (3.2).  Their
intersections are

\[
\begin{array}{c|c|c}
 &\text{intersection}&\text{rank}\\ \hline
C_0:A|D_3&0x0639&6\\
C_0:D_3|E&0x0435&5\\
C_0:E|F&0x1879&7\\ \hline
C_1:A|E&0x1639&7\\
C_1:E|D_3&0x0439&5\\
C_1:D_3|F&0x0875&6.
\end{array}                                             \tag{3.8}
\]

Thus the adjacent rank-seven deck, and hence the full family multiset after
adding the common correction (3.6), loses exactly singleton `0x1879` and
gains exactly singleton `0x1639`.  The unmatched full cells are

\[
\begin{array}{c|c|c|c|c}
 &J&(E_p)_{p\in J}&U_J&M_J\\ \hline
C_0&[5316,5318)&(0x1871,0x1859)&0x1879&0x0838\\
C_1&[1059,1062)&(0x1039,0x1419,0x1219)&0x1639&0x0631.
\end{array}                                             \tag{3.9}
\]

This proves (3.3)--(3.4). \(\square\)

Consequently

\[
 Z(C_0)=\{0x1639\},\qquad Z(C_1)=\{0x1879\}.           \tag{3.10}
\]

The three old facet hosts are not part of the transfer.  Each remains unique
in both carriers, with the identical cells

\[
0x4c71:[6607,6609),\qquad
0x4879:[9717,9719),\qquad
0x4c39:[12164,12166).                                  \tag{3.11}
\]

This is stronger than observing one hole in each row: all other 11,438
target multiplicities agree exactly.  It is nevertheless not a local
identity of occurrence-labelled physical providers.  When cells are labelled
by their original base-row tuples, 939 target-family sets change, with 938
occurrences removed and 938 added.  Thus “one token” is exact at the
unlabelled family/multiplicity level; the chronology transporting it is
genuinely nonlocal.

## 4. What mod-2 and design data can and cannot prove

Equation (3.3) changes the odd-support XOR from `0x8ba1` to `0x85e1`.
Since

\[
0x1639\mathbin\triangle0x1879=0x0e40,
\]

the point-design parity changes on zero-based bit coordinates
\(6,9,10,11\).  Therefore
even the first point moments are not invariants of exact G0, upper-complete
carrier moves.  More generally, any additive statistic
\(L_w(h)=\sum_Tw(T)h(T)\) invariant under (3.2) must satisfy
\(w(0x1639)=w(0x1879)\).

There is also a sharp abstract countermodel to every linear
\(\mathbf F_2\) statistic of the unlabelled family-count vector, including
all linear degree/design moments.  In either new carrier, `0x8c63` has
degree four, realized by four singleton-family copies.
Replace two singleton families labelled `0x8c63` by two singleton families
labelled by the unique hole \(z\).  Algebraically,

\[
 h'=h-2e_{0x8c63}+2e_z.                                \tag{4.1}
\]

Then \(h'\) is zero-free, has the same total incidence, the same family-size
multiset, and \(h'=h\pmod2\) coordinatewise.  Hence every linear
\(\mathbf F_2\) design moment is unchanged.  This is an incidence
countermodel, not a claim that the relabelled singleton cells arise from a
physical chronology.  It preserves the exact family-size multiset, but not
occurrence-labelled cell feasibility.  It proves that a linear unlabelled
parity/design-marginal argument alone cannot establish an odd hole even in
the narrower old-facet-complete profile.

A nonlinear invariant specific to physically reachable old-facet-complete
chronologies is not excluded by these data.  No such invariant is presently
identified.

## 5. Exact constructive gate for B+1

Suppose a legal carrier move from a one-hole ledger \(h\), with hole \(z\),
has pure transfer signature

\[
 h' = h+e_z-e_a.                                       \tag{5.1}
\]

If the deleted occurrence is a singleton host at \(a\), then the move closes
the rank-seven gate exactly when \(h(a)\ge2\).  If \(h(a)=1\), it merely
moves the singleton hole to \(a\).  This is precisely the behavior of
(3.3).  A move involving a nonsingleton family needs its full vector
signature and is not covered by (5.1).

Each new carrier has

\[
1320+2\cdot55+3\cdot6=1448                         \tag{5.2}
\]

surplus full-static incidences distributed over 1,381 multi-host targets.
Thus scalar donor capacity is present.  Equation (4.1) separately shows that
no linear unlabelled-parity marginal forces a residual hole.  The nearest
multi-host targets in the Johnson graph are already explicit:

\[
\begin{array}{c|c|c}
z& a&h(a)\\ \hline
0x1639&0x9439&2\\
0x1879&0x8879&2\\
      &0x9869&2\\
      &0x9859&3.
\end{array}                                             \tag{5.3}
\]

These are search priorities, not existence witnesses.  None belongs to the
three nonsingleton families (3.7), so every listed donor occurrence is a
singleton family.  The exact remaining lemma is a chronology-legal, G0,
upper-complete transfer into the hole which deletes one such singleton
occurrence from a target of multiplicity at least two, followed by the full
lower/compiler audit.  Therefore B+1 remains plausible within carrier form;
it is not guaranteed by the present theorem.

## 6. Frozen evidence and scope

Primary carrier audit:

    scratch/k16_state2_hostseam_5opt_survivors_20260730/independent.audit.json
      SHA a189324d549d1e4caa6f6cb2b070ee30dd62df578177b76b9962180ee1f2d233

Old-carrier G0 and upper-completeness audit used in Section 2:

    scratch/k16_resident_state2_2opt3opt_20260730/independent.audit.json
      SHA 676bec9981dbbfc72c54dbe9d87212a577cc39060f54e6b7c7cd162b904d9961
      payload SHA
      150573b156c0e509ea55c9e4a3620f2729d4a009b7cf58563c1a966fbc4f50dc

New targets and envelopes:

    candidate_0.targets
      SHA 762a6361c571f4e182aa03340399d3a1c07f25755c689362da173f04bd1cc407
    candidate_0.targets.envelope
      SHA fce73774568bbec791eb59c205a287aeb58885bab140f0f4a1ce2b884957d900
    candidate_1.targets
      SHA 1e75cfb4c8e610a4ea2bf1095e44d3236f655aabc3efe65e8532912b7c0572a8
    candidate_1.targets.envelope
      SHA adc3afa8507f31cc1b78bc155d6d50c81612f008d3b63aa3af5a7c7cb5679c9b

Independent rank-seven comparison:

    scratch/audit_a_k16_state2_fiveopt_rank7_token_20260730.py
      SHA 16dfe2e7f456a8d028afb05767e3cf4e921b6601a42e0c79a99398e811bd169b
    scratch/a_k16_state2_fiveopt_rank7_token_20260730.audit.json
      SHA 941088b36e218779071055bff1600112551d3b2835b0841d669a140d113c01b9
      payload SHA
      7d8b01040d1eb12bc1916a6e14d0967e899a315382fd2b9e7ce4fd24ba3add5c

The comparison is exact for the four frozen chronologies.  It refutes a
universal odd-hole theorem and isolates a support-token gate.  It does not
prove a zero-free physical carrier, does not rule out a nonlinear invariant
on the old-facet-complete reachable subclass, and does not change the K16
bracket `12873 <= nu(16) <= 12874`.
