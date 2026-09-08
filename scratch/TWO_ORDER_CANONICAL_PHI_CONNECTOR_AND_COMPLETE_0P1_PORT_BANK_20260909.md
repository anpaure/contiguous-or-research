# Two deletion orders complete the local 0P1 connector bank

Date: 2026-09-09. Pure constructive proof; no mathematical execution.

Every port 000D11 with nonempty Dyck D has two explicit three-edge canonical-Phi routes to the same corrected end. Their exact age conditions are complementary at a strict incoming boundary. Consequently the supplied residence-three parent factor, embedded as 0P1, supplies a disjoint connector for **every** fixed port 00D1. This is a complete local path bank, not a spanning child factor or an all-rank word construction.

## 1. Two literal routes and their canonical insertions

Let r>=2, let D be Dyck of semilength r-1, and write D=1R. On 2r+3 child sites name the first three coordinates u,x,y, the last two a,b, and the first D-coordinate d. The source is A=000D11. Define

    B   = 001D10,
    C_I = 011D00,
    C_II= 0110R10,
    E   = 1110R00.

The two routes are

    I:  A -> B -> C_I  -> E,     deletions b,a,d;
    II: A -> B -> C_II -> E,     deletions b,d,a.        (1.1)

Both routes insert y,x,u in that order. All states have rank r+1, and every edge is a strict Johnson edge through the actual canonical upper.

At A, the first global prefix minimum is -3 at y, so Phi adds y. At B it is -2 at x, so Phi adds x. At C_I, initial 011 has heights -1,0,1, the Dyck word remains above or at height1, and the final 00 only returns to -1; hence the first global minimum is at u.

For the new intermediate C_II=0110R10, the initial 0110 has heights -1,0,1,0. Since D=1R is Dyck, every prefix of R has height at least -1 and R finishes at height -1. Thus every old prefix of C_II is at least -1, with the first attainment at u. The final 10 has heights 0,-1, so it only ties that minimum. Phi again adds u. In particular

    Phi(C_II)=1110R10,                               (1.2)

and deleting a gives exactly E. Route II never visits 011D00.

The three consumed uppers are

    route I:  001D11, 011D10, 111D00;
    route II: 001D11, 011D10, 1110R10.                 (1.3)

These formulas certify the insertions directly; the new route is not merely a formal exchange of two deletions on an unverified owner sequence.

## 2. Exact age theorem and a deterministic choice

At A let beta, alpha, gamma be the ages of b,a,d, respectively. Assume a valid residence-three incoming history with beta>=3. Both alpha and gamma are at least1, and may be infinite. The deletion ages are exactly

    route I:  beta, alpha+1, gamma+2;
    route II: beta, gamma+1, alpha+2.                  (2.1)

Therefore route I is legal if and only if alpha>=2, and route II is legal if and only if gamma>=2. These statements are exact for the two specified routes, not just sufficient estimates. No other coordinate is deleted inside either route.

If the incoming edge at A is strict Johnson, at most one coordinate present at A was freshly inserted. The distinct present coordinates a and d therefore cannot both have age1. It follows that at least one route is legal. A deterministic rule is

    choose route I if alpha>=2;
    otherwise choose route II.                        (2.2)

On the second branch alpha=1 forces gamma>=2. This argument does not require a particular inverse-Phi predecessor, or the stronger no-age-two theorem for the 00D1 port family. It only needs the actual strict incoming history and mature b.

At E the inserted coordinates u,x,y have exact ages 1,2,3 in that physical order on BOTH routes. Every surviving D-coordinate has its initial age plus three, and a,b,d are absent. Hence the choice changes neither the final lower state nor the ages of any surviving coordinate. It does change the intermediate state, the third consumed upper, and the individual closed lengths of the a- and d-runs.

The condition D nonempty is essential to this construction: it supplies the distinct coordinate d. No r=1 connector is asserted.

## 3. Application to a complete specified parent factor

Take any specified strict canonical-Phi factor on 2r+1 parent sites, of lower rank r, whose positive runs have residence at least three. Embed it as 0P1, with child u fixed absent and b permanently present. The last parent coordinate is active child a. Matching commutation and preservation of the actual parent ages were proved in [the 0P1 embedding note](ACTUAL_PARENT_0P1_EMBEDDING_CONNECTOR_AGE_SUPPLY_AND_BAD_EDGE_CRITERION_20260909.md), Section 1.

Its fixed ports P=00D1 are present in the complete parent inventory. At every embedded port A, b has infinite age and the incoming parent edge is strict Johnson. Thus rule (2.2) supplies a legal route at every port. There is no remaining local input-age exception for this two-route rule.

For the actual nineteen-coordinate parent, the previous [fixed diagnostic](ACTUAL19_EMBEDDED_CORRECTED21_CONNECTOR_AGES_1371_GOOD_59_BAD_CERTIFICATE_20260909.md) found 1,371 ports where route I works and 59 where alpha=1. Equation (2.2) assigns route II to those 59. This last conclusion follows symbolically from the checked history and the theorem; no mixed-route replay has been executed by this proof's author. Any separate finite audit must retain its own source-review and execution status.

The earlier explicit bad predecessor 10D0 gives an additional direct certificate: its child image 010D01 retains every D-one into A, so gamma>=2. That inverse classification and the universal exclusion of age2 at 00D1 remain valid results, but they are not needed for the two-order existence argument.

Only the original outgoing parent edge at each selected port is replaced. Its incoming edge is not changed by the local rule, and no one-step-earlier departure is used. At a bad port that incoming source is 10D0, which is not itself a 00D1 port, so that particular incoming edge is also outside the set of replaced parent edges.

## 4. The mixed bank has no lower or consumed-upper collision

Use rule (2.2) at any selected subset of the fixed ports; in particular it may be used at all of them. All embedded lower and upper states have u=0 and b=1. Every new lower B,C_I,C_II,E has b=0 and is therefore outside the complete embedded lower inventory.

The shared B bank has prefix001. The two possible middle banks have prefix011 and are separated by a: C_I has a=0, C_II has a=1. The E bank has prefix111. Within each bank the physical suffix determines D, so every bank is injective. The shared end E(D) is used once for its single indexed port, regardless of the selected route. Thus all new lower states are mutually distinct, including across ports using different routes.

The first consumed upper 001D11 is the original embedded outgoing upper, reused once. The common second-upper bank 011D10 has b=0 and prefix011. The two third-upper banks have b=0 and prefix111, and are separated by a: 111D00 versus 1110R10. Each is injectively indexed by D. Therefore all newly consumed uppers are mutually distinct and outside the embedded upper inventory. In particular the swapped route creates no conflict with a different port's unchanged route, with any B outgoing owner, or with any retained embedded owner.

Let M=binom(2r+1,r), and select h ports. Removing their h old outgoing edges and adding their 3h routes gives

    used lower states = M+3h,
    assigned edges / consumed uppers = M+2h.           (4.1)

It gives h directed paths, plus any original components containing no selected port. Each missing incoming head is 0sigma(00D1)1. Each free outgoing end is E(D), with free upper 1110R01. These outputs are unchanged by the route choice, so the earlier immediate-closing obstruction remains: every missing head begins00, while a facet of the free upper, whose first two bits are11, cannot clear both bits in one deletion.

The inherited parent histories certify each local choice before cutting. A later global gluing must still restore sufficient capped parent ages and mature b at every exposed path head, and must respect the young output coordinates of ages1,2,3. The mixed bank does not provide that gluing, a residual matching, unused middle states, global connectivity, or an all-rank cap compiler. The former all-root first-entrance obstruction concerns a different installed edge family and is not contradicted by this path-bank theorem.

## 5. Attribution and audit status

The original b,a,d connector and its age-one failures are retained results. The induction agent derived the alternate b,d,a route, its first-minimum proof and the joint bank accounting. Root independently checked it and identified the stronger one-fresh-coordinate argument showing that the two exact age conditions always cover a strict incoming boundary. The finite-frontier agent independently read the complete proof and passed the first-minimum calculation, complementary age criteria, shared endpoint and exit ages, mixed-bank disjointness, ledger and scope. This is internal independent review. The fixed 1,371/59 count belongs to the earlier finite-frontier diagnostic; the present construction and its scope are pure proof. No new mathematical execution occurred here.

## 6. Separate finite corroboration

After this proof and independent source review, the finite-frontier agent completed one root-authorized fixed-input mixed-route audit on h100. Its [complete certificate](actual19_mixed_corrected21_connector_bank_20260909/output/actual19_mixed_corrected21_connector_bank_certificate.json) reports all 1,430 chosen routes legal: 1,371 original routes and 59 swapped routes. Every mixed lower and consumed-upper bank passed injectivity and disjointness checks, and the common endpoint and exit ages were replayed. The recorded source SHA is `a696a4cff29f93675f987a23f7b9db726642d6d3c9f9161d2cbc83ddd991902d`; CPU time was 0.553959171 seconds under the fixed 30 CPU-second / 45 wall-second / 1 GiB limits.

The induction agent reviewed the source before execution and read the completed certificate afterward, without performing a new run. This finite corroboration supplies no additional global matching, age gluing or all-rank coverage claim beyond the theorem's stated local path bank.
