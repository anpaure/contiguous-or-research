# A phase-compatible paired Kneser block gives the asymptotic two-stratum bank

Date: 2026-08-01  
Lane: endpoint-hole repair / separate-target phase bank  
Status: unconditional asymptotic resource-selection theorem and exact
endpoint ledger.  Common owner-basis extension and decorated completion
remain open.

## 0. Outcome

Put

\[
 r=m-2,\qquad |G|=2r+1,\qquad
 N={2r+1\choose r},\qquad C=\operatorname {Cat}_m .
\]

The anonymous controlled packet uses two upper resources with the same
two-special-coordinate signature.  It therefore needs

\[
                              2C\le N.                 \tag{0.1}
\]

Indeed

\[
 {2C\over N}={8(2m-1)\over m(m+1)},                \tag{0.2}
\]

so the inequality first holds at \(m=15\).  The anonymous bank therefore
cannot be used for a finite
\(m=6,7,8,9\) calibration.

The phase-compatible packet has a different target, with only its active
special coordinate.  Pairing one packet in each of the two swapped strata
removes (0.1).  This note proves that, for all sufficiently large \(m\),
one can choose \(C/2\) such paired blocks when \(C\) is even, or one
flagged odd Kneser cycle plus paired blocks when \(C\) is odd, so that
all central indices, physical owner cores, auxiliary uppers, target uppers,
and lower resources are distinct.

The chosen packets have the exact balanced endpoint vector

\[
 E_\alpha=C+s_\alpha,\qquad E_\beta=C+s_\beta,\qquad
 E_t=C\quad(t\in G),                                  \tag{0.3}
\]

where \(s_\alpha+s_\beta=C\) are the two stratum sizes.  The endpoint-hole
law is therefore satisfied by the simple balanced hole family from the
two-stratum theorem, and the packet cores may be chosen to avoid its lower
resources.

The construction also plants the literal three incidence rows of the
four-row C-phase for every packet.  It does not prove that all \(3C\)
planted rows extend to one perfect owner basis, nor that the residual
decorated two-factor exists.

## 1. One paired flagged block

Let \(S,J\) be disjoint \(r\)-sets in \(G\), and let \(u\) be the unique
point outside \(S\cup J\).  Define

\[
 L_S=G-J=S+u,\qquad L_J=G-S=J+u.                    \tag{1.1}
\]

Choose flags

\[
 b\in J,\qquad d\in S,                               \tag{1.2}
\]

and put

\[
\begin{array}{lll}
 V_S=S+b,&U_S=L_S+b,&Q_S=G-U_S=J-b,\\
 V_J=J+d,&U_J=L_J+d,&Q_J=G-U_J=S-d.
\end{array}                                          \tag{1.3}
\]

Use the directed core \(S\to J\) in stratum
\((a,z)=(\alpha,\beta)\), and \(J\to S\) in the swapped stratum.
The two phase-compatible replacements are

\[
\begin{aligned}
 (\alpha\beta L_S,\alpha S;\alpha L_S,\alpha\beta S)
 &\longmapsto
 (\alpha U_S,\alpha S;\alpha L_S,\alpha V_S)
 +(\alpha\beta L_S,\beta S;\alpha\beta S,\beta L_S),\\
 (\alpha\beta L_J,\beta J;\beta L_J,\alpha\beta J)
 &\longmapsto
 (\beta U_J,\beta J;\beta L_J,\beta V_J)
 +(\alpha\beta L_J,\alpha J;\alpha\beta J,\alpha L_J).
\end{aligned}                                        \tag{1.4}
\]

Thus it suffices to make the following abstract resources disjoint across
blocks:

\[
\begin{array}{c|c}
\text{rank in }G&\text{resources}\\ \hline
r&S,J\\
r+1&L_S,L_J,V_S,V_J\\
r-1&Q_S,Q_J.
\end{array}                                          \tag{1.5}
\]

Indeed \(Q\) determines \(U=G-Q\).  Distinct \(Q\)'s make the target
cores injective; the outer letters \(\alpha,\beta\) separate the two
target shores.  Distinct \(L\)'s make the auxiliary uppers injective.
Distinct \(V\)'s, disjoint also from all selected \(L\)'s, separate the
new owner banks from each other and from the old endpoint banks.  Distinct
\(S,J\) separate both lower banks and the middle owners.

All eight resources in (1.5) are distinct inside one block when \(r\ge2\).
For example \(L_S=S+u\ne S+b=V_S\), and a cross equality between an
\(S\)-based and a \(J\)-based \((r+1)\)-set would contain all but at most
one point of each of the two disjoint \(r\)-sets.

## 2. Exact raw and conflict counts

There are

\[
 B_0={N(r+1)\over2}r^2                              \tag{2.1}
\]

flagged paired blocks: the odd Kneser graph has \(N(r+1)/2\) edges and
each edge has \(r^2\) flag pairs.

The number of blocks using one fixed rank-\(r\) resource is

\[
                         \mu_r=(r+1)r^2.             \tag{2.2}
\]

A fixed rank-\((r+1)\) resource can occur as an \(L\)-resource in at most
\((r+1)r^2\) blocks and as a \(V\)-resource in at most the same number.
Hence

\[
                         \mu_{r+1}\le2(r+1)r^2.      \tag{2.3}
\]

For a fixed rank-\((r-1)\) resource \(Q\), choose the deleted point
\(b\notin Q\), then the opposite Kneser endpoint, then its reverse flag.
This gives

\[
                         \mu_{r-1}=(r+2)(r+1)r.      \tag{2.4}
\]

A block contains two rank-\(r\), four rank-\((r+1)\), and two
rank-\((r-1)\) resources.  Therefore it conflicts with at most

\[
\begin{aligned}
 \Delta_{\rm blk}
 &\le2\mu_r+4\mu_{r+1}+2\mu_{r-1}\\
 &\le4r(r+1)(3r+1)                                  \tag{2.5}
\end{aligned}
\]

other blocks.  Overcounting a block which shares two resources is harmless.

## 3. Greedy resource-disjoint selection

Let \(\mathcal F\) be a forbidden family of central rank-\(r\) resources.
A block meeting \(\mathcal F\) at a Kneser endpoint belongs to at most

\[
                         |\mathcal F|\mu_r           \tag{3.1}
\]

raw blocks.  After choosing \(t\) pairwise resource-disjoint blocks, at
most \(t(\Delta_{\rm blk}+1)\) blocks, including the chosen blocks
themselves, have been excluded.

The Catalan density is

\[
 {C\over N}={4(2r+3)\over(r+2)(r+3)}=O(r^{-1}).     \tag{3.2}
\]

The balanced endpoint-hole construction has a one-special-coordinate
forbidden core bank of order

\[
 |\mathcal F|\le4\operatorname {Cat}_{m-1}-C
 ={3C\over2m-1}=O(Nr^{-2}).                         \tag{3.3}
\]

For \(t\le C/2\), division by (2.1) gives

\[
 {t(\Delta_{\rm blk}+1)\over B_0}
 \le4{C\over N}{3r+1\over r}
     +{C\over N(r+1)r^2}=O(r^{-1}),\qquad
 {|\mathcal F|\mu_r\over B_0}
 \le {2|\mathcal F|\over N}=O(r^{-2}).              \tag{3.4}
\]

Both terms tend to zero.  Hence, for all sufficiently large \(m\), the
greedy algorithm can select \(C/2\) disjoint blocks when \(C\) is even.
It avoids every central core in \(\mathcal F\) and is disjoint in all
three resource ranks in (1.5).

### Theorem 3.1 (even bank)

For every sufficiently large \(m\) with even \(C\), there is a
resource-disjoint family of \(C/2\) paired blocks.  Assigning opposite
strata inside each block gives exactly \(C/2\) packets in each stratum.
All typed resources in (1.4) are distinct, and the packet lower bank is
disjoint from the prescribed balanced hole family.

## 4. Odd Catalan order

Suppose \(C\) is odd.  Use one standard directed odd cycle of length

\[
                              n=2r+1.                              \tag{4.1}
\]

Identify \(G\) with \(\mathbb Z/n\mathbb Z\).  For every cyclic start
\(s\), put

\[
 S_s=\{s,s+1,\ldots,s+r-1\},\qquad
 J_s=\{s+r,s+r+1,\ldots,s+2r-1\}.                               \tag{4.2}
\]

Ordering starts by \(s\mapsto s+r\) traverses all starts and makes
consecutive vertices disjoint.  Flag the arc \(S_s\to J_s\) by

\[
                              b_s=s+r+1.                          \tag{4.3}
\]

The associated \(L\)-bank consists of all cyclic \((r+1)\)-intervals,
whereas \(V_s=S_s+b_s\) is not a cyclic interval.  Thus \(V\) avoids
\(L\).  The \(V_s\) are distinct.  The \(Q_s=J_s-b_s\) are also
distinct: equality for two deleted cyclic \(r\)-intervals would force
adjacent starts and deletion of a boundary point, while (4.3) deletes the
second point.  The assertion at \(r=2\) follows by the same boundary check.

Hence the entire odd cycle is a resource-disjoint flagged packet seed.
Its endpoint contribution telescopes to \(n\mathbf1_G\).  A uniformly
random coordinate permutation of this cycle avoids the forbidden central
family \(\mathcal F\)
for all sufficiently large \(r\), because its expected intersection is

\[
                              {n|\mathcal F|\over N}=O(r^{-1}).   \tag{4.4}
\]

Reserve its \(O(r)\) resources.  Since \(C-n\) is even, apply the greedy
proof to \((C-n)/2\) paired blocks avoiding the seed.  The added loss is
\(O(r\Delta_{\rm blk})\), still negligible relative to \(B_0\).  Label
the odd-cycle vertices so that the total stratum sizes differ by one.

### Theorem 4.1 (all sufficiently large dimensions)

For every sufficiently large \(m\), regardless of the parity of \(C\),
there is a phase-compatible, resource-disjoint two-stratum packet bank of
order \(C\), together with a simple disjoint lower-hole family, satisfying

\[
                              E=H+2c\mathbf1.                    \tag{4.5}
\]

The two stratum sizes lie in the exact interval

\[
                         C-2c\le s_\alpha,s_\beta\le2c.          \tag{4.6}
\]

## 5. Four-row phase interface

For the packet \(S\to J\) in stratum \((a,z)\), plant

\[
                    aS\mapsto aL_S,\qquad
                    zS\mapsto azS,\qquad
                    L_S\mapsto zL_S.                            \tag{5.1}
\]

Across the selected bank these are \(3C\) distinct incidence rows.  They
are exactly the local C-phase rows of the four-row SCD grammar.  Let
\(\mathcal D_P,\mathcal I_P\) be their domain and image banks.  Extension
to one perfect owner basis is equivalent to

\[
 |N(X)\setminus\mathcal I_P|\ge |X|
 \quad\text{for every }
 X\subseteq{\Omega\choose m-1}\setminus\mathcal D_P.             \tag{5.2}
\]

The resource selection theorem does not prove (5.2).  Nor does it prove
that the selected central pairs occur in one SCD.

## 6. Exact scope

The theorem closes the asymptotic packet-selection and endpoint-hole
interface for the corrected separate-target phases.  It also explains why
the finite shared-signature packet bank is pigeonhole impossible before
\(m=15\).

The following remain separate:

1. the common-owner-basis Hall condition (5.2);
2. residual upper/lower/owner-slot saturation;
3. the graphic condition that every residual component is a path;
4. residence, higher shadows, and compiler compatibility.

In particular, no decorated two-factor or contiguous-OR equality word is
claimed.
