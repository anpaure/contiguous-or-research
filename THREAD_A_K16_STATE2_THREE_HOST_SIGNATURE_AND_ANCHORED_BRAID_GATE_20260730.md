# K16 state2: exact three-host signatures and the anchored braid gate

Date: 2026-07-30

Status: exact fixed-chronology theorem, complete comparison of the two
tail-fixed upper-complete three-opts, and a scoped minimum-four-cut theorem
for the anchored host-preserving braid. This is not an unrestricted K16
lower bound and does not change

\[
12873\leq \nu(16)\leq 12874.
\]

## 1. Frozen inputs

Let \(Q=(Q_0,\ldots,Q_{L-1})\), \(L=12873\), be a rank-eight delivery
chronology. Its no-gap delivery depths are \(d_i\in\{0,1,2,3\}\), with
scheduled middle intervals

\[
I_i=[i,i+d_i].
\]

The maximal source envelopes are

\[
P_p=\bigcap_{i:\,p\in I_i}Q_i. \tag{1.1}
\]

The two upper-complete chronologies are the pattern-4 block transpositions

\[
Q^{(a)}
 =Q[0,a]\,Q[6389,12826]\,Q[a+1,6388]\,Q[12827,L-1] \tag{1.2}
\]

at \(a=3278\) (chronology \(u_0\)) and \(a=5725\) (chronology \(u_1\)).
Their frozen data are:

* \(u_0\): target SHA
  9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b,
  envelope SHA
  57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a,
  first flat 3322, scalar capacity 29065;
* \(u_1\): target SHA
  6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0,
  envelope SHA
  20aed0f12f33d49a6abd0565da85fcc7ba5ae6ba580c8097dc1d4012bea8a6b3,
  first flat 5769, scalar capacity 31512.

Both have terminal flats 12869 and 12871, exact maximal-envelope middle
reconstruction, and no strict-upper hole.

## 2. Exact individual-host theorem

Every lower witness beginning at \(s\) must be a proper-prefix cell

\[
J=[s,s+\ell-1],\qquad 1\leq\ell\leq d_s. \tag{2.1}
\]

Indeed, a longer interval contains the scheduled rank-eight interval \(I_s\).
For such \(J\), put

\[
U_J=\bigcup_{p\in J}P_p. \tag{2.2}
\]

For \(x\in Q_i\), let

\[
C_{i,x}=\{p\in I_i:x\in P_p\}
\]

be its complete maximal-envelope carrier, and define

\[
M_J=\{x:C_{i,x}\ne\varnothing,\ C_{i,x}\subseteq J
          \text{ for some }i\}. \tag{2.3}
\]

### Theorem 2.1 (exact local host criterion)

Assume \(P_p\ne\varnothing\) and

\[
Q_i=\bigcup_{p\in I_i}P_p \qquad\text{for every }i. \tag{2.4}
\]

There is a nonempty source assignment \(A_p\subseteq P_p\) which preserves
every middle equality

\[
Q_i=\bigcup_{p\in I_i}A_p
\]

and realizes \(\bigcup_{p\in J}A_p=S\) if and only if

\[
M_J\subseteq S\subseteq U_J,\qquad
P_p\cap S\ne\varnothing\quad(p\in J). \tag{2.5}
\]

#### Proof

Necessity is literal. Since \(A_p\subseteq P_p\), the target union is
contained in \(U_J\). Nonempty \(A_p\subseteq S\cap P_p\) gives the last
condition. If \(C_{i,x}\subseteq J\), every possible carrier of the required
middle bit \(x\) lies in \(J\), so \(x\in S\).

Conversely, set

\[
A_p=P_p\cap S\quad(p\in J),\qquad
A_p=P_p\quad(p\notin J).
\]

The last condition in (2.5) makes every source cell nonempty, while
\(S\subseteq U_J\) makes the union on \(J\) exactly \(S\). A middle bit whose
carrier is not contained in \(J\) survives outside \(J\); a carrier contained
in \(J\) survives by \(M_J\subseteq S\). Thus all middle equalities survive.
\(\square\)

This is an exact one-pin theorem. Simultaneous lower pins and global
first-delivery inequalities are additional constraints.

### Corollary 2.2 (exact-envelope host)

If \(U_J=S\), then \(J\) is automatically a host. Every nonempty \(P_p\) in
\(J\) is a subset of \(S\), and every mandatory bit belongs to some such
\(P_p\).

## 3. Local adjacency formulae

Suppose first that the complete covering ancestry of cells \(s,s+1\) is
exactly the constant-depth-two collar (so no earlier depth-three row reaches
either cell). Write

\[
(X,Y,Z,W)=(Q_{s-2},Q_{s-1},Q_s,Q_{s+1}).
\]

Then

\[
P_s=X\cap Y\cap Z,\qquad P_{s+1}=Y\cap Z\cap W,
\]

and

\[
U_{[s,s+1]}=(Y\cap Z)\cap(X\cup W). \tag{3.1}
\]

For \(s\geq3\), suppose similarly that the covering ancestry is the
constant-depth-three collar, and put

\[
(A,B,C,D,E,F)=(Q_{s-3},\ldots,Q_{s+2}).
\]

For the length-three prefix,

\[
\begin{aligned}
P_s&=A\cap B\cap C\cap D,\\
P_{s+1}&=B\cap C\cap D\cap E,\\
P_{s+2}&=C\cap D\cap E\cap F,
\end{aligned}
\]

so

\[
U_{[s,s+2]}
 =C\cap D\cap\bigl((A\cap B)\cup(B\cap E)\cup(E\cap F)\bigr). \tag{3.2}
\]

Equations (2.5), (3.1), and (3.2) are the exact local
adjacency/envelope pattern. In the saturated hosts below \(U_J=S\), so the
displayed union identity proves the host after nonzero-envelope audit.

There is also a cheap necessary endpoint clause. If \(s>0\), monotonicity of
the depth schedule puts \(J\) inside both scheduled rows \(Q_{s-1}\) and
\(Q_s\). Hence

\[
S\subseteq Q_{s-1}\cap Q_s. \tag{3.3}
\]

For a saturated rank-seven host with \(Q_{s-1}\ne Q_s\), this adjacent
intersection is its exact lower colour. Equation (3.3) is only a prefilter;
(2.5) is exact.

## 4. Complete host catalogue for \(u_0,u_1\)

Write

\[
S_C=0x4c71,\qquad S_R=0x4879,\qquad S_G=0x4c39.
\]

For the two frozen chronologies, the complete proper-prefix audit is:

| chronology | mask | cell \((s,\ell)\) | envelope tuple | \(U_J\) | \(M_J\) |
|---|---:|---:|---|---:|---:|
| \(u_0\) | 0x4c71 | none | none | none | none |
| \(u_0\) | 0x4879 | \((9717,2)\) | (0x4871, 0x4079) | 0x4879 | 0x0818 |
| \(u_0\) | 0x4c39 | \((12164,2)\) | (0x4c31, 0x4c29) | 0x4c39 | 0x0c18 |
| \(u_1\) | 0x4c71 | \((3279,3)\) | (0x0c61, 0x0471, 0x4461) | 0x4c71 | 0x4830 |
| \(u_1\) | 0x4879 | none | none | none | none |
| \(u_1\) | 0x4c39 | none | none | none | none |

Every displayed host is unique within its indicated chronology. In each
empty entry, no cell in that chronology even satisfies \(S\subseteq U_J\).

This host trilemma is a property of the two frozen state2 chronologies, not
of K16 in general.  In particular, the S4 perfect-seed fixed body has three
pairwise disjoint unique literal hosts,

\[
0x4c71:\ 2300\ldots2302,\qquad
0x4879:\ 5581\ldots5583,\qquad
0x4c39:\ 6243\ldots6245. \tag{4.1}
\]

The corresponding source triples are

\[
(0x4421,0x0010,0x0c61),\quad
(0x0808,0x0050,0x4021),\quad
(0x4029,0x4c21,0x4810),
\]

respectively.  No incumbent literal host touches its free collar, but (4.1)
is already a counterexample to any global facet obstruction.  Only the local
criterion in Theorem 2.1 is chronology-independent; every incompatibility
below retains the stated state2 segment-basin hypotheses.

The exact state2 adjacent-row collars producing the displayed \(u_0,u_1\)
hosts are

\[
\begin{array}{c|c|c}
S&d&\text{middle-row collar}\\
\hline
0x4c71&3&(0x0ee5,0x0e75,0x4c75,0x4c79,0x6479,0x7469),\\
0x4879&2&(0xca71,0x4a79,0x4c79,0x6479),\\
0x4c39&2&(0x5d31,0x4d39,0x4e39,0x4f29).
\end{array} \tag{4.2}
\]

Before either upper repair, 0x4c39 had the depth-three collar

\[
(0x5935,0x5d31,0x4d39,0x4e39,0x4f29,0x47a9)
\]

and envelope tuple (0x4831, 0x4c21, 0x4429). The \(u_1\) cut is exactly
before 0x4e39. Its replacement collar

\[
(0xca71,0x4a79,0x4e39,0x4f29)
\]

gives envelopes (0x4a31, 0x4a29), whose union 0x4a39 misses precisely bit
0x0400 from 0x4c39.

## 5. The state2 protected lower/upper coboundary

The identities

\[
0x4c71=0x4c75\cap0x4c79,\qquad
0x4879=0x4a79\cap0x4c79 \tag{5.1}
\]

use the same middle row 0x4c79 within the frozen state2 catalogue but
incompatible predecessor/depth states. The \(u_0\) service seam also
satisfies

\[
0x4a79\cup0x4c79=0x4e79. \tag{5.2}
\]

Thus, on the three-mask protected ledger, the frozen head-attachment move has

\[
\text{lower }(+0x4879-0x4c71),\qquad
\text{upper service }(+0x4e79). \tag{5.3}
\]

This is not the complete signed palette of all three cut edges; the other
old and new seam colours still require full replay.

The \(u_1\) service seam instead has

\[
0x4a79\cap0x4e39=0x4a39,\qquad
0x4a79\cup0x4e39=0x4e79,
\]

and deletes the old edge

\[
0x4d39\cap0x4e39=0x4c39.
\]

It keeps the old 0x4c71 host but supplies neither of the other two named
hosts. This trade is scoped to the head-attachment pattern: reversing a
segment can retain the old predecessor edge and attach 0x4a79 on the other
side of 0x4c79.

## 6. Host transport

### Lemma 6.1 (phase-labelled collar transport)

Let \(J\) be an exact-envelope host, meaning \(U_J=S\). If a block braid
transports, in order,
every target/depth incidence used to form \(P_p\), \(p\in J\), then it
transports \(J\) to an exact host of the same mask.

In a constant depth-\(h\) phase it is enough to transport the row collar

\[
[s-h,s+\ell-1] \tag{6.1}
\]

without a cut or flat crossing it, while retaining depth \(h\).

#### Proof

The translated sliding intersections defining every \(P_p\), \(p\in J\),
are identical, so their union remains \(S\). Corollary 2.2 applies.
\(\square\)

Here the original 0x4c71 collar is cut by \(u_0\) and moved from depth three
to depth two. Its first two new envelopes become the unique 0x4879 host in
\(u_0\),
while its full three-cell union is the rank-eight row 0x4c79. The 0x4c39
collar is transported internally by \(u_0\) and contracts to its depth-two
host. The \(u_1\) cut splits that collar and loses bit 0x0400.

## 7. Anchored minimum-four-cut theorem

The preceding protected trade can be avoided at q1 by retaining

\[
L|X=0x4c75|0x4c79
\]

and attaching \(C=0x4a79\) on the other side of \(X\). The wedge \(L-X-C\)
retains lower 0x4c71, creates lower 0x4879, and creates upper 0x4e79.

Put

\[
Y=0x6479,\qquad N=0xc639.
\]

The cut edge \(X|Y\) is the unique interval witness of upper mask 0x6c79 in
the frozen state2 source.
To restore it at a new seam while using \(b_0|N\) for upper 0xc679, a third
old cut edge \(b_1|b_0\) must satisfy

\[
Y\cup b_1=0x6c79,\qquad b_0\cup N=0xc679. \tag{7.1}
\]

### Theorem 7.1 (anchored three-cut topology obstruction)

In the frozen state2 base chronology, (7.1) has exactly one oriented old-edge
solution:

\[
b_1|b_0=0x6879|0x4679
\quad\text{at positions }6387|6388. \tag{7.2}
\]

The cuts

\[
X|Y,\qquad b_1|b_0,\qquad C|N
\]

cannot be reconnected into one path while using all three required seams

\[
X|C,\qquad Y|b_1,\qquad b_0|N. \tag{7.3}
\]

Consequently this anchored host-preserving route requires at least a fourth
cut, or a different witness of one of the three upper masks.

#### Proof

Since \(N\) is a rank-eight facet of rank-nine 0xc679, the possibilities in
the second equation of (7.1) are exactly

\[
b_0=0xc679\setminus\{z\},\qquad z\in N.
\]

There are eight. The unions with \(Y\) of the two actual neighbours of their
unique occurrences are:

| \(b_0\) | \(Y\cup\operatorname{pred}(b_0)\) | \(Y\cup\operatorname{succ}(b_0)\) |
|---:|---:|---:|
| 0xc678 | 0xf679 | 0xe47d |
| 0xc671 | 0x6e79 | 0xec79 |
| 0xc669 | 0xe6f9 | 0xe679 |
| 0xc659 | 0xe67b | 0xe679 |
| 0xc479 | 0xec79 | 0xe479 |
| 0xc279 | 0xe779 | 0xe679 |
| 0x8679 | 0xf679 | 0xe67d |
| 0x4679 | 0x6c79 | 0x6679 |

Thus (7.2) is the sole solution in the frozen state2 chronology. Directly,

\[
0x6479\cup0x6879=0x6c79,\qquad
0x4679\cup0xc639=0xc679.
\]

The cuts split the old path into outer pieces and the internal segment
\(B=Y\cdots b_1\). The required seam \(Y|b_1\) joins the two ends of \(B\),
closing it into a separate cycle; the other two seams join the remaining
pieces. Thus (7.3) cannot be one path. \(\square\)

This theorem is deliberately anchored. A different three-cut may synthesize
a new 0x4c71 host rather than retain \(L|X\); q1 seam algebra alone does not
rule that out.

## 8. Complete bounded pattern-4 theorem

In the common pattern-4 service family (1.2), the seam
\(0x4a79|Q_{a+1}\) can create upper 0x4e79 only if \(Q_{a+1}\) is one of its
rank-eight facets. Before the fixed cut \(b=6388\), this leaves exactly

\[
a\in\{281,3278,4172,5626,5725,6333,6387\}. \tag{8.1}
\]

The complete exact table is:

| \(a\) | \(Q_{a+1}\) | capacity | exact middle envelope | upper holes | exact host vector \((S_C,S_R,S_G)\) |
|---:|---:|---:|:---:|---:|:---:|
| 281 | 0x4e78 | 26068 | no | 0 | n/a |
| 3278 | 0x4c79 | 29065 | yes | 0 | (0,1,1) |
| 4172 | 0x0e79 | 29959 | yes | 2 | (1,0,1) |
| 5626 | 0x4e59 | 31413 | no | 1 | n/a |
| 5725 | 0x4e39 | 31512 | yes | 0 | (1,0,0) |
| 6333 | 0x4e69 | 32120 | no | 1 | n/a |
| 6387 | 0x4679 | 32174 | no | 0 | n/a |

Thus \(u_0,u_1\) are the only carrier-valid, upper-complete rows in this
family, and neither contains all three hosts. More sharply, 0x4879 occurs
only at \(a=3278\), where 0x4c71 is absent.

For a named mask absent from the indicated \(u_0\) or \(u_1\) envelope
catalogue, a new order-preserving, phase-retaining, maximum-depth-three
state2 braid host must meet a new seam dependency collar; away from those
collars its ordered local envelope tuple is transported from that chronology.
A seam can change only the first three envelopes on its right. Including every
length-one, length-two, or length-three cell which reaches one of those
positions shows that at most

\[
3+4+5=12 \tag{8.2}
\]

cells can acquire the missing envelope coverage per seam. A flat moved
across a block is separate: that
block must be recomputed in its new phase. If an old cell already has
envelope coverage but fails a mandatory-carrier condition, its larger carrier
collar must also be audited. Equation (2.5) is the fail-closed final test.

For the anchored continuation of Theorem 7.1, the fourth cut must break the
stranded segment \(Y\cdots b_1\). To preserve the known 0x4c39 host, it must
avoid its phase-labelled collar

\[
(0x5d31,0x4d39,0x4e39,0x4f29),
\]

unless it simultaneously supplies a replacement host passing (2.5).

## 9. Audit and scope

The two chronologies and maximal envelopes were reconstructed independently
from (1.2). All proper-prefix cells were classified by (2.5), yielding

\[
u_0:(0,1,1),\qquad u_1:(1,0,0)
\]

in the stated mask order. The seven-row theorem is complete only for (1.2)
with \(b=6388,c=12826\). Theorem 7.1 is complete only for the anchored wedge
which retains 0x4c75|0x4c79, attaches 0x4a79 on the other side, and services
0xc679 through 0xc639. Neither excludes a nonstandard four-cut braid, a
three-cut synthesizing a different host, or another length-12873 chronology.
The disjoint S4 hosts in (4.1) explicitly refute extending the state2
trilemma to arbitrary K16 chronologies.

Frozen cross-checks:

* scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  host_atlas.audit.json,
  SHA 9304c90e9196d06f2eaad195f090b8f30d708ec7acc426d0edaab6b2cda24718;
* scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  three_target_literal_hosts.tsv,
  SHA 3605e399221a564a0cc354030a2ee57f2d296798517bc475ee04d8e63adf019d;
* scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/
  three_target_potential_free_intervals.tsv,
  SHA bc73bcd34318325ce89a9d73be5948d9f5a51c7c1edf60badfba00c1ddbde58b;

* scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/
  lower_hall_singleton_4c71.independent.audit.json,
  SHA c2b40f1b7b256c21cda3811a60422b70b7771294b71f98d6e966125c03002ddd;
* scratch/k16_state2_tailfixed_3opt_uppercomplete_20260730/u1/
  comp3_static.audit.json,
  SHA bc60f0a07e13fe885b5d5d6c30d72d6645fb1a09b5cd2908fb9cdf69a7320c67;
* scratch/threadD_k16_state2_threehost_standard_3opt_20260730/summary.json,
  SHA 4f9cdfe7bdc13e89b0730224b252c577c8dba3ef4ed52d685e6894e96951085b.
