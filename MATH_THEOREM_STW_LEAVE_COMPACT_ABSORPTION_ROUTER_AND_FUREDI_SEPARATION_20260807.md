# Upgrading the STW leave requires a full-profile absorber router, not only (o(W)) exceptional chains

**Date:** 2026-08-07  
**Status:** quantitative synthesis, conditional absorption theorem, and
exact robust-expansion gate.  The STW upper-half construction leaves
enough scalar room for compact rail absorbers, but its published chain-size
control does not imply the occurrence-labelled packetization or router
expansion needed to obtain depth (d+O(1)).  Such a one-sided maximum-depth
theorem would be strictly weaker than the full Füredi equitable-chain
conjecture.

## 1. Size of the STW leave

Put

\[
 R=\left\lceil\frac k2\right\rceil,
 \qquad W=\binom{k}{R},
 \qquad
 \Lambda=\sum_{s=1}^{R-1}\binom{k}{s},
\]

and let (d) be the sharp deadline.  The audited STW consequence gives an
anchored cap-(d) chain packing with leave (E) satisfying

\[
 |E|=O\!\left(\Lambda k^{-1/16+o(1)}\right).
\tag{1.1}
\]

Since (d=\Theta(\sqrt k)) and (Lambda=\Theta(Wd)),

\[
 \boxed{|E|=O\!\left(Wd,k^{-1/16+o(1)}\right)
       =O\!\left(Wk^{7/16+o(1)}\right).}
\tag{1.2}
\]

This is (o(\Lambda)), but it is not (O(W)).  In fact the average leave
per owner allowed by (1.2) is (k^{7/16+o(1)}\), which diverges.

The source of (1.1) is also important.  It is not only the
(O(Wk^{-1/8+o(1)})) atypical chains.  Typical STW chains may deviate from
the target length by (O(k^{-1/16}d)), and this diffuse error over (W)
owners is the dominant term.  Therefore a theorem acting only on the
atypical owner set cannot close (1.1).

## 2. Scalar compatibility with compact absorbers

A coupled two-size rail absorber changes only

\[
 2\ell-1
\tag{2.1}
\]

named ports on each side at width (ell).  Across the lower widths
(1\le\ell\le d), its complete exclusive footprint is

\[
 \sum_{\ell=1}^d(2\ell-1)=d^2.
\tag{2.2}
\]

At the owner width it changes (2d+1=O(d)) owners.  Consequently, if the
leave could be packed at constant density into full triangular absorber
profiles, the required number of gadgets would be

\[
 g=O(|E|/d^2)
  =O\!\left(\frac{W}{d}k^{-1/16+o(1)}\right),
\tag{2.3}
\]

and their changed-owner footprint would be

\[
 O(gd)=O\!\left(Wk^{-1/16+o(1)}\right)=o(W).
\tag{2.4}
\]

Thus there is no scalar-density obstruction: an (o(W)) protected owner
bank has enough *potential* compact-port area to process the STW leave.

Equation (2.4) must not be misread as an absorber theorem.  It assumes
that nearly all (d^2) ports of each selected gadget can be used
coherently.  If one gadget absorbs only (O(1)) arbitrary targets, the
required owner footprint is much larger than (W).  The missing gain is
therefore a full-profile packetization/expansion statement.

## 3. Full-state leave packets

Call a **compact full-state packet** (Q) the following data.

1. A bundle (E(Q)) of currently uncovered lower targets.
2. Any padding or duplicate-reserve targets needed to complete the
   per-width profile (2\ell-1).
3. A complete choice of the two-size absorber roles, base order, insertion
   cuts and state sign.
4. A literal assignment of every packet target to an entering exclusive
   port so that the resulting owner fibres are nested chains.
5. The complete coordinate-incidence residue, upper-ticket ledger,
   residence collars and common-cap tickets.

The packet is **accepting at a host** if the reference state is already
present or can be installed without losing an assigned target, and
switching to the accepting state covers (E(Q)) while retaining every
old target and all protected nonlower rows.

The coordinate-unit theorem is relevant here: the two positive states
realize (e_x-e_y) coherently at every common width.  But a general target
bundle may have a large incidence discrepancy.  A packet definition must
include an actual decomposition of that discrepancy into the available
unit gadgets.  Equal rank totals alone do not provide it.

## 4. The exact router condition

Suppose the leave has been partitioned into packets

\[
 E=E(Q_1)\mathbin{\dot\cup}\cdots\mathbin{\dot\cup}E(Q_g).
\tag{4.1}
\]

Let (mathcal P) be a bank of candidate protected absorber hosts.  Join a
packet (Q) to every entry port at which its complete literal prefix can
be installed.  After deleting the fixed reference matching, protected
collars, and already used packet interiors, let (Gamma) be the directed
alternating suffix network from those entry ports to distinct free host
sinks.

For a packet family (X), let (P_X) be the union of its admissible entry
ports and let

\[
 r_\Gamma(P_X)
\tag{4.2}
\]

be the maximum number of vertex-disjoint directed paths from (P_X) to
the free sink bank.

### Theorem 4.1 (conditional STW compact absorption)

Assume:

1. the STW cap-(d) packing and its boundary are embedded in a protected
   reference factor;
2. (4.1) is a full-state packetization with (g=O(|E|/d^2));
3. packet entry prefixes are private;
4. vertex-disjoint paths in (Gamma), together with their packets,
   compose literally and preserve owner capacity at most (d+C), all
   old lower targets, and every named upper/residence/common-cap ticket;
5. for every packet subfamily (X),

   \[
   \boxed{r_\Gamma(P_X)\ge|X|.}
   \tag{4.3}
   \]

Then the complete strict lower ideal has an anchored chain factor of
maximum depth at most (d+C).  If the protected reference factor already
contains the required upper chronology, the same switches preserve it.

#### Proof

Condition (4.3) is exactly the Rado--strict-gammoid criterion for choosing
one entry from every packet and linking the chosen entries by
vertex-disjoint paths to distinct sinks.  Integrality of gammoid
intersection supplies all (g) routes simultaneously.  Private prefixes
and Hypothesis 4 make their literal packet switches compose.  Every leave
packet is installed, no old target is lost, and no owner exceeds depth
(d+C).  The protected ticket clauses give the last assertion.
\(\square\)

The theorem is deliberately stated with the complete physical ticket in
each packet.  A target-only matching does not guarantee nested flags,
coordinate residue, upper transparency, or compiler compatibility.

## 5. A purely static adjacent-slice version

Before physical tickets are imposed, the same gate can be stated in the
ordered-slice language.  A partial cap-(q) chain factor is a family of
partial matchings

\[
 M_0:A_1\to\mathcal O,
 \qquad
 M_j:A_{j+1}\to A_j
 \quad(1\le j<q).
\]

Orient unused containment edges forward and matched edges backward in the
usual alternating network, and add a sink for every unused slice/owner
slot.  A missing target is insertable exactly when it has an alternating
path to a free sink.  A family (X) of missing targets is simultaneously
insertable exactly when the corresponding strict-gammoid rank is at least
(|X|).

Thus the exact robust static statement needed after STW is

\[
 \boxed{
 r_{\Gamma_{\rm flag}}(X)\ge|X|
 \quad\text{for every }X\subseteq E,}
\tag{5.1}
\]

after allowing the compact insertion/unit-residue exchanges as additional
certified alternating arcs.

Scalar free-slot count proves only (5.1) for (X=E) after forgetting all
incidences.  Ordinary Boolean normalized matching proves expansion between
complete rank shores.  Neither result proves (5.1) in the conditioned
STW slices after the reference chains, boundary, and protected tickets are
fixed.

## 6. Why STW alone does not imply the router

STW supplies:

* the number of chains;
* an (o(W)) count of atypical chains; and
* a bound on typical chain lengths.

It does not supply:

* rank-by-rank or named-target distribution of the leave;
* a partition of the leave into the triangular profiles (2.1);
* coordinate-moment discrepancy of leave versus reserve;
* occurrence-labelled neighborhoods in a protected absorber bank; or
* all-cut expansion after the existing chain matchings are contracted.

These omissions are logically load-bearing.  Even with enough total free
ports, all candidate packets may be forced through one capacity-one host
or one alternating bottleneck.  Then the cut (X) consisting of those
packets has

\[
 r_\Gamma(P_X)=1<|X|.
\]

Nestedness of the targets inside each packet does not rule out this cut;
the earlier two-task nested-chain configuration gives an integral failure
even after every fractional resource cut passes.

Accordingly, the shortest credible upgrade of STW is:

> **Robust full-profile flag-router theorem.**  The STW partition can be
> chosen jointly with an (o(W)) compact absorber bank so that its leave
> admits a density-(\Theta(d^2)) full-state packetization and the residual
> packet-to-sink gammoid satisfies (4.3).

This is strictly stronger than an (o(W))-exception statement and is the
exact new expansion input required by Theorem 4.1.

## 7. Relation to Füredi's conjecture

Assume only a one-sided anchored factor of the lower ideal into (W)
chains of maximum length (d+C), for an absolute constant (C).  Appending
the distinct owners gives lower-half chains of maximum (d+C+1).  In odd
dimension, complement-pairing the lower chains gives a full Boolean
(W)-chain partition of maximum length at most

\[
 2(d+C)+1
 =\frac{2^k}{W}+O(C+1).
\tag{7.1}
\]

This is a strong additive upper bound on the longest chain.  It is not the
full Füredi conclusion that all (W) chain lengths are the two integers
bracketing their average.

The distinction is numerical as well as structural.  If the average chain
length is an integer (A), the multiset with half its lengths (A-1) and
half (A+1) has average (A) and maximum (A+1), but is not equitable.
More generally, a maximum bound permits the entire total deficit below the
maximum to be concentrated on a small collection of very short chains.
The one-sided theorem supplies no lower bound on individual lengths and no
pairing rule matching short lower chains to long complementary chains.

Therefore

\[
 \boxed{
 \text{one-sided }d+O(1)
 \Longrightarrow
 \text{full-lattice maximum }\frac{2^k}{W}+O(1),
 \quad\text{not full Füredi equity}.}
\tag{7.2}
\]

In special scalar cases, an exact maximum equal to an integral average
would force every chain to have that common length.  That exceptional
observation does not turn the general (d+O(1)) statement into Füredi's
conjecture.

## 8. Verdict

The STW leave and the compact absorber have compatible asymptotic sizes:
at full triangular port density, only (o(W)) owner changes are needed.
The missing theorem is not more scalar capacity.  It is the joint
construction of:

1. a (\Theta(d^2))-dense full-state packetization of the named leave;
2. a protected compact absorber host bank; and
3. the all-cut gammoid expansion (4.3).

Until those rows are proved, STW gives (o(\Lambda)) static deficiency but
not depth (d+O(1)).  Proving the one-sided upgrade would be a major advance,
yet it would remain strictly weaker than the full equitable-chain
conjecture.
